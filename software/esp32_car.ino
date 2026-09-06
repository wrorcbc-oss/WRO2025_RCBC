#include <ESP32Servo.h>

// ======================================================
//                    PIN DEFINITIONS
// ======================================================

// Ultrasonic Sensors
#define TRIG_FRONT 4
#define ECHO_FRONT 5

#define TRIG_LEFT  18
#define ECHO_LEFT  19

#define TRIG_RIGHT 21
#define ECHO_RIGHT 22

// DC Motor Control (L298N / Driver)
#define IN1        27
#define IN2        26
#define MOTOR_PWM  14

// Servo Motor Control
#define SERVO_PIN  13


// ======================================================
//                    STEERING SETTINGS
// ======================================================

const int STEERING_CENTER    = 90;
const int STEERING_MAX_LEFT  = 55;
const int STEERING_MAX_RIGHT = 125;


// ======================================================
//              SPEED SETTINGS (SLIGHTLY FASTER)
// ======================================================

const int SPEED_NORMAL    = 135;  
const int SPEED_CORNER    = 95;   
const int SPEED_OBSTACLE  = 100;  
const int SPEED_CLEARANCE = 135;  


// ======================================================
//                    WALL FOLLOWING
// ======================================================

const float TARGET_DIST     = 20.0;
const float WALL_DEADBAND   = 2.0;
const int WALL_CORRECTION   = 18;


// ======================================================
//                    CORNER SETTINGS
// ======================================================

const float FRONT_CORNER_DIST = 60.0;
const float FRONT_CLEAR_DIST  = 75.0;

const unsigned long MIN_CORNER_TIME = 250;
const unsigned long MAX_CORNER_TIME = 1000;

unsigned long cornerStartTime = 0;
int cornerDirection = STEERING_CENTER;
bool inCorner = false;


// ======================================================
//                    VISION & OBSTACLE DATA
// ======================================================

char visionMode       = 'N';  
char obstacleColor    = 'N';
float obstacleError   = 0.0;
float obstacleDistance = 0.0;
int visionSteerAngle  = 90;

float visionLeftArea  = 0.0;
float visionRightArea = 0.0;
int visionTurnCount   = 0;

// Parking marker data (received from vision over UART, header 'M').
// Stored only — no parking maneuver logic is implemented yet.
bool  parkingMarkersFound = false;
float parkingGapError     = 0.0;
float parkingGapWidth     = 0.0;

unsigned long lastObstacleTime = 0;
const unsigned long CLEARANCE_TIME = 500;

unsigned long lastVisionTime = 0;
const unsigned long VISION_TIMEOUT = 500;


// ======================================================
//                    SENSOR FILTERS
// ======================================================

float distFront = 400.0;
float distLeft  = 400.0;
float distRight = 400.0;

float filteredLeft  = 400.0;
float filteredRight = 400.0;

bool filterInitialized = false;
const float FILTER_ALPHA = 0.30;


// ======================================================
//                    SERVO OBJECT
// ======================================================

Servo steeringServo;


// ======================================================
//              ULTRASONIC SENSOR FUNCTION
// ======================================================

float getUltrasonicDistance(int trigPin, int echoPin)
{
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);

    digitalWrite(trigPin, LOW);

    long duration = pulseIn(echoPin, HIGH, 25000);

    if (duration == 0)
        return 400.0;

    return (duration * 0.0343) / 2.0;
}


// ======================================================
//                    READ ALL SENSORS
// ======================================================

void readAllSensors()
{
    float rawFront = getUltrasonicDistance(TRIG_FRONT, ECHO_FRONT);
    float rawLeft  = getUltrasonicDistance(TRIG_LEFT, ECHO_LEFT);
    float rawRight = getUltrasonicDistance(TRIG_RIGHT, ECHO_RIGHT);

    if (!filterInitialized)
    {
        distFront = rawFront;
        filteredLeft = rawLeft;
        filteredRight = rawRight;
        distLeft = rawLeft;
        distRight = rawRight;
        filterInitialized = true;
        return;
    }

    distFront     = 0.35 * rawFront + 0.65 * distFront;
    filteredLeft  = FILTER_ALPHA * rawLeft + (1.0 - FILTER_ALPHA) * filteredLeft;
    filteredRight = FILTER_ALPHA * rawRight + (1.0 - FILTER_ALPHA) * filteredRight;

    distLeft  = filteredLeft;
    distRight = filteredRight;
}


