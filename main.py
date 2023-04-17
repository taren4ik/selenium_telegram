import os
from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv

URL = "https://web.telegram.org/k/"
CHANEL = "t.me/ERAanarchy/"

posts = (
    606,
    607,
    610
)

load_dotenv()

PHONE = os.getenv('PHONE')
PASSWORD = os.getenv('PASSWORD')


def authorization():
    """Прохождение авторизации."""
    button = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div/div[2]/div[3]/div/div[2]/button[1]/div"
    )
    button.click()

    phone = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]"
    )
    phone.send_keys(PHONE)
    sleep(3)

    next = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div/div[2]/div[2]/div/div[3]/button[1]"
    )
    next.click()
    sleep(5)

    password = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div/div[2]/div[5]/div/div[2]/div/input[2]"
    )
    sleep(5)
    password.send_keys(PASSWORD)

    pwd_next = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div/div[2]/div[5]/div/div[2]/button/div"
    )
    sleep(3)
    pwd_next.click()
    sleep(3)


def get_screenshot():
    "Скриншоты постов."
    for post in posts:
        driver.get(CHANEL + str(post) + '/')
        sleep(5)
        driver.save_screenshot(f'screenshot_+{post}.png')


if __name__ == '__main__':
    mobile = {'deviceName': 'iPhone 6 Plus'}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--allow-profiles-outside-user-dir')
    chrome_options.add_argument('--enable-profile-shortcut-manager')
    chrome_options.add_argument(
        r'user-data-dir=D:\developer\selenium_telegram')
    chrome_options.add_argument('--profile-directory=Profile 1')
    # chrome_options.add_experimental_option('mobileEmulation', mobile)
    driver = webdriver.Chrome(
        options=chrome_options
    )
    driver.get(URL)
    driver.implicitly_wait(20)
    authorization()
    get_screenshot()
    driver.quit()
