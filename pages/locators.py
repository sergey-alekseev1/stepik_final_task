from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    LOGIN_URL = 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators():
    PRODUCT_URL = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_ALERT = (By.XPATH, "//strong[text()='Coders at Work']")
    PRODUCT_COST_ON_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_COST_IN_ALERT = (By.XPATH, "//strong[text()='£19.99']")
    PRODUCT_IMG = (By.CSS_SELECTOR, ".item img")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    HEADER_VIEW_BASKET = (By.XPATH, '//*[contains(@class, "btn-default") and normalize-space(text()) = "View basket"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_BASKET_EMPTY = (By.XPATH, '//p[contains(text(), "Your basket is empty.")]')

