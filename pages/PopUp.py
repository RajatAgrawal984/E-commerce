from selenium.webdriver.common.by import By
from pages.CartPage import CartPage

class PopUp:

    def __init__(self, driver):
        self.driver = driver

    addtocart_button = (By.XPATH, "//div/button[@class='button part_btn']")
    viewcart = (By.XPATH, "//div[@class='popup_add']/a")

    def add_to_cart_button(self):
        return self.driver.find_element(*PopUp.addtocart_button)
        # self.driver.find_element(By.XPATH, "//div/button[@class='button part_btn']").click()

    def view_cart(self):
        return self.driver.find_element(*PopUp.viewcart)
        # self.driver.find_element(By.XPATH, ""//div[@class='popup_add']/a").click()