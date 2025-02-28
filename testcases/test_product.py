import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.BaseClass import BaseClass
from pages.CartPage import CartPage
from pages.CheckOutPage import CheckOut
from pages.HomePage import HomePage
from pages.PopUp import PopUp
from pages.ProductPage import ProductPage
from testdata.CheckoutPageData import CheckOutPageData


# @pytest.mark.usefixtures("setup_browser")
class TestProduct(BaseClass):

    @pytest.mark.parametrize("getdata,get_product, single_product",
                             [(CheckOutPageData.test_checkoutpage_data[0],CheckOutPageData.product_cat[0],CheckOutPageData.product_name[0]),
                              (CheckOutPageData.test_checkoutpage_data[1],CheckOutPageData.product_cat[1],CheckOutPageData.product_name[1])])
    def  test_productpage(self, getdata, get_product, single_product):

        log = self.getLogger()

        # ---------- Select the categories from the Home menu start ----------

        nev_items = self.driver.find_elements(By.XPATH,"//ul[@id='menu-main-menu']/li")

        for item in nev_items:
            if item.text == get_product["product_name"]:
                log.info(item.text)
                item.click()
                break
            # item_name = nev_items.find_element(By.XPATH,"a").text
            # if item_name == "VR Headsets":
            #     item.find_element(By.XPATH,"")

        # home_page = HomePage(self.driver)
        # home_page.VRHeadset_product().click()
        # productpage_obj = home_page.VRHeadset_product()
        # self.driver.find_element(By.XPATH, "//li[@id='menu-item-25569']").click()
        # time.sleep(5)

        # ---------- Select the categories from the Home menu end ----------

        # ---------- Select the one product from the product category page start ----------

        productpage_obj = ProductPage(self.driver)
        log.info("getting all the card titles")
        products = productpage_obj.product_page()

        # products = self.driver.find_elements(By.XPATH, "//ul[@class='products oceanwp-row clr prdlist grid']/li")

        for product in products:
            product_name = product.find_element(By.XPATH, "div/div/div/h2/a").text
            log.info(product_name)
            # print(f"Product name:{product_name}")
            if product_name == single_product["singleproduct_name"]:
                time.sleep(2)
                self.page_scroll(product.find_element(By.XPATH, "div/div/div/div[@class='addtocartbtn']"))
                # element = product.find_element(By.XPATH, "div/div/div/div[@class='addtocartbtn']")
                # self.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(2)
                product.find_element(By.XPATH, "div/div/div/div[@class='addtocartbtn']").click()
                break

        # ---------- Select the one product from the product category page end ----------

        # ---------- POP-UP opens start ----------

        time.sleep(2)
        popup_obj = PopUp(self.driver)
        # self.explicit_wait_xpath(popup_obj.Add_to_cart_button())
        popup_obj.add_to_cart_button().click()
        # self.driver.find_element(By.XPATH, "//div/button[@class='button part_btn']").click()
        time.sleep(2)
        popup_obj.view_cart().click()
        # self.driver.find_element(By.ID, "view_cart").click()

        # ---------- POP-UP opens end ----------

        # ---------- Cart page start ----------

        cart_page_obj = CartPage(self.driver)
        element1 = cart_page_obj.cartpage()
        # element1 = self.driver.find_element(By.CSS_SELECTOR, "div.cart_menu_btn a.checkout-button")
        self.page_scroll(element1)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element1)
        time.sleep(2)

        cart_page_obj.cartpage().click()
        # self.driver.find_element(By.CSS_SELECTOR, "div.cart_menu_btn a.checkout-button").click()
        time.sleep(5)

        # ---------- Cart page end ----------

        # ---------- Checkout page start ----------

        checkout_obj = CheckOut(self.driver)

        checkout_obj.checkout_firstname().send_keys(getdata["firstname"])
        log.info("User first name is:"+getdata["firstname"])
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_first_name").send_keys("Rajat")
        time.sleep(1)

        # checkout_obj.checkout_lastname().send_keys(getdata["lastname"])
        self.driver.find_element(By.CSS_SELECTOR, "#billing_last_name").send_keys("Agrawal")
        time.sleep(1)

        checkout_obj.checkout_email().send_keys(getdata["email"])
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_email").send_keys("rajat@believintech.com")
        time.sleep(1)

        checkout_obj.checkout_phone().send_keys(getdata["phone"])
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_phone").send_keys("123231233")
        time.sleep(1)

        element3 = self.driver.find_element(By.CSS_SELECTOR, "#select2-billing_country-container")
        self.page_scroll(element3)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element3)
        time.sleep(2)

        select_country = Select(checkout_obj.checkout_country())
        # select_country = Select(self.driver.find_element(By.XPATH, "//select[@name='billing_country']"))
        time.sleep(1)

        # select_country.select_by_index(1)
        select_country.select_by_value("NL")
        # select_country.select_by_visible_text("Netherlands")
        time.sleep(1)

        # self.explicit_wait_xpath("#billing_address_1")
        checkout_obj.checkout_address1().send_keys(getdata["address"])
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_address_1").send_keys("Test 123")
        time.sleep(1)

        checkout_obj.checkout_postcode().send_keys(getdata["post_code"])
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_postcode").send_keys("1234 RA")
        time.sleep(1)

        checkout_obj.checkout_company().send_keys(getdata["company_name"])
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_company").send_keys("Believ-In Technologies Pvt Ltd")
        time.sleep(1)

        checkout_obj.checkout_city().send_keys(getdata["city"])
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_city").send_keys("Gurgaon")
        time.sleep(1)

        checkout_obj.checkout_vat().send_keys(getdata["Vat_number"])
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_eu_vat_number").send_keys("NL857935252B01")
        time.sleep(1)

        element2 = self.driver.find_element(By.CSS_SELECTOR,"#next-payment")
        self.page_scroll(element2)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element2)
        time.sleep(1)

        checkout_obj.checkout_button().click()
        # self.driver.find_element(By.CSS_SELECTOR,"#next-payment").click()
        time.sleep(1)

        # ---------- Checkout page end ----------

        # ----------- Back to Home page start ------------

        back_to_home = self.driver.find_element(By.XPATH,"//div[@class='div-img']")
        self.driver.execute_script("arguments[0].scrollIntoView();", back_to_home)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class='div-img']").click()
        log.info("Test Pass Rajat")
        time.sleep(5)

    # @pytest.fixture(params=[{"firstname":"Rajat", "lastname":"Agrawal","email":"rajat@believintech.com","phone":"1231231232"
    #                          ,"address":"Test 123"}])
    @pytest.fixture(params=CheckOutPageData.test_checkoutpage_data)
    def getdata(self, request):
        return request.param

    @pytest.fixture(params=CheckOutPageData.product_cat)
    def get_product(self,request):
        return request.param

    @pytest.fixture(params=CheckOutPageData.product_name)
    def single_product(self, request):
        return request.param







