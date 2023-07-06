import pyautogui
import time

from pyautogui import write, press
from time import sleep

# from the trade stocks and etf page

# in the stock and etf symbol look up
sleep(3)
#write("TLIS")
write("KPG:")
press('tab')
sleep(5)
press('tab', presses=3)
press('right', presses=2)
press('space')
press('tab')
press('space')
press('tab', presses=2)
press('space')
press('tab', presses=4)
press('space')
sleep(2)
press('tab', presses=4)
press('space')
sleep(2)
press('tab', presses=2)
press('space')
sleep(3)
with pyautogui.hold('shift'):
    press('tab', presses=4)