from selenium.webdriver.common.by import By
from pages.PaymentPage import PaymentPage

class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    firstname = (By.CSS_SELECTOR, "#billing_first_name")
    lastname = (By.CSS_SELECTOR, "#billing_last_name")
    email = (By.CSS_SELECTOR, "#billing_email")
    phone = (By.CSS_SELECTOR, "#billing_phone")
    country = (By.XPATH, "//select[@name='billing_country']")
    address1 = (By.CSS_SELECTOR, "#billing_address_1")
    postcode = (By.CSS_SELECTOR, "#billing_postcode")
    companyname = (By.CSS_SELECTOR, "#billing_company")
    city = (By.CSS_SELECTOR, "#billing_city")
    vatnumber = (By.CSS_SELECTOR, "#billing_eu_vat_number")
    checkoutbutton = (By.CSS_SELECTOR, "#next-payment")

    def checkout_firstname(self):

        return self.driver.find_element(*CheckOut.firstname)
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_first_name").send_keys("Rajat")
    def checkout_lastname(self):
        return self.driver.find_element(*CheckOut.lastname)
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_last_name").send_keys("Agrawal")

    def checkout_email(self):
        return self.driver.find_element(*CheckOut.email)
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_email").send_keys("rajat@believintech.com")

    def checkout_phone(self):
        return self.driver.find_element(*CheckOut.phone)
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_phone").send_keys("123231233")

    def checkout_country(self):
        return self.driver.find_element(*CheckOut.country)
        # select_country = Select(self.driver.find_element(By.XPATH, "//select[@name='billing_country']"))

    def checkout_address1(self):
        return self.driver.find_element(*CheckOut.address1)
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_address_1").send_keys("Test 123")

    def checkout_postcode(self):
        return self.driver.find_element(*CheckOut.postcode)
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_postcode").send_keys("1234 RA")

    def checkout_company(self):
        return self.driver.find_element(*CheckOut.companyname)
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_company").send_keys("Believ-In Technologies Pvt Ltd")

    def checkout_city(self):
        return self.driver.find_element(*CheckOut.city)
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_city").send_keys("Gurgaon")

    def checkout_vat(self):
        return self.driver.find_element(*CheckOut.vatnumber)
        # self.driver.find_element(By.CSS_SELECTOR, "#billing_eu_vat_number").send_keys("NL857935252B01")

    def checkout_button(self):
        return self.driver.find_element(*CheckOut.checkoutbutton)

        # self.driver.find_element(By.CSS_SELECTOR, "#next-payment").click()

