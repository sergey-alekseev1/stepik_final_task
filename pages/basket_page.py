from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	def check_message_about_basket_empty(self):
		assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), \
			"MESSAGE_BASKET_EMPTY mismatch"

	def check_basket_has_no_items(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
			"BASKET_ITEMS not empty"
