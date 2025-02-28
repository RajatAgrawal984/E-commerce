import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.BaseClass import BaseClass


class Testsoftware(BaseClass):

    def test_software(self):

        self.driver.find_element(By.XPATH,"//div[@class='cstm_popupbtns']/a[1]").click()

        # ----------- Click on the Software in the menu start ----------

        hover_software = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//ul[@id='menu-main-menu']/li[4]")))

        # hover_software = self.driver.find_element(By.XAPTH,"//ul[@id='menu-main-menu']/li[4]")
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_software).perform()

        # ------------ click on the category form the software start ---------

        software_category = self.driver.find_elements(By.XPATH,"//div[@class='catN-List']/ul/li/a")

        for category in software_category:
            # time.sleep(3)
            if category.text == "VR software >":
                category.click()
                break
        time.sleep(3)

    # ------------ click on the category form the software end ---------

    # ----------- Click on the Software in the menu end ----------

    # ------------ Select one of the software product start -----------


        software_product_list = self.driver.find_elements(By.XPATH,"//ul[@class='products oceanwp-row clr prdlist grid']/li")

        for product in software_product_list:
            product_name = product.find_element(By.XPATH,"div/div/div/div/h3")
            if product_name.text == "ArborXR":
                self.page_scroll(product_name)
                time.sleep(2)
                self.page_scroll(product.find_element(By.XPATH,"div/div/div/div/div[@class='addtocartbtn']"))
                time.sleep(2)
                product.find_element(By.XPATH,"div/div/div/div/div[@class='addtocartbtn']").click()
                break
        time.sleep(3)

    # ------------ Select one of the software product end -----------

        self.driver.find_element(By.XPATH,"//div[@class='popup_add']/button").click()

        view_basket = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='popup_add']/a[@id='view_cart']")))
        print(view_basket.text)
        self.driver.find_element(By.XPATH,"//div[@class='popup_add']/a[@id='view_cart']").click()

        time.sleep(5)

    # ------------ Select one of the software product end -----------

    # ----------- On the cart page click on the Proceed to chckoutpage start ------------

        checkout_button = self.driver.find_element(By.XPATH, "//div[@class='cart_menu_btn']/a[2]")
        self.page_scroll(checkout_button)
        time.sleep(2)
        checkout_button.click()
        time.sleep(5)

    # ----------- On the cart page click on the Proceed to chckoutpage end ------------

    # ----------- Fill the form on the checkout page start ------------

        # ------ First Name -----
        self.driver.find_element(By.XPATH,"//input[@id='billing_first_name']").send_keys("Rajat")

        # ----- Last Name -------
        self.driver.find_element(By.XPATH,"//input[@id='billing_last_name_field']").send_keys("Agrawal")

        # ------- Email field ------
        self.driver.find_element(By.XPATH, "//input[@id='billing_email_field']").send_keys("rajat@believintech.com")

        # ------ Phone nUmber field ------
        self.driver.find_element(By.XPATH, "//input[@id='billing_phone_field']").send_keys("1231232323")

        # ------ select Country Field ------
        select_country = self.driver.find_element(By.XPATH, "//input[@id='billing_country']")
        self.page_scroll(select_country)
        a = Select(select_country)
        a.select_by_value("NL")
        time.sleep(3)

        # ----- address field ------
        self.driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("Testing123")

        # ------ Postcode field -----
        self.driver.find_element(By.XPATH, "//input[@id='billing_postcode_field']").send_keys("1234 AR")

        # ------ Company Name ------
        self.driver.find_element(By.XPATH, "//input[@id='billing_company_field']").send_keys("Believ_in Technologies")

        # ------- City field --------
        self.driver.find_element(By.XPATH, "//input[@id='billing_city_field']").send_keys("Test")

        # ------ VAT number field -------
        self.driver.find_element(By.XPATH, "//input[@id='billing_eu_vat_number_field']").send_keys("NL857935252B01")

        # --------- Click on the Proceed to payment ---------
        self.driver.find_element(By.XPATH, "//div[@class='max-571 mt-66']/a[2]").click()
        time.sleep(5)













