from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import pytest
import time
from faker import Faker
import random
import string

link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
# link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# link_number = list(range(10))

class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		page = ProductPage(browser, link)
		page.open()
		page.go_to_login_page()
		login_page = LoginPage(browser, browser.current_url)
		login_page.should_be_login_page()

		# Регистрируем нового пользователя
		fake = Faker()
		email = fake.email()
		password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))
		login_page.register_new_user(email, password)

	def test_user_cant_see_success_message(self, browser):
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()
		page.click_on_add_to_basket_button()
		page.should_be_success_message(page.get_product_name())
		page.should_be_basket_total_message(page.get_product_price())

# @pytest.mark.parametrize('number', link_number)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser): # , number):
	# if number == 7:
	# 	pytest.xfail(reason="Test fails with number 7")
	# link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()
	page.click_on_add_to_basket_button()
	page.should_be_success_message(page.get_product_name())
	page.should_be_basket_total_message(page.get_product_price())
	# page.success_message_should_disappear()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	page = ProductPage(browser, link)
	page.open()
	page.click_on_add_to_basket_button()
	page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
	page = ProductPage(browser, link)
	page.open()
	page.click_on_add_to_basket_button()
	page.success_message_should_disappear()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	# link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()
	login_page = LoginPage(browser, browser.current_url)
	login_page.should_be_login_page()
	login_page.should_be_login_form()
	login_page.should_be_register_form()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket_message()
