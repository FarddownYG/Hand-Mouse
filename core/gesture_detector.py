# LANGAGE: Python

from utils import distance

class GestureDetector:
    def __init__(self):
        self.left_down = False
        self.right = False
        self.fist = False

    def detect(self, lm):

        thumb = lm[4]
        index = lm[8]
        pinky = lm[20]
        wrist = lm[0]
        middle = lm[12]

        pinch = distance(thumb, index)
        right = distance(thumb, pinky)

        fist = (
            distance(index, wrist) < 0.1 and
            distance(middle, wrist) < 0.1 and
            distance(pinky, wrist) < 0.1
        )

        action = None

        # ✊ SCROLL MODE
        if fist:
            if not self.fist:
                action = "scroll_start"
            self.fist = True
        else:
            if self.fist:
                action = "scroll_end"
            self.fist = False

        # 🖱️ DRAG
        if not fist:
            if pinch < 0.035:
                if not self.left_down:
                    action = "left_down"
                    self.left_down = True
            elif pinch > 0.06:
                if self.left_down:
                    action = "left_up"
                    self.left_down = False

        # 🖱️ RIGHT CLICK
        if not fist and right < 0.035:
            action = "right_click"

        return action