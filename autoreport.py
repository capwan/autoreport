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
dayofweek = date.today().strftime('%d,%A')

spreadsheetname = date.today().strftime('%d.%m.%y')
 

if dayofweek == "Saturday":
    y = y + 15
    x = x - 22 * 6

pyautogui.moveTo(70, 1062, duration=2)
pyautogui.click(70, 1062)

pyautogui.moveTo(150, 79, duration=2)
pyautogui.click(150, 79)

pyautogui.moveTo(406, 62, duration=2)
pyautogui.click(406, 62)

# first date
pyautogui.moveTo(x, y, duration=2)
pyautogui.click(x, y)

pyautogui.moveTo(408, 88, duration=2)
pyautogui.click(408, 88)

# second date
pyautogui.moveTo(x,y+20, duration=2)
pyautogui.click(x,y+20)

# Calculate button
pyautogui.moveTo(480, 50, duration=2)
pyautogui.click(480, 50)

# Clock IN/Out log button
pyautogui.moveTo(79, 136, duration=2)
pyautogui.click(79, 136)

pyautogui.moveTo(292, 158, duration=2)
pyautogui.rightClick(292,158)

# Columns button
pyautogui.moveTo(516, 265, duration=2)
pyautogui.click(516,265)

# Department add
pyautogui.moveTo(656,467, duration=2)
pyautogui.click(656,467)

# Empty field
pyautogui.moveTo(324,474, duration=2)
pyautogui.click(324,474)

pyautogui.moveTo(295, 160, duration=2)
pyautogui.rightClick(295,160)

pyautogui.moveTo(531, 269, duration=2)
pyautogui.click(531, 269)

# Take "No" column
pyautogui.moveTo(684, 312, duration=2)
pyautogui.click(684,312)

# Empty field
pyautogui.moveTo(324,474, duration=2)
pyautogui.click(324,474)

pyautogui.moveTo(295, 160, duration=2)
pyautogui.rightClick(295,160)

pyautogui.moveTo(531, 269, duration=2)
pyautogui.click(531, 269)

# Take "New State" column
pyautogui.moveTo(662, 402, duration=2)
pyautogui.click(662,402)

# Empty field
pyautogui.moveTo(324,474, duration=2)
pyautogui.click(324,474)

pyautogui.moveTo(295, 160, duration=2)
pyautogui.rightClick(295,160)

pyautogui.moveTo(531, 269, duration=2)
pyautogui.click(531, 269)

# Take "Exception" column
pyautogui.moveTo(623,418, duration=2)
pyautogui.click(623,418)

# Empty field
pyautogui.moveTo(324,474, duration=2)
pyautogui.click(324,474)

pyautogui.moveTo(295, 160, duration=2)
pyautogui.rightClick(295,160)

pyautogui.moveTo(531, 269, duration=2)
pyautogui.click(531, 269)

# Take "Operation" column
pyautogui.moveTo(622,444, duration=2)
pyautogui.click(622,444)

# Export data button
pyautogui.moveTo(566,74, duration=2)
pyautogui.click(566,74)

# "OK" button in Export data
pyautogui.moveTo(853,583, duration=2)
pyautogui.click(853,583)

pyautogui.moveTo(738,526, duration=2)
pyautogui.click(738,526)
# Write Today's Date in the name of Excel Spreadsheet
pyautogui.typewrite(spreadsheetname)
pyautogui.press("space")
pyautogui.typewrite("report")

# Save Excel Spreadsheet
pyautogui.moveTo(1035,530, duration=2)
pyautogui.click(1035,530)

# Press "OK" [Confirmation]
pyautogui.moveTo(928,504, duration=2)
pyautogui.click(928,504)


if dayofweek != "Saturday":
    x = x + 22

xwrite = open("x.txt", "w")
xwrite.write(str(x))

ywrite = open("y.txt", "w")
ywrite.write(str(y))


