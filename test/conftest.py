from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import chromedriver_autoinstaller
from utilities.customLogger import LogGen


service = Service(executable_path=ChromeDriverManager().install())

# @pytest.fixture()
# def driver():
#     options = Options()
#     options.add_argument('--disable-blink-features=AutomationControlled')
#     options.add_argument('headless')
#     options.add_argument("start-maximized")
#     driver = webdriver.Chrome(service=service, options=options)
#     return driver

@pytest.fixture()
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(service=Service())
    driver.maximize_window()
    return driver

@pytest.fixture()
def logger():
    return LogGen.loggen()