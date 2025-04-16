from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
	page = ProductPage(browser, link)
	page.open()
	page.click_on_add_to_basket_button()
	page.should_be_add_message()
	page.should_be_basket_total_message()