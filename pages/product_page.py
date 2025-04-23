from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
	def click_on_add_to_basket_button(self):
		add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
		add_button.click()

		# Ждём alert, и если он появляется — решаем задачу
		try:
			WebDriverWait(self.browser, 3).until(EC.alert_is_present())
			self.solve_quiz_and_get_code()
		except TimeoutException:
			print("Alert did not appear, skipping quiz solving")

	def get_product_name(self):
		return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

	def get_product_price(self):
		return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

	def should_be_basket_total_message(self, product_price):
		assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "'Basket total' message is not presented"
		assert product_price == self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text, "Basket total does not match the book price"

	def should_be_success_message(self, product_name):
		assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "'Added to basket' message is not presented"
		assert product_name == self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, "Book titles don't match"

	def should_not_be_success_message(self):
	    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	def success_message_should_disappear(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not dissapeared"