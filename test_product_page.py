from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import pytest
import time

link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

link_number = list(range(10))

@pytest.mark.parametrize('number', link_number)
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, number):
	if number == 7:
		pytest.xfail(reason="Test fails with number 7")
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
	print(link)
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()
	page.click_on_add_to_basket_button()
	page.should_be_success_message(page.get_product_name())
	page.should_be_basket_total_message(page.get_product_price())
	page.success_message_should_disappear()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	page = ProductPage(browser, link)
	page.open()
	page.click_on_add_to_basket_button()
	page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
	page = ProductPage(browser, link)
	page.open()
	page.click_on_add_to_basket_button()
	page.success_message_should_disappear()