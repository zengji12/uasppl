import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:8000/"

def test_logout(driver):
    driver.get(BASE_URL + "index.php")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign out"))).click()
    
    WebDriverWait(driver, 10).until(EC.url_contains("login.php"))
    assert "login.php" in driver.current_url
