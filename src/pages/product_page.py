from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    def wait_for_page_load(self, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete',
            message="Страница ещё не загрузилась полностью" )
        element = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(ProductPageLocators.PRODUCT_IMG)
        )
        assert element is not None, "Картинка товара не появилась в DOM за отведённое время"

    def product_add_to_basket(self):
        # Проверяем, что кнопка есть на странице
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not present on the page"
        # Ждём, пока кнопка станет кликабельной и сохраняем её
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)
        )
        button.click()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            assert alert_text, "Expected alert text but got empty"
        except NoAlertPresentException:
            pass

    def validate_product_name_in_alert(self):
        product_name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE).text
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text
        assert product_name_on_page == product_name_in_alert, (
            f"Product name mismatch: '{product_name_on_page}' != '{product_name_in_alert}'"
        )

    def validate_cost_in_alert(self):
        product_cost_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_ON_PAGE).text
        product_cost_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_IN_ALERT).text
        assert product_cost_on_page == product_cost_in_alert, (
            f"Product name mismatch: '{product_cost_on_page}' != '{product_cost_in_alert}'"
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_ALERT), \
            "PRODUCT_NAME_IN_ALERT mismatch"

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_ALERT), \
            "PRODUCT_NAME_IN_ALERT mismatch"

