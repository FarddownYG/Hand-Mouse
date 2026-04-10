# LANGAGE: Python

import cv2
import threading

class Camera:
    def __init__(self, w=640, h=480):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, w)
        self.cap.set(4, h)

        self.frame = None
        self.running = True

        self.thread = threading.Thread(target=self.update)
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.frame = frame

    def read(self):
        return self.frame

    def release(self):
        self.running = False
        self.cap.release()