// ======================================================
//             READ & PARSE VISION DATA (SERIAL)
// ======================================================

void readVisionData()
{
    while (Serial.available() > 0)
    {
        String data = Serial.readStringUntil('\n');
        data.trim();

        if (data.length() == 0)
            continue;

        char header = data.charAt(0);
        visionMode = header;

        if (header == 'A')
        {
            sscanf(data.c_str(), "A,%f,%f,%f,%d,%d",
                   &visionLeftArea,
                   &visionRightArea,
                   &obstacleError,
                   &visionSteerAngle,
                   &visionTurnCount);

            obstacleColor = 'N';
            lastVisionTime = millis();
        }
        else if (header == 'R' || header == 'G' || header == 'B')
        {
            char col;
            sscanf(data.c_str(), "%c,%f,%f,%d",
                   &col,
                   &obstacleError,
                   &obstacleDistance,
                   &visionSteerAngle);

            obstacleColor = col;
            lastVisionTime = millis();
        }
        else if (header == 'C')
        {
            obstacleColor = 'C';
            sscanf(data.c_str(), "C,%f", &obstacleError);
            lastVisionTime = millis();
        }
        else if (header == 'M')
        {
            // Parking-gap data from the magenta markers.
            // Parsed and stored only — no maneuver is triggered here.
            int found = 0;
            sscanf(data.c_str(), "M,%d,%f,%f", &found, &parkingGapError, &parkingGapWidth);
            parkingMarkersFound = (found == 1);
            lastVisionTime = millis();
        }
        else if (header == 'N')
        {
            obstacleColor = 'N';
            obstacleDistance = 0.0;
            obstacleError = 0.0;
            visionSteerAngle = STEERING_CENTER;
            lastVisionTime = millis();
        }
    }

    if (millis() - lastVisionTime > VISION_TIMEOUT)
    {
        obstacleColor = 'N';
        visionMode = 'N';
    }
}


// ======================================================
//                    MOTOR CONTROL
// ======================================================

void setMotor(int speed, bool forward)
{
    speed = constrain(speed, 0, 255);

    if (forward)
    {
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
    }
    else
    {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
    }

    analogWrite(MOTOR_PWM, speed);
}

void stopMotor()
{
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    analogWrite(MOTOR_PWM, 0);
}


// ======================================================
//                    SERVO CONTROL
// ======================================================

void setSteering(int angle)
{
    int clampedAngle = constrain(angle, STEERING_MAX_LEFT, STEERING_MAX_RIGHT);
    int invertedAngle = 180 - clampedAngle;
    steeringServo.write(invertedAngle);
}

void centerSteering()
{
    setSteering(STEERING_CENTER);
}


// ======================================================
//                    CORNER LOGIC
// ======================================================

void startCorner()
{
    if (inCorner) return;

    inCorner = true;
    cornerStartTime = millis();

    if (distRight > distLeft)
        cornerDirection = STEERING_MAX_RIGHT;
    else
        cornerDirection = STEERING_MAX_LEFT;
}

bool handleCorner()
{
    if (!inCorner) return false;

    unsigned long elapsed = millis() - cornerStartTime;

    if (elapsed > MAX_CORNER_TIME)
    {
        inCorner = false;
        centerSteering();
        return false;
    }

    setSteering(cornerDirection);
    setMotor(SPEED_CORNER, true);

    if (elapsed < MIN_CORNER_TIME)
        return true;

    if (distFront > FRONT_CLEAR_DIST)
    {
        inCorner = false;
        centerSteering();
        return false;
    }

    return true;
}

void detectCorner()
{
    if (inCorner) return;

    if (distFront > 0 && distFront < FRONT_CORNER_DIST)
    {
        startCorner();
    }
}


// ======================================================
//                VISION OBSTACLE AVOIDANCE
// ======================================================

