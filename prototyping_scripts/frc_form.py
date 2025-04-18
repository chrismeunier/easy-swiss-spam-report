from selenium.webdriver.remote.webdriver import WebDriver  # for type hints
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from constants import *
from selenium_form_filling_tools import start_at_url, fill_from_dict


def fill_form(
    phone_number: str, hide_browser=False, optional_inputs=[False] * len(FRC_OPTIONAL)
) -> WebDriver:
    print("Starting web driver...")
    driver = start_at_url(URL_FRC, hide_browser)
    assert VALIDATION_FRC in driver.title
    print("Website loaded")

    close_cookie_panel(driver)

    # Click first the spam calls radio button
    driver.find_element(By.ID, SPAM_TYPE).click()

    # Fill personal data
    fill_from_dict(driver, PERSONAL_DATA_FRC)
    fill_spam_phone_number(driver, phone_number)

    other_buttons_to_click = complete_optional_buttons(optional_inputs)
    click_buttons_listed(driver, other_buttons_to_click)
    print("Form filled")

    send_form(driver)

    validate_form_received(driver)


    return driver


def close_cookie_panel(driver: WebDriver):
    try:
        WebDriverWait(driver, 2)
        driver.find_element(By.ID, CLOSE_COOKIE).click()
    except NoSuchElementException as err:
        print("No cookie panel found, continuing...")
        return
    try:
        wait = WebDriverWait(driver, 5)
        wait.until_not(EC.element_to_be_clickable((By.ID, CLOSE_COOKIE)))
    except TimeoutException as err:
        print("Timeout!", err)


def fill_spam_phone_number(driver: WebDriver, number: str):
    driver.find_element(By.NAME, SPAM_INPUT).send_keys(number)


def complete_optional_buttons(optional_inputs: list[bool]):
    button_list_ids = FRC_ID_TO_CLICK
    assert len(optional_inputs) == len(FRC_OPTIONAL)
    for option_selected, optional_id in zip(optional_inputs, FRC_OPTIONAL.values()):
        if option_selected:
            button_list_ids.append(optional_id)
    return button_list_ids


def click_buttons_listed(driver: WebDriver, button_list_ids: list[str]):
    for ID in button_list_ids:
        driver.find_element(By.ID, ID).click()


def send_form(driver: WebDriver):
    driver.find_element(By.ID, ID_BTN_SEND).click()

def validate_form_received(driver: WebDriver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains(VALIDATION_FRC_SENT))
    except TimeoutException as err:
        print("Timeout!", err)
    finally:
        print("Form sent successfully!")

if __name__ == "__main__":
    fill_form(
        phone_number="032 711 85 37",
        hide_browser=False,
        optional_inputs=[True, False, False, False, False, False, True, True],
    ).quit()
    pass
