# Sell RSA stocks from Schwab

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
# loads the trading ticket
sleep(5)
press('tab', presses=8)
press('space')
sleep(1)
press('down', presses=2)
press('tab')
sleep(1)
press('tab', presses=7)
press('space')
press('up')
press('tab')
sleep(1)
press('tab', presses=6)
sleep(1)
press('space')
sleep(2)
press('tab', presses=3)
sleep(1)
press('space')
""""
press('tab', presses=3)
press('space')
"""

# From the chase sell program
"""press('space')
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
    press('tab', presses=4)"""