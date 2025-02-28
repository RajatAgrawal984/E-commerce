from selenium.webdriver.common.by import By
from pages.ProductPage import ProductPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    VR_Headsets = (By.XPATH, "//li[@id='menu-item-25569']")
    AR_Headsets = (By.XPATH, "//li[@id='menu-item-25575']")

    def VRHeadset_product(self):
        return self.driver.find_element(*HomePage.VR_Headsets)
        # productpage_obj = ProductPage(self.driver)
        # return productpage_obj
        # self.driver.find_element(By.XPATH, "//li[@id='menu-item-25569']").click()

    def ARHeadsets_product(self):
        return self.driver.find_element(*HomePage.AR_Headsets)

