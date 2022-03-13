from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pynput.keyboard import Controller
from random import randint
import time

keyboard = Controller()
temp_word = '1'
natural_type = [0.01, 0.011, 0.012, 0.013, 0.014, 0.015, 0.019, 0.06, 0.08, 0.09, 0.1]
fast_type = 0.005
max_index = len(natural_type) - 1

# Setting the path to the Firefox webdriver.
PATH = Service('C:\\webdrivers\\geckodriver.exe')
driver = webdriver.Firefox(service=PATH)

# Opening the driver and maximizing window.
driver.get("https://www.nitrotype.com/race")
driver.maximize_window()

option = input('[F]ast | [N]atural | [Q]uit \n ')

# Fast typing

if option.upper() == 'F':
    time.sleep(3)
    words = driver.find_element(By.CSS_SELECTOR, '.dash-copy').text
    for letter in words:
        time.sleep(0.0055)
        if letter == '&nbsp':
            keyboard.type(' ')
            time.sleep(0.0001)
        elif letter == temp_word:
            pass
        else:
            keyboard.type(letter)
            print(letter)
            time.sleep(fast_type)

        temp_word = letter

# Natural typing
elif option.upper() == 'N':
    time.sleep(3)
    words = driver.find_element(By.CSS_SELECTOR, '.dash-copy').text
    for letter in words:
        time.sleep(0.0035)
        if letter == '&nbsp':
            keyboard.type(' ')
            time.sleep(0.0001)
        else:
            keyboard.type(letter)
            random_index = randint(0, max_index)
            print(letter)
            time.sleep(natural_type[random_index])

        temp_word = letter

elif option.upper() == 'Q':
    quit()


# Time to see the WPM
time.sleep(6)
driver.close()
