import pyautogui, os, sys, time

os.chdir(os.path.dirname(sys.argv[0]))

sleep_timer = 0
click_counter = 0

while True:

    if sleep_timer == 300:
        sleep_timer = 0
        pyautogui.press('volumedown')
        pyautogui.press('volumeup')
        
    button_location = pyautogui.locateCenterOnScreen('button.png', confidence= 0.9)

    if button_location is None:
        print("None detected.")

    else:
        pyautogui.moveTo(button_location)
        pyautogui.click()
        pyautogui.move(-100, -100)

        click_counter += 1
        print(f"Counted {click_counter} clicks. Sleeping...")

        time.sleep(30)
    
    sleep_timer += 1
    time.sleep(1)
        



    