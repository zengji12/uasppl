import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:8000/"

def test_delete_contact(driver):
    driver.get(BASE_URL + "login.php")
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("nimda666!")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), \"OK I'm sign in\")]"))
    ).click()

    driver.get(BASE_URL + "create.php")

    driver.find_element(By.NAME, "name").send_keys("Reza")
    driver.find_element(By.NAME, "email").send_keys("reza@mail.com")
    driver.find_element(By.NAME, "phone").send_keys("081336437785")
    driver.find_element(By.NAME, "title").send_keys("Hey, It's Me!")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Save']"))
    ).click()

    driver.get(BASE_URL + "index.php")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "employee_next"))
    ).click()
    
    rows = driver.find_elements(By.XPATH, "//tbody/tr")
    for row in rows:
        name = row.find_element(By.XPATH, "./td[2]").text

        if name == "Reza":
            delete_button = row.find_element(By.XPATH, ".//a[contains(text(), 'delete')]")
            delete_button.click()

            WebDriverWait(driver, 5).until(EC.alert_is_present())
            driver.switch_to.alert.accept()

            driver.refresh()
            names = [row.text for row in driver.find_elements(By.XPATH, "//tbody/tr/td[2]")]
            assert "Reza Updated" not in names, "❌ Nama 'Reza Updated' masih ada setelah dihapus."
            return
