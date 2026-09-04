import cv2 as cv
import numpy as np

def nothing(x):
    pass


cv.namedWindow("Trackbars")
cv.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv.createTrackbar("L - S", "Trackbars", 100, 255, nothing)
cv.createTrackbar("L - V", "Trackbars", 100, 255, nothing)
cv.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv.createTrackbar("U - V", "Trackbars", 255, 255, nothing)
cv.createTrackbar("Min Area", "Trackbars", 1000, 10000, nothing) # لتجربة المساحة

capture = cv.VideoCapture(0) 

while True:
    ret, frame = capture.read()
    if not ret:
        break
        
    blur = cv.GaussianBlur(frame, (5, 5), 0)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
    
    
    l_h = cv.getTrackbarPos("L - H", "Trackbars")
    l_s = cv.getTrackbarPos("L - S", "Trackbars")
    l_v = cv.getTrackbarPos("L - V", "Trackbars")
    u_h = cv.getTrackbarPos("U - H", "Trackbars")
    u_s = cv.getTrackbarPos("U - S", "Trackbars")
    u_v = cv.getTrackbarPos("U - V", "Trackbars")
    min_area = cv.getTrackbarPos("Min Area", "Trackbars")
    
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    
    
    mask = cv.inRange(hsv, lower_bound, upper_bound)
    
    kernel = np.ones((5, 5), np.uint8)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > min_area:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(frame, (x, y), (x + w, h + y), (0, 255, 0), 2)
            
    cv.imshow("Frame", frame)
    cv.imshow("Mask", mask)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        print(f"the best color:")
        print(f"Lower: [{l_h}, {l_s}, {l_v}]")
        print(f"Upper: [{u_h}, {u_s}, {u_v}]")
        print(f"Min Area: {min_area}")
        break

capture.release()
cv.destroyAllWindows()