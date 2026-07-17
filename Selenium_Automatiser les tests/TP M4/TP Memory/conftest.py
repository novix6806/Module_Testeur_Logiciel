import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    options = Options()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    service = Service(
        executable_path=r"C:\Users\User\.cache\selenium\chromedriver\win64\150.0.7871.124\chromedriver.exe"
    )

    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.quit()
