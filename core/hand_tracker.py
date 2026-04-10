# LANGAGE: Python

import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.mp = mp.solutions.hands
        self.hands = self.mp.Hands(
            max_num_hands=1,
            model_complexity=0,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb)