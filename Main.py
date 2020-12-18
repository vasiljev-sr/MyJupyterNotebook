import time
from datetime import datetime

import pyautogui

path = '/home/MARBUM/log-kip-cik/Pic/'
while True:
    image = pyautogui.screenshot(path + str(datetime.now()) + '.png')
    time.sleep(60)