from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import pytest
import time

# link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

link_number = list(range(2))

@pytest.mark.parametrize('number', link_number)
def test_guest_can_add_product_to_basket(browser, number):
	if number == 7:
		pytest.xfail(reason="Test fails with number 7")
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
	print(link)
	page = ProductPage(browser, link)
	page.open()
	page.click_on_add_to_basket_button()
	page.should_be_add_message(page.get_product_name())
	page.should_be_basket_total_message(page.get_product_price())