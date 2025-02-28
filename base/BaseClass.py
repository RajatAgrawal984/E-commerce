import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup_browser")
class BaseClass:

    def explicit_wait_xpath(self, text):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, text)))

    def page_scroll(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'} );", element)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('reports/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger