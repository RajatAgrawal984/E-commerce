import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome") # help="my option: type1 or type2"

@pytest.fixture(scope="class")
def setup_browser(request):
    global driver

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--start-maximized")
        # chrome_option.add_argument("headless")
        # driver = webdriver.Chrome()
        service_obj = Service("C:/Users/Admin/Downloads/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=chrome_option)
        driver.get("https://vr-expert.com/")
        driver.implicitly_wait(10)
        # driver.maximize_window()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        # service_obj = Service("C:/Users/Admin/Downloads/geckodriver-v0.35.0-win-aarch64/geckodriver.exe")
        # driver = webdriver.Firefox(service=service_obj)
        driver.get("https://vr-expert.com/vr-headsets/")
        driver.maximize_window()

    elif browser_name == "edge":
        service_obj = Service("C:/Users/Admin/Downloads/edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
        driver.get("https://vr-expert.com/vr-headsets/")
        driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)





