import pyautogui, os, sys, time

os.chdir(os.path.dirname(sys.argv[0]))

sleep_timer = 0
click_counter = 0

print("Starting search...")

while True:

    # prevent screen turn-off every 300 seconds
    if sleep_timer == 300:
        sleep_timer = 0
        pyautogui.press('volumedown')
        pyautogui.press('volumeup')
    
    # search for Yes button to continue watching
    button_location = pyautogui.locateCenterOnScreen('button.png', confidence= 0.9)

    if button_location is not None:
        pyautogui.moveTo(button_location)
        pyautogui.click()
        # move mouse a bit to not interfere with future searches
        pyautogui.move(-100, -100)

        # print out click count
        click_counter += 1
        print(f"Counted {click_counter} clicks. Sleeping...")

        # sleep for a bit
        time.sleep(30)
    
    sleep_timer += 1
    time.sleep(1)
        



    