bool handleVisionObstacle()
{
    if (obstacleColor == 'N')
        return false;

    if (obstacleDistance <= 0 || obstacleDistance > 50)
        return false;

    if (obstacleColor == 'R')
    {
        lastObstacleTime = millis();
        setSteering(STEERING_MAX_RIGHT);
        setMotor(SPEED_OBSTACLE, true);
        return true;
    }

    if (obstacleColor == 'G')
    {
        lastObstacleTime = millis();
        setSteering(STEERING_MAX_LEFT);
        setMotor(SPEED_OBSTACLE, true);
        return true;
    }

    return false;
}


// ======================================================
//                  CLEARANCE STATE
// ======================================================

bool clearanceState()
{
    if (millis() - lastObstacleTime < CLEARANCE_TIME)
    {
        centerSteering();
        setMotor(SPEED_CLEARANCE, true);
        return true;
    }
    return false;
}


// ======================================================
//               WALL & AREA VISION FOLLOWING
// ======================================================

void wallFollowing()
{
    int steering = STEERING_CENTER;

    if (visionMode == 'A')
    {
        steering = visionSteerAngle;
    }
    else
    {
        if (distRight < 70.0 && distLeft >= 70.0)
        {
            float error = distRight - TARGET_DIST;
            if (abs(error) <= WALL_DEADBAND)
                steering = STEERING_CENTER;
            else if (error > 0)
                steering = STEERING_CENTER + WALL_CORRECTION;
            else
                steering = STEERING_CENTER - WALL_CORRECTION;
        }
        else if (distLeft < 70.0 && distRight >= 70.0)
        {
            float error = distLeft - TARGET_DIST;
            if (abs(error) <= WALL_DEADBAND)
                steering = STEERING_CENTER;
            else if (error > 0)
                steering = STEERING_CENTER - WALL_CORRECTION;
            else
                steering = STEERING_CENTER + WALL_CORRECTION;
        }
        else if (distLeft < 70.0 && distRight < 70.0)
        {
            float centerError = distLeft - distRight;
            if (abs(centerError) > 2.0)
                steering = STEERING_CENTER - (int)(centerError * 2.0);
            else
                steering = STEERING_CENTER;
        }
    }

    setSteering(steering);
    setMotor(SPEED_NORMAL, true);
}


// ======================================================
//                        SETUP
// ======================================================

void setup()
{
    Serial.begin(115200);
    // Prevents readStringUntil() in readVisionData() from blocking the main
    // loop for up to the default 1000ms if a line arrives without its '\n'
    // terminator (communication-layer fix only — no driving logic changed).
    Serial.setTimeout(10);

    pinMode(TRIG_FRONT, OUTPUT);
    pinMode(ECHO_FRONT, INPUT);

    pinMode(TRIG_LEFT, OUTPUT);
    pinMode(ECHO_LEFT, INPUT);

    pinMode(TRIG_RIGHT, OUTPUT);
    pinMode(ECHO_RIGHT, INPUT);

    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(MOTOR_PWM, OUTPUT);

    ESP32PWM::allocateTimer(0);
    ESP32PWM::allocateTimer(1);
    ESP32PWM::allocateTimer(2);
    ESP32PWM::allocateTimer(3);

    steeringServo.setPeriodHertz(50);
    steeringServo.attach(SERVO_PIN, 500, 2500);

    centerSteering();
    stopMotor();
    lastVisionTime = millis();

    delay(1000);
}


// ======================================================
//                      MAIN LOOP
// ======================================================

void loop()
{
    readAllSensors();
    readVisionData();

    if (handleVisionObstacle())
    {
        delay(15);
        return;
    }

    if (clearanceState())
    {
        delay(15);
        return;
    }

    if (handleCorner())
    {
        delay(15);
        return;
    }

    detectCorner();
    if (inCorner)
    {
        handleCorner();
        delay(15);
        return;
    }

    wallFollowing();

    if (visionTurnCount >= 12)
    {
        stopMotor();
        while (true) {
            // Stop vehicle upon completing 3 laps
        }
    }

    delay(15);
}
