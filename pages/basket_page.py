from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasketPage(BasePage):
	def should_be_basket_url(self):
		assert "basket" in self.browser.current_url, "Current page is not basket page"

	def should_be_empty_basket_message(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "'Empty basket' message is not presented"

	def should_not_be_empty_basket_message(self):
		assert self.is_not_element_present(*BasketPageLocators.EMPTY_MESSAGE), "'Empty basket' is presented, but should not be"

	def should_not_be_items_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY_TITLE), "Basket is not empty"