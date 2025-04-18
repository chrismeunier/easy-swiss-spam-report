from selenium.webdriver.remote.webdriver import WebDriver  # for type hints
from selenium.webdriver.common.by import By
from datetime import datetime
import locale
from constants import *
from selenium_form_filling_tools import start_at_url, fill_from_dict


def fill_personal_info(driver: WebDriver):
    fill_from_dict(driver, PERSONAL_DATA_SECO)


def check_radio_buttons(driver: WebDriver, answered=Answer.NO, healthcare=Answer.DNK):
    #  say no/yes to number in phonebook
    xpath = XPATH_BTN_PHONEBOOK if NUMBER_IN_PHONEBOOK else XPATH_BTN_NOT_PHONEBOOK
    driver.find_element(By.XPATH, xpath).click()

    # say no/yes to phone call answered
    xpath = XPATH_BTN_ANSWERED if answered is Answer.YES else XPATH_BTN_NOT_ANSWERED
    driver.find_element(By.XPATH, xpath).click()

    # healthcare insurance question
    xpath = (
        XPATH_BTN_HEALTH_DNK
        if healthcare is Answer.DNK
        else (XPATH_BTN_HEALTH_YES if healthcare is Answer.YES else XPATH_BTN_HEALTH_NO)
    )
    driver.find_element(By.XPATH, xpath).click()

    # Authorize SECO to prosecute the caller
    driver.find_element(By.XPATH, XPATH_BTN_AUTHORIZE).click()


def fill_spam_info(driver: WebDriver, spam_number: str):
    driver.find_element(By.NAME, "ANRUFENDE_TELEFONNUMMER").send_keys(spam_number)
    # Write the current date and time
    locale.setlocale(locale.LC_TIME, "fr_FR.utf8")
    element = driver.find_element(By.NAME, "DATUM_UHRZEIT_DES_ANRUFS")
    element.send_keys(datetime.now().strftime("%A %d %B %Y %Hh%M"))


def solve_captcha(driver: WebDriver):
    element = driver.find_element(By.XPATH, XPATH_EQUATION)
    equation = element.text.split("\n")[0]
    answer = solve_text_equation(equation)
    driver.find_element(By.NAME, ":cq:captcha:captcha").send_keys(answer)


def send_form(driver: WebDriver):
    send_button = driver.find_element(By.XPATH, XPATH_BTN_SEND)
    send_button.click()  # going to the next page!


def solve_text_equation(equation: str) -> str:
    listed_elements = equation.split()  # cut at spaces
    x = listed_elements[0]
    y = listed_elements[2]
    op = listed_elements[1]
    z = ""
    match op:
        case "+":
            z = int(x) + int(y)
        case "-":
            z = int(x) - int(y)
        case "*":
            z = int(x) * int(y)
        # no division I guess?
        case _:
            print(
                "Not implemented error :-( the division is not supported to solve the captcha."
            )

    return str(z)


# def fill_form_with_constants(): #! FOR INITIAL TESTS
#     driver = start_at_url(URL_SECO)
#     # Check we got the correct page loaded properly
#     assert VALIDATION_SECO in driver.title

#     fill_personal_info(driver)
#     check_radio_buttons(driver)
#     fill_spam_info(driver, "000 000 00 00")
#     solve_captcha(driver)
#     send_form(driver)

#     # Check we landed at the right place
#     assert VALIDATION_SECO in driver.find_element(By.XPATH, XPATH_SUCCESS_TEXT).text


def fill_form_from_inputs(phone_number: str, answered: Answer, healthcare: Answer):
    driver = start_at_url(URL_SECO, hide_browser=False)
    # Check we got the correct page loaded properly
    assert VALIDATION_SECO in driver.title

    fill_personal_info(driver)
    check_radio_buttons(driver, answered, healthcare)
    fill_spam_info(driver, phone_number)
    solve_captcha(driver)
    send_form(driver)

    # Check we landed at the right place
    assert VALIDATION_SECO in driver.find_element(By.XPATH, XPATH_SUCCESS_TEXT).text

    driver.close()


if __name__ == "__main__":
    # fill_form_with_constants()
    fill_form_from_inputs("032 711 85 37", Answer.NO, Answer.DNK)
    pass
