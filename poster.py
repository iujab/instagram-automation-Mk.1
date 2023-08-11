import main
import pyautogui
import time
import os
import pyperclip

if main.account == "ACCOUNT" or main.account == "CONFIGURE MULTIPLE ACCOUNTS":
    pyperclip.copy("INSERT POST DESCRIPTION")

adOffset = 0
path = main.directory + r"\\"
dirs = os.listdir(path)


def removeLatest():
    dirs = os.listdir(path)
    for item in dirs[:1]:
        print(item)
        os.remove(path + item)


def moveAndClick(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click(x, y)
    time.sleep(1)


def slideAD():
    global adOffset
    adOffset = 60
    moveAndClick(111, 420)  # media button
    moveAndClick(111, 450)  # media button
    moveAndClick(481, 78)  # directory
    pyautogui.typewrite(r"C:\INSERT DIRECTORY\""[:-1] + "ad") # Separate folder that holds ad slide
    time.sleep(0.25)
    pyautogui.press('enter')
    time.sleep(0.25)
    moveAndClick(332, 241)  # item
    moveAndClick(675, 737)  # open button
    time.sleep(2.5)


"""START"""
row = 0
col = 0

moveAndClick(1742, 13)  # close pycharm

for i in range(main.days):
    time.sleep(1)

    """PLANNER PAGE"""
    moveAndClick(1817, 179)  # create button

    """ADD CONTENT"""
    moveAndClick(111, 378)  # media button
    moveAndClick(111, 420)  # media button

    """FILE EXPLORER"""
    moveAndClick(481, 78)  # directory
    pyautogui.typewrite(main.directory)
    time.sleep(0.25)
    pyautogui.press('enter')
    time.sleep(0.25)
    moveAndClick(332, 241)  # item
    moveAndClick(675, 737)  # open button
    time.sleep(2.5)

    """SLIDE AD"""
    if main.ad:
        slideAD()  # OPTIONAL SECOND SLIDE

    """EDIT POST"""
    moveAndClick(256, 550 + adOffset)  # text
    pyautogui.hotkey("ctrl", "v")  # write caption

    moveAndClick(384, 821 + adOffset)  # schedule button
    pyautogui.scroll(-15)
    pyautogui.scroll(-15)
    pyautogui.scroll(-15)
    moveAndClick(201, 864)  # date
    pyautogui.hotkey("ctrl", "a")
    for k in range(10):
        pyautogui.press("backspace")
    pyautogui.typewrite(str(main.month) + "/" + str(main.startDay + i) + "/" + str(main.year))
    moveAndClick(319, 863)
    pyautogui.typewrite(main.hour)
    moveAndClick(334, 863)
    pyautogui.typewrite("0")
    moveAndClick(351, 863)
    pyautogui.typewrite(main.ampm)

    moveAndClick(477, 966)  # post button
    time.sleep(7.5)
    removeLatest()
