from selenium.webdriver.common.by import By
from urllib3.util.util import reraise


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    productpage = (By.XPATH,"//ul[@class='products oceanwp-row clr prdlist grid']/li")

    def product_page(self):

        return self.driver.find_elements(*ProductPage.productpage)
        # products = self.driver.find_elements(By.XPATH, "//ul[@class='products oceanwp-row clr prdlist grid']/li")

