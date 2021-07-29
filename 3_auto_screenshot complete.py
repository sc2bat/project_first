# advanced_screenshot
# 터미널 pip install keyboard

import time
import keyboard
from PIL import ImageGrab
def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("imgae{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot) # F9 누르면 스크린샷 저장

keyboard.wait("esc") # 유저가 esc 누르때까지 프로그램 수행