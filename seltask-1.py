from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


url = "https://www.saucedemo.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
driver.find_element(By.ID,'user-name').send_keys("standard_user")
driver.find_element(By.ID,'password').send_keys("secret_sauce")
driver.find_element(By.ID,'login-button').click()

t = driver.title
u = driver.current_url

print("Title",t)
print("URL",u)
f = open("webpage_task_11.txt","w")
f.writelines(driver.find_element(By.XPATH, "/html/body").text)



sleep(5)




