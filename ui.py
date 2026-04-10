# LANGAGE: Python

import cv2

class UI:
    def __init__(self):
        self.hand = "Right"
        self.status = "None"

    def update_status(self, status):
        if status:
            self.status = status

    def draw(self, frame):
        cv2.putText(frame, f"Hand: {self.hand}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        cv2.putText(frame, f"Action: {self.status}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

    def handle_key(self, key):
        if key == ord('l'):
            self.hand = "Left"
        elif key == ord('r'):
            self.hand = "Right"