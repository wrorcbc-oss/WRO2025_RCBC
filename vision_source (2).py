import cv2 as cv
import numpy as np
import serial
import time

capture = cv.VideoCapture(0)

# ser = serial.Serial("COM8", 115200)
time.sleep(2)

kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = capture.read()
    h, w = frame.shape[:2]
    frame_center = (w // 2, h // 2)

    blur = cv.GaussianBlur(frame, (5, 5), 0)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    lower_green = np.array([35, 80, 80])
    upper_green = np.array([90, 255, 255])

    lower_lane = np.array([0, 0, 200])
    upper_lane = np.array([180, 50, 255])

    red_mask1 = cv.inRange(hsv, lower_red1, upper_red1)
    red_mask2 = cv.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv.bitwise_or(red_mask1, red_mask2)

    green_mask = cv.inRange(hsv, lower_green, upper_green)
    lane_mask = cv.inRange(hsv, lower_lane, upper_lane)

    red_mask = cv.morphologyEx(red_mask, cv.MORPH_OPEN, kernel)
    red_mask = cv.morphologyEx(red_mask, cv.MORPH_CLOSE, kernel)

    green_mask = cv.morphologyEx(green_mask, cv.MORPH_OPEN, kernel)
    green_mask = cv.morphologyEx(green_mask, cv.MORPH_CLOSE, kernel)

    lane_mask = cv.morphologyEx(lane_mask, cv.MORPH_OPEN, kernel)
    lane_mask = cv.morphologyEx(lane_mask, cv.MORPH_CLOSE, kernel)

    lane_mask[:h // 2, :] = 0

    cv.line(frame, (w // 2, 0), (w // 2, h), (255, 255, 255), 2)
    cv.circle(frame, frame_center, 5, (255, 255, 255), -1)

    red_contours, _ = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    green_contours, _ = cv.findContours(green_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if red_contours:
        contour = max(red_contours, key=cv.contourArea)
        area = cv.contourArea(contour)

        if area > 1000:
            x, y, bw, bh = cv.boundingRect(contour)
            rect_area = bw * bh
            solidity = area / rect_area if rect_area > 0 else 0

            if solidity > 0.5:
                cx = x + bw // 2
                cy = y + bh // 2

                cv.rectangle(frame, (x, y), (x + bw, y + bh), (0, 0, 255), 3)
                cv.circle(frame, (cx, cy), 6, (255, 255, 255), -1)
                cv.line(frame, frame_center, (cx, cy), (0, 0, 255), 2)

                cv.putText(frame, f"RED X={cx}", (x, y - 10),
                           cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                if cx < frame_center[0]:
                    print(f"RED is on the LEFT side | X = {cx}")
                else:
                    print(f"RED is NOT on the LEFT side | X = {cx}")

    if green_contours:
        contour = max(green_contours, key=cv.contourArea)
        area = cv.contourArea(contour)

        if area > 1000:
            x, y, bw, bh = cv.boundingRect(contour)
            rect_area = bw * bh
            solidity = area / rect_area if rect_area > 0 else 0

            if solidity > 0.5:
                cx = x + bw // 2
                cy = y + bh // 2

                cv.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 3)
                cv.circle(frame, (cx, cy), 6, (255, 255, 255), -1)
                cv.line(frame, frame_center, (cx, cy), (0, 255, 0), 2)

                cv.putText(frame, f"GREEN X={cx}", (x, y - 10),
                           cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                if cx > frame_center[0]:
                    print(f"GREEN is on the RIGHT side | X = {cx}")
                else:
                    print(f"GREEN is NOT on the RIGHT side | X = {cx}")

    cv.imshow("Detection", frame)
    cv.imshow("Red Mask", red_mask)
    cv.imshow("Green Mask", green_mask)
    cv.imshow("Lane Mask", lane_mask)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()