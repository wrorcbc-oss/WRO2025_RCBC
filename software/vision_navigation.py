import cv2 as cv
import numpy as np
import serial 


# 1. Initialization & Setup


# esp32 = serial.Serial('COM3', 115200, timeout=0.1) 

capture = cv.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)

# Control parameters
kp = 0.05               
offset_multiplier = 1.5 

while True:
    ret, frame = capture.read()
    if not ret:
        break
        
    
    # 2. Image Preprocessing
    
    blur = cv.GaussianBlur(frame, (5, 5), 0)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
    
    h, w = frame.shape[:2]
    frame_center_x = w // 2 
    
    #  HSV Bounds 
    # Traffic Signs 
    lower_red1, upper_red1 = np.array([0, 100, 100]), np.array([10, 255, 255])
    lower_red2, upper_red2 = np.array([170, 100, 100]), np.array([180, 255, 255])
    lower_green, upper_green = np.array([35, 80, 80]), np.array([90, 255, 255])
    
    # Track Navigation: Masking the White Floor (Drivable Area between Black Walls)
    # Adjust these thresholds based on the venue's lighting conditions
    lower_lane = np.array([0, 0, 200])      # High value/brightness for white floor
    upper_lane = np.array([180, 50, 255])

    # Parking lot limiters (RGB 255,0,255 -> magenta hue band in OpenCV's 0-179 scale)
    lower_magenta = np.array([140, 100, 100])
    upper_magenta = np.array([165, 255, 255])
    
    # --- Masks Creation ---
    red_mask = cv.bitwise_or(cv.inRange(hsv, lower_red1, upper_red1), 
                             cv.inRange(hsv, lower_red2, upper_red2))
    green_mask = cv.inRange(hsv, lower_green, upper_green)
    lane_mask = cv.inRange(hsv, lower_lane, upper_lane)
    magenta_mask = cv.inRange(hsv, lower_magenta, upper_magenta)
    
    # Morphology (Noise Removal)
    red_mask = cv.morphologyEx(red_mask, cv.MORPH_OPEN, kernel)
    green_mask = cv.morphologyEx(green_mask, cv.MORPH_OPEN, kernel)
    lane_mask = cv.morphologyEx(lane_mask, cv.MORPH_OPEN, kernel)
    magenta_mask = cv.morphologyEx(magenta_mask, cv.MORPH_OPEN, kernel)
    
    
    # 3. ROI (Region of Interest) for Track Floor Tracking
    
    # Ignore the top half of the frame to avoid detecting ambient light outside the field
    roi_top_boundary = h // 2
    lane_mask[0:roi_top_boundary, :] = 0 
    
    # 4. State Machine & Object Detection
    
    red_contours, _ = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    green_contours, _ = cv.findContours(green_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    lane_contours, _ = cv.findContours(lane_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    target_cx = None 
    action_text = "LOST (STOP)" 

    # STATE 1: Avoid Red Pillar -> Keep to the Right Side [WRO Rule 5]
    if red_contours and cv.contourArea(max(red_contours, key=cv.contourArea)) > 1000:
        contour = max(red_contours, key=cv.contourArea)
        x, y, bw, bh = cv.boundingRect(contour)
        if (cv.contourArea(contour) / (bw * bh)) > 0.5:
            cx = x + bw // 2
            cy = y + bh // 2
            target_cx = cx - int(bw * offset_multiplier) # Shift path to the left of the pillar
            action_text = "AVOID RED"
            cv.rectangle(frame, (x, y), (x + bw, y + bh), (0, 0, 255), 3)
            cv.circle(frame, (target_cx, cy), 8, (255, 0, 0), -1)

    # STATE 2: Avoid Green Pillar -> Keep to the Left Side [WRO Rule 5]
    elif green_contours and cv.contourArea(max(green_contours, key=cv.contourArea)) > 1000:
        contour = max(green_contours, key=cv.contourArea)
        x, y, bw, bh = cv.boundingRect(contour)
        if (cv.contourArea(contour) / (bw * bh)) > 0.5:
            cx = x + bw // 2
            cy = y + bh // 2
            target_cx = cx + int(bw * offset_multiplier) # Shift path to the right of the pillar
            action_text = "AVOID GREEN"
            cv.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 3)
            cv.circle(frame, (target_cx, cy), 8, (255, 0, 0), -1)

    # STATE 3: Center on White Track Floor (Default when no pillars are visible)
    elif lane_contours:
        contour = max(lane_contours, key=cv.contourArea)
        if cv.contourArea(contour) > 500: 
            # Calculate the center of mass of the visible white floor section
            M = cv.moments(contour)
            if M['m00'] > 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                target_cx = cx # Target is the exact center of the white drivable corridor
                action_text = "CENTER ON TRACK"
                
                # Visual feedback of the calculated corridor center
                cv.drawContours(frame, [contour], -1, (255, 255, 0), 2)
                cv.circle(frame, (cx, cy), 8, (255, 255, 0), -1)

    # STATE 4: Parking marker detection (runs every frame, independent of the
    # driving state above - the ESP32 decides when to act on it, only after
    # it has counted 3 completed laps).
    magenta_contours, _ = cv.findContours(magenta_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    marker_centers = []
    for cnt in magenta_contours:
        area = cv.contourArea(cnt)
        if area > 150:  # tune: markers look small in frame from a distance
            mx, my, mw, mh = cv.boundingRect(cnt)
            marker_centers.append(mx + mw // 2)
            cv.rectangle(frame, (mx, my), (mx + mw, my + mh), (255, 0, 255), 2)
    marker_centers.sort()

    if len(marker_centers) >= 2:
        left_marker, right_marker = marker_centers[0], marker_centers[-1]
        gap_center = (left_marker + right_marker) // 2
        gap_error = gap_center - frame_center_x   # +ve = gap sits right of centre
        gap_width = right_marker - left_marker
        both_markers_found = 1
        cv.putText(frame, f"PARKING GAP | Err: {gap_error} W: {gap_width}",
                   (10, 60), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
    else:
        gap_error = 0
        gap_width = 0
        both_markers_found = 0

    # Send to ESP32 - matches the "M,<found>,<gapError>,<gapWidth>" case
    # added to readVisionData() in control.ino.
    # esp32.write(f"M,{both_markers_found},{gap_error},{gap_width}\n".encode('utf-8'))

    
    # 5. Steering Control & Serial Communication
    
    if target_cx is not None:
        error = target_cx - frame_center_x
        steering_angle = error * kp 
        
        # Clamp steering limits to prevent servo strain
        if steering_angle > 0.5: steering_angle = 0.5
        elif steering_angle < -0.5: steering_angle = -0.5
            
        # Send steering command to ESP32
        # esp32.write(f"S:{steering_angle:.2f}\n".encode('utf-8')) 
        
        cv.putText(frame, f"{action_text} | Err: {error} | Steer: {steering_angle:.2f}", 
                   (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv.line(frame, (frame_center_x, h), (target_cx, h//2), (255, 0, 255), 2)
                   
    else:
        # No track floor or pillars detected (Emergency stop state)
        # esp32.write(b"S:0.00\n")
        cv.putText(frame, "TRACK LOST", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    
    # 6. Display (Debug Windows)
    
    cv.imshow("Detection", frame)
    # cv.imshow("White Floor Mask", lane_mask) # Uncomment to calibrate white color under event lights
    
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()