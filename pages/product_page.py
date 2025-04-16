from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
	def click_on_add_to_basket_button(self):
		add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
		add_button.click()
		self.solve_quiz_and_get_code()

	def should_be_add_message(self):
		assert self.is_element_present(*ProductPageLocators.ADD_MESSAGE), "'Added to basket' message is not presented"
		assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == self.browser.find_element(*ProductPageLocators.ADD_MESSAGE).text, "Book titles don't match"

	def should_be_basket_total_message(self):
		assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "'Basket total' message is not presented"
		assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text, "Basket total does not match the book price"