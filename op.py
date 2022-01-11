import pyautogui  ,time
time.sleep(1)




with open("text.txt","r") as tulisan:
    for text in tulisan:
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        repeats = "enter" * 1
        time.sleep(3)


        