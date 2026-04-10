# LANGAGE: Python

import cv2
from camera_thread import Camera
from core.hand_tracker import HandTracker
from core.gesture_detector import GestureDetector
from core.mouse_controller import MouseController
from core.scroll_controller import ScrollController
from ui.tray import Tray

camera = Camera()
tracker = HandTracker()
gesture = GestureDetector()
mouse = MouseController()
scroll = ScrollController()

running = True
scrolling = False

def stop():
    global running
    running = False

tray = Tray(stop)

import threading
threading.Thread(target=tray.run, daemon=True).start()

while running:

    frame = camera.read()
    if frame is None:
        continue

    frame = cv2.flip(frame, 1)

    results = tracker.process(frame)

    if results.multi_hand_landmarks:

        lm = results.multi_hand_landmarks[0].landmark

        # MOVE
        x, y = lm[8].x, lm[8].y
        sx, sy = mouse.map(x, y)
        mouse.move(sx, sy)

        # GESTURE
        action = gesture.detect(lm)

        if action == "left_down":
            mouse.left_down()

        elif action == "left_up":
            mouse.left_up()

        elif action == "right_click":
            mouse.right_click()

        elif action == "scroll_start":
            scrolling = True
            scroll.start(lm[8].y)

        elif action == "scroll_end":
            scrolling = False
            scroll.stop()

        if scrolling:
            scroll.update(lm[8].y)

    cv2.imshow("Hand Mouse FINAL", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()