import cv2
import numpy as np
import random
 
roi = None
 
upper_color = np.array([255, 255, 255], dtype='uint8')
lower_color = np.array([0, 100, 100], dtype='uint8')
 
 
COLORS = ['R', 'G', "B"]
 
red_mask = [np.array([0, 100, 50]), np.array([6, 255, 255])]
green_mask = [np.array([30, 100, 50]), np.array([70, 255, 255])]
blue_mask = [np.array([80, 100, 50]), np.array([110, 255, 255])]
 
def set_upper(x):
    global upper_color
    upper_color[0] = x
 
 
def set_lower(x):
    global lower_color
    lower_color[0] = x
 
 
cam = cv2.VideoCapture(0)
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)

 
def find_circle(frame_inp, color):
    blurred = cv2.GaussianBlur(frame_inp, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
 
    mask = cv2.inRange(hsv, color[0], color[1])
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
 
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = max(contours, key=cv2.contourArea)
        (curr_x, curr_y), radius = cv2.minEnclosingCircle(c)
        if radius > 30:
            return int(curr_x), int(curr_y), int(radius)
    return None
 
 
def find_line(red_ball, green_ball, blue_ball):
    if red_ball and green_ball and blue_ball:
        ball_data = [{"data": red_ball, "color": "R"},
                     {"data": green_ball, "color": "G"},
                     {"data": blue_ball, "color": "B"}]
        ball_data.sort(key=lambda x: x['data'][0])
        if ball_data[0]['color'] == colors[0] and ball_data[1]['color'] == colors[1] and ball_data[2]['color'] == colors[2]:
            cv2.putText(frame, f'You did it', (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (205, 92, 92))

 
if __name__ == '__main__':
    colors = COLORS
    random.shuffle(colors)
    print(colors)
    while cam.isOpened():
        ret, frame = cam.read()
 
        red_ball = find_circle(frame, red_mask)
        green_ball = find_circle(frame, green_mask)
        blue_ball = find_circle(frame, blue_mask)
 
        if red_ball:
            cv2.circle(frame, (red_ball[0], red_ball[1]), red_ball[2], (0, 255, 255), 2)
        if green_ball:
            cv2.circle(frame, (green_ball[0], green_ball[1]), green_ball[2], (0, 255, 255), 2)
        if blue_ball:
            cv2.circle(frame, (blue_ball[0], blue_ball[1]), blue_ball[2], (0, 255, 255), 2)
 
        find_line(red_ball, green_ball, blue_ball)
 
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
 
        cv2.imshow("Camera", frame)
 
    cam.release()
    cv2.destroyAllWindows()