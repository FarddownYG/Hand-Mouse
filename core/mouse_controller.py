# LANGAGE: Python

import pyautogui
from config import SMOOTHING, SCREEN_MARGIN

pyautogui.FAILSAFE = False

class MouseController:
    def __init__(self):
        self.w, self.h = pyautogui.size()
        self.px = None
        self.py = None
        self.down = False

    def map(self, x, y):
        x = max(0, min(1, (x - SCREEN_MARGIN) / (1 - 2 * SCREEN_MARGIN)))
        y = max(0, min(1, (y - SCREEN_MARGIN) / (1 - 2 * SCREEN_MARGIN)))
        return x * self.w, y * self.h

    def smooth(self, x, y):
        if self.px is None:
            self.px, self.py = x, y

        x = self.px + (x - self.px) * SMOOTHING
        y = self.py + (y - self.py) * SMOOTHING

        self.px, self.py = x, y
        return x, y

    def move(self, x, y):
        x, y = self.smooth(x, y)
        pyautogui.moveTo(x, y)

    def left_down(self):
        if not self.down:
            pyautogui.mouseDown()
            self.down = True

    def left_up(self):
        if self.down:
            pyautogui.mouseUp()
            self.down = False

    def right_click(self):
        pyautogui.click(button="right")