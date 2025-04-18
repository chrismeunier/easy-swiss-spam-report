from enum import Enum
class Answer(Enum):
    NO = 0
    YES = 1
    DNK = 2

from secrets import FIRST_NAME, LAST_NAME, STREET, ZIP, CITY, CANTON, EMAIL, OPERATOR, PHONE, NUMBER_IN_PHONEBOOK

LASTNAME_FIRSTNAME = " ".join([LAST_NAME, FIRST_NAME])
ZIP_CITY = " ".join([ZIP, CITY])

# SECO specific data
URL_SECO = "https://www.seco.admin.ch/seco/fr/home/Werbe_Geschaeftsmethoden/Unlauterer_Wettbewerb/Beschwerde_melden/beschwerde_werbeanruf.html"
VALIDATION_SECO = "appels publicitaires"
PERSONAL_DATA_SECO = {
    "NAME_VORNAME": LASTNAME_FIRSTNAME,
    "STRASSE": STREET,
    "PLZ_ORT": ZIP_CITY,
    "KANTON": CANTON,
    "MEINE_EMAIL": EMAIL,
    "MEINE_FDA": OPERATOR,
    "MEINE_TELEFONNUMMER": PHONE,
}
ANSWERED_CALL = Answer.NO
HEALTHCARE = Answer.DNK

# XPATHS_SECO
XPATH_BTN_PHONEBOOK = "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[8]/form/div/div[13]/div/div[2]/div[4]/label"
XPATH_BTN_NOT_PHONEBOOK = "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[8]/form/div/div[13]/div/div[2]/div[2]/label"
XPATH_BTN_ANSWERED = "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[8]/form/div/div[19]/div/div[2]/div[2]/label"
XPATH_BTN_NOT_ANSWERED = "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[8]/form/div/div[19]/div/div[2]/div[4]/label"
XPATH_BTN_HEALTH_YES = "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[8]/form/div/div[20]/div/div[2]/div[2]/label"
XPATH_BTN_HEALTH_NO = "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[8]/form/div/div[20]/div/div[2]/div[4]/label"
XPATH_BTN_HEALTH_DNK = "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[8]/form/div/div[20]/div/div[2]/div[6]/label"
XPATH_BTN_AUTHORIZE = "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[8]/form/div/div[22]/div/div[2]/div[2]/label"
XPATH_EQUATION = "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[8]/form/div/div[24]"
XPATH_BTN_SEND = "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[8]/form/div/div[25]/div[1]/input"
XPATH_SUCCESS_TEXT = "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/article/p[2]"

# FRC specific data
URL_FRC = "https://www.frc.ch/denoncez-les-pratiques-deloyales/"
VALIDATION_FRC = "Fédération romande des consommateurs"
VALIDATION_FRC_SENT = "Formulaire"
PERSONAL_DATA_FRC = {
    "input_12": FIRST_NAME,
    "input_59": LAST_NAME,
    "input_13": STREET,
    "input_14": ZIP,
    "input_60": CITY,
    "input_8": EMAIL,
    "input_15": PHONE,
    "input_71": PHONE,
    "input_73": OPERATOR,
}
CLOSE_COOKIE = "cn-close-notice"
SPAM_TYPE = "choice_2_9_1"
SPAM_INPUT = "input_21"
FRC_ID_TO_CLICK = ["choice_2_74_1", "choice_2_61_1", "choice_2_69_1"]
ID_BTN_SEND = "gform_submit_button_2"
# Optional buttons to select
FRC_OPTIONAL = {
    "USES_ANTI_SPAM" : "choice_2_74_0",
    "IS_FRC_MEMBER" : "choice_2_61_0",
    "IS_CLIENT" : "choice_2_25_0",
    "HAS_STAR" : "choice_2_28_0",
    "ANSWERED_SURVEY" : "choice_2_33_0",
    "LOST_MONEY" : "choice_2_53_0",
    "KNOWS_ANTI_SPAM" : "choice_2_76_0",
    "ANTI_SPAM_ACTIVE" : "choice_2_77_0",
}
