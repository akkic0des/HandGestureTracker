import cv2
import mediapipe as mp
import pyautogui
import time




# declare variables for the line connecting dots
x1 =y1 =x2 =y2 =0

# main code body
webcam = cv2.VideoCapture(0)

webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

myHands = mp.solutions.hands.Hands()
drawingUtils= mp.solutions.drawing_utils
while True:
    ret, image = webcam.read()
    if not ret:
        print("Failed to grab the frame")
        break

    frame_height, frame_width, frame_depth = image.shape
    
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = myHands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawingUtils.draw_landmarks(image,hand)
        landmarks = hand.landmark
        for (id, landmark) in enumerate(landmarks):
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            if id ==8:
                cv2.circle(img=image, center=(x,y), radius= 8, color=(0,0,255), thickness= 3)
                x1=x
                y1=y
            if id ==4:
                 cv2.circle(img=image, center=(x,y), radius= 8, color=(255,0,0), thickness= 3)
                 x2=x
                 y2=y
                 
        if x1 and y1 and x2 and y2:
            
            distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
            cv2.line(image,(x1,y1),(x2,y2),(0,255,0),5)

            if distance>50:
                pyautogui.press("volumeup")
                time.sleep(0)
            else:
                pyautogui.press("volumedown")
                time.sleep(0)

    cv2.imshow("Hand Volume Control using Python", image)
    key= cv2.waitKey(10)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
