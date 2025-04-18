from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver  # for type hints
from selenium.webdriver.common.by import By

def start_headless_driver() -> WebDriver:
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    return webdriver.Firefox(options=options)

def start_at_url(url: str, hide_browser=True) -> WebDriver:
    options = webdriver.FirefoxOptions()
    if hide_browser:
        options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    return driver

def fill_from_dict(driver: WebDriver, dictionary: dict, by=By.NAME):
    for key, value in dictionary.items():
        elem = driver.find_element(by, key)
        elem.send_keys(value)
