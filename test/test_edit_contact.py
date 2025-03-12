import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:8000/"

def test_edit_contact(driver):
    driver.get(BASE_URL + "index.php")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "employee_next"))
    ).click()

    rows = driver.find_elements(By.XPATH, "//tbody/tr")
    for row in rows:
        name = row.find_element(By.XPATH, "./td[2]").text

        if name == "Reza":
            edit_button = row.find_element(By.XPATH, ".//a[contains(text(), 'edit')]")
            driver.execute_script("arguments[0].scrollIntoView();", edit_button)
            edit_button.click()

            name_input = driver.find_element(By.ID, "name")
            name_input.clear()
            updated_name = "Reza Updated"
            name_input.send_keys(updated_name)

            driver.find_element(By.XPATH, "//input[@type='submit' and @value='Update']").click()

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tbody/tr"))
            )

            driver.refresh()
            names = [row.text for row in driver.find_elements(By.XPATH, "//tbody/tr/td[2]")]
            assert updated_name in names, "❌ Nama 'Reza Updated' TIDAK ditemukan."
            return
