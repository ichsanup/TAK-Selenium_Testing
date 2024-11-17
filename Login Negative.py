import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from GlobalVar import Elemen
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://demowebshop.tricentis.com/")

# Empty Email
LoginBtn = driver.find_element(By.CLASS_NAME, "ico-login")
LoginBtn.click()
Email = driver.find_element(By.ID, Elemen.email)
Email.send_keys('')
Password = driver.find_element(By.ID, Elemen.password)
Password.send_keys('Password123')
BtnLogin = driver.find_element(By.XPATH, Elemen.login_btn)
BtnLogin.click()

# Empty Password
LoginBtn = driver.find_element(By.CLASS_NAME, "ico-login")
LoginBtn.click()
Email = driver.find_element(By.ID, Elemen.email)
Email.send_keys('ichsanup@gmail.com')
Password = driver.find_element(By.ID, Elemen.password)
Password.send_keys('')
BtnLogin = driver.find_element(By.XPATH, Elemen.login_btn)
BtnLogin.click()


try:
    element = driver.find_element(By.XPATH, Elemen.gift_card)
    print("Teks elemen ditemukan:", element.text)  # Cetak teks elemen
    element.click()  # Klik elemen jika diperlukan
except Exception as e:
    print("Elemen tidak ditemukan:", e)

# Empty Input Data Buyer
Recipent_Name = driver.find_element(By.ID, Elemen.recipient_name)
Recipent_Name.send_keys("")
Recipent_Email = driver.find_element(By.ID, Elemen.recipient_email)
Recipent_Email.send_keys("")
Btn_Cart = driver.find_element(By.ID, Elemen.btn_cart)
Btn_Cart.click()

# Validasi Element dengan Click menggunakan ActionChains
Shopping_cart = driver.find_element(By.XPATH, Elemen.shopping_cart)
try:
    ActionChains(driver).move_to_element(Shopping_cart).click().perform()
    print("Expected Result: Elemen dapat diklik.")
except Exception as e:
    print("Expected Result: Elemen tidak dapat diklik.", e)

ChecklistBtn = driver.find_element(By.ID, Elemen.checklist_btn)
ChecklistBtn.click()
CheckoutBtn = driver.find_element(By.ID, Elemen.checkout_btn)
CheckoutBtn.click()


time.sleep(5)
driver.quit()
