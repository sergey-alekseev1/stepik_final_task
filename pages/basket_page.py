from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException
import time
import math
from selenium.webdriver.support.ui import WebDriverWait

class BasketPage(BasePage):
	def check_message_about_basket_empty(self):
		assert self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_EMPTY), \
			"MESSAGE_BASKET_EMPTY mismatch"

	def check_basket_has_no_items(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
			"BASKET_ITEMS not empty"
