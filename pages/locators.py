from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_URL = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_ALERT = (By.XPATH, "//strong[text()='Coders at Work']")
    PRODUCT_COST_ON_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_COST_IN_ALERT = (By.XPATH, "//strong[text()='£19.99']")
    PRODUCT_IMG = (By.CSS_SELECTOR, ".item img")

