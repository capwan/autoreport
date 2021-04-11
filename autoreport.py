import time
import pyautogui
from datetime import date

pyautogui.PAUSE = 2
pyautogui.FAILSAFE = False

xread = open("x.txt", "r+")
x = int(xread.read())

yread = open("y.txt", "r+")
y = int(yread.read())

today = date.today()
fdate = date.today().strftime('%d')
dayofweek = date.today().strftime('%d,%A') 

if dayofweek == "Saturday":
    y = y + 15
    x = x - 22 * 6

pyautogui.moveTo(120, 875, duration=2)
pyautogui.click(120, 875)

pyautogui.moveTo(150, 79, duration=2)
pyautogui.click(150, 79)

pyautogui.moveTo(406, 62, duration=2)
pyautogui.click(406, 62)

# first date
pyautogui.moveTo(x, y, duration=2)
pyautogui.click(x, y)

pyautogui.moveTo(408, 88, duration=2)
pyautogui.click(408, 88)

# last date
pyautogui.moveTo(x,y+20, duration=2)
pyautogui.click(x,y+20)

# print(today)
print(fdate)
print(dayofweek)

if dayofweek != "Saturday":
    x = x + 22

xwrite = open("x.txt", "w")
xwrite.write(str(x))

ywrite = open("y.txt", "w")
ywrite.write(str(y))

