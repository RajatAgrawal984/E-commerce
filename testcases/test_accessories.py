import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from unicodedata import category

from base.BaseClass import BaseClass
from pages.PopUp import PopUp


class TestAccessories(BaseClass):

    def test_accessories(self):

        # ---------- Select the categories from the Home menu start ----------

        hover_element = self.driver.find_element(By.XPATH,"//ul[@id='menu-main-menu']/li[3]")
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()
        time.sleep(3)

        allcategory = self.driver.find_elements(By.XPATH, "//div[@class='catN-List']/ul/li/a")

        for category in allcategory:
            print(category.text)
            if category.text == "Flight Cases >":
                category.click()
                break
        time.sleep(5)

        # ---------- Select the categories from the Home menu start ----------

        # ---------- Select the one product from the product category page start ----------

        # products = (WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(
        #     (By.XPATH, "//ul[@class='products oceanwp-row clr prdlist grid']/li")))
        #             .find_elements(By.XPATH, "//ul[@class='products oceanwp-row clr prdlist grid']/li"))

        products = self.driver.find_elements(By.XPATH, "//ul[@class='products oceanwp-row clr prdlist grid']/li")

        for product in products:
            product_name = product.find_element(By.XPATH, "div/div/div/h2")
            if product_name.text == "Flight Case for 1 x Pico 4 Enterprise":
                time.sleep(2)
                self.page_scroll(product_name)

                time.sleep(2)
                product.find_element(By.XPATH, "div/div/div/div[@class='addtocartbtn']").click()
                break
        time.sleep(5)

        # ---------- Select the one product from the product category page end ----------

    # ---------- POP-UP opens start ----------

        cartpop_obj = PopUp(self.driver)

        # ---------- Click on the ad to cart button start -----------

        cartpop_obj.add_to_cart_button().click()
        # self.driver.find_element(By.XPATH, "//div[@class='popup_add']/button").click()

        # ---------- Click on the add to cart button end -----------

        # ---------- Click on the View cart/basket start -----------

        view_basket_path = "//div[@class='popup_add']/a"

        view_button = self.explicit_wait_xpath(view_basket_path)
        view_button.click()
        time.sleep(5)

        # ---------- Click on the View cart/basket end -----------

    # ---------- POP-UP opens start ----------

    # ---------- Cart page start ----------

        proceed_to_checkout = self.driver.find_element(By.XPATH, "//div[@class='cart_menu_btn']/a[2]")

        self.page_scroll(proceed_to_checkout)


        time.sleep(2)
        proceed_to_checkout.click()
        time.sleep(5)

    # ---------- Cart page end ----------