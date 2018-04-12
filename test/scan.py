import colorsys
import time

from blinkt import set_brightness, set_pixel, show

spacing = 360.0 / 16.0
hue = 0

set_brightness(0.1)

while True:
    hue = int(time.time() * 100) % 360
    for x in range(8):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        set_pixel(x, r, g, b)
    show()
    time.sleep(0.001)
