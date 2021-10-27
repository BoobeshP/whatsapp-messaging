import pyautogui,time,datetime,emoji
time.sleep(3)
msg = 'hi'


def message(msg):
    while True:
       print(datetime.datetime.now())
       pyautogui.typewrite(msg)
       pyautogui.press("enter")
       time.sleep(5)
message(msg)