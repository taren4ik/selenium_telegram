from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

URL = "https://web.telegram.org/k/"


def authorization():
    "Прохождение авторизации."
    driver.find_element
    button = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div/div[2]/div[3]/div/div[2]/button[1]/div"
    )
    button.click()
    phone = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]"
    )
    phone.send_keys("79990591101")
    sleep(3)
    next = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div/div[2]/div[2]/div/div[3]/button[1]/div"
    )
    next.click()
    sleep(3)


def get_post():
    sleep(3)


if __name__ == '__main__':
    mobile = {'deviceName': 'iPhone 6 Plus'}
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option('mobileEmulation', mobile)
    driver = webdriver.Chrome(
        options=chrome_options
    )
    driver.get(URL)
    driver.implicitly_wait(15)
    authorization()
    get_post()
    driver.quit()
