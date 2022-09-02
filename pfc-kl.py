import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("http://192.168.86.228:8124/")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")
elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")
driver.find_element(By.XPATH, "//*[@id='login']/div[3]/div/input").click()
driver.get("http://192.168.86.228:8124/")
time.sleep(20)
driver.find_element(By.XPATH, "//*[@id='CreateTicketInQueue']/div[1]/input").click()
elemento1 = driver.find_element(By.ID, "Cc-selectized")
elemento1.clear()
elemento1.send_keys("karen.lima@estudiantes.utec.edu.uy")
time.sleep(20)
driver.close()