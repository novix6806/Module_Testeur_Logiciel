from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_testaccueil(driver):
    driver.get("https://enijdenis.github.io/memory/index.html")
    driver.find_element(By.LINK_TEXT, "Accueil").click()

    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p"))
    )

    assert driver.find_element(By.CSS_SELECTOR, "p").text == "Bienvenue sur le site du Memory de l'ENI."
  
