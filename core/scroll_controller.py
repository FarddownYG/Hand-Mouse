# LANGAGE: Python

import pyautogui

class ScrollController:
    def __init__(self):
        self.prev_y = None
        self.active = False

    def start(self, y):
        self.active = True
        self.prev_y = y

    def stop(self):
        self.active = False
        self.prev_y = None

    def update(self, y):
        if not self.active:
            return

        if self.prev_y is None:
            self.prev_y = y
            return

        dy = self.prev_y - y

        # 🔥 sensibilité scroll (augmente si besoin)
        amount = int(dy * 80)

        if abs(amount) > 1:
            pyautogui.scroll(amount)

        self.prev_y = y