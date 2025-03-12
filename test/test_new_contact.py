import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:8000/"

def test_new_contact(driver):
    driver.get(BASE_URL + "create.php")

    driver.find_element(By.NAME, "name").send_keys("Reza")
    driver.find_element(By.NAME, "email").send_keys("reza@mail.com")
    driver.find_element(By.NAME, "phone").send_keys("081336437785")
    driver.find_element(By.NAME, "title").send_keys("Hey, It's Me!")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Save']"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody/tr"))
    )

    while True:
        names = [row.text for row in driver.find_elements(By.XPATH, "//tbody/tr/td[2]")]

        if "Reza" in names:
            return

        try:
            next_button = driver.find_element(By.ID, "employee_next")

            if "disabled" in next_button.get_attribute("class"):
                break
            
            next_button.click()

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//tbody/tr"))
            )
        except:
            break

    assert False, "❌ Nama 'Reza' TIDAK ditemukan di dalam tabel."
