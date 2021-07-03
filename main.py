from datetime import datetime
import keyboard
import cv2
import numpy as np
import pyautogui

time_stamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')


output = f"{time_stamp}.avi"

img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

height, width, channels = img.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output, fourcc, 15, (width, height))

webcam = cv2.VideoCapture(0)

while True:
    img = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    _, frame = webcam.read()
    temp = cv2.resize(frame, (200, 200), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
    fr_height, fr_width, _ = temp.shape

    image[0:fr_height, 0: fr_width, :] = temp[0: fr_height, 0: fr_width, :]

    out.write(image)

    StopIteration(0.5)

    if keyboard.is_pressed('esc'):
        print('Exit')
        break


out.release()
cv2.destroyAllWindows()

