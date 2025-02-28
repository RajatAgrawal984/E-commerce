from selenium.webdriver.common.by import By
from pages.CheckOutPage import CheckOut

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    cart = (By.CSS_SELECTOR, "div.cart_menu_btn a.checkout-button")

    def cartpage(self):
        return self.driver.find_element(*CartPage.cart)



