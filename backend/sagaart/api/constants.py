FEEDBACK_MESSAGE_MAX_LEN = 3000

DEFAULT_CHARFIELD_LEN = 128

ARTOBJECTS_APP_LABEL = "artobjects"

FEEDBACK_EMAIL_ADRESS = "example@sagaart.com"

GENDER_LIST = ((1, "Male"), (2, "Female"))

SIZE_CATEGORIES = (
    (1, "Любой"),
    (2, "Small (до 40 см)"),
    (3, "Medium (40 - 100 см)"),
    (4, "Large (100 - 160 см)"),
    (5, "Oversize (более 160 см)"),
)

PRICE_CATEGORIES = (
    (1, "до 20 000 руб."),
    (2, "от 20 000 до 50 000 руб."),
    (3, "50 000 до 100 000 руб."),
    (4, "от 100 000 до 200 000 руб."),
    (5, "от 200 000 до 500 000 руб."),
)

TELEPHONE_VALIDATE = "^(\+|\d)?[\d]{9,15}$"
PASSWORD_VALIDATE = "^[A-Za-z0-9@#$%^&+=]{8,25}$"
USERNAME_VALIDATE = "^[^\s][A-z0-9А-я -]{2,150}$"

MAX_LENGHT_EMAIL = 250
MIN_LENGHT_EMAIL = 8
MAX_LENGHT_USER_NAME = 150
MIN_LENGHT_USER_NAME = 2
MAX_LENGHT_TELEPHONE = 15
MIN_LENGHT_TELEPHONE = 11
