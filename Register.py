from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from GlobalVar import Elemen

driver = webdriver.Firefox()
driver.get("https://demowebshop.tricentis.com/")

RegistBtn = driver.find_element(By.XPATH, Elemen.regist_btn)
RegistBtn.click()
Gender = driver.find_element(By.ID, Elemen.gender)
Gender.click()
FirstName = driver.find_element(By.ID, Elemen.first_name)
FirstName.send_keys('Ichsan')
LastName = driver.find_element(By.ID, Elemen.last_name)
LastName.send_keys('Putra')
Email = driver.find_element(By.ID, Elemen.email)
Email.send_keys('ichsanuu@gmail.com')
Password = driver.find_element(By.ID, Elemen.password)
Password.send_keys('Password123')
Confirm_Password = driver.find_element(By.ID, Elemen.confirm_pw)
Confirm_Password.send_keys('Password123')
Btn_Regist = driver.find_element(By.ID, Elemen.regist_btn)
Btn_Regist.click()

try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Categories"))
    )
finally:
    driver.quit()
