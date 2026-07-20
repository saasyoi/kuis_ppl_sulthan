import time
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:8000"

# TC_REG_01
def test_register_valid(driver):
    driver.get(f"{BASE_URL}/register.php")
    driver.find_element(By.NAME, "username").send_keys("testuser123")
    driver.find_element(By.NAME, "email").send_keys("test@pengupil.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    
    assert "login" in driver.current_url.lower() or "berhasil" in driver.page_source.lower()

# TC_REG_03
def test_register_duplicate(driver):
    driver.get(f"{BASE_URL}/register.php")
    driver.find_element(By.NAME, "username").send_keys("testuser123")
    driver.find_element(By.NAME, "email").send_keys("test@pengupil.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    
    assert "register.php" in driver.current_url or "sudah" in driver.page_source.lower()
