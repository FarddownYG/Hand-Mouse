# LANGAGE: Python

import pystray
from PIL import Image

class Tray:
    def __init__(self, stop_callback):
        self.stop_callback = stop_callback

    def run(self):
        image = Image.new('RGB', (64, 64), (0, 0, 0))

        menu = pystray.Menu(
            pystray.MenuItem("Quit", self.exit_app)
        )

        self.icon = pystray.Icon("HandMouse", image, "Hand Mouse", menu)
        self.icon.run()

    def exit_app(self, icon, item):
        self.stop_callback()
        icon.stop()
