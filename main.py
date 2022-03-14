from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pynput.keyboard import Controller
from random import randint
import undetected_chromedriver as uc
import time


def fast_type(velocity):
    time.sleep(3)
    words = driver.find_element(By.CSS_SELECTOR, '.dash-copy').text
    for letter in words:
        time.sleep(0.0055)
        if letter == '&nbsp':
            keyboard.type(' ')
            time.sleep(0.0001)
        else:
            keyboard.type(letter)
            print(letter)
            time.sleep(velocity)


def natural_type():
    natural_times = [0.01, 0.011, 0.012, 0.013, 0.014, 0.015, 0.019, 0.06, 0.08, 0.09, 0.1]
    max_index = len(natural_times) - 1
    time.sleep(2)
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
            time.sleep(natural_times[random_index])


if __name__ == '__main__':
    keyboard = Controller()
    fast_time = 0.005

    # Setting the path to the Chrome webdriver.
    PATH = Service('C:\\webdrivers\\chromedriver.exe')
    driver = uc.Chrome(service=PATH)

    # Opening the driver and maximizing window.
    driver.get("https://www.nitrotype.com")
    driver.maximize_window()

    while True:
        option = input('[F]ast | [N]atural | [Q]uit \n ')
        if option.upper() == 'N':
            natural_type()

        elif option.upper() == 'F':
            fast_type(fast_time)

        elif option.upper() == 'Q':
            break

    # Time to see the WPM
    time.sleep(6)
    quit()
