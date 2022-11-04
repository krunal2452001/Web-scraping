import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

with open('output.csv','w') as file:
    file.write("Txn_Hash, Method, Block, Age, Value, Txn_Fee \n")

executable_path="C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path)

driver.get("https://bscscan.com/txs")
driver.maximize_window()

dropdown = driver.find_element(By.XPATH, '//select[@class="custom-select custom-select-xs mx-2"]')
radius = Select(dropdown)
radius.select_by_visible_text('100')
time.sleep(2)

tranx = driver.find_elements(By.XPATH,'//a[@class ="myFnExpandBox_searchVal"]')
method = driver.find_elements(By.XPATH, '//span[@class ="u-label u-label--xs u-label--info rounded text-dark text-center"]')
blook = driver.find_elements(By.XPATH,'//td[@class="d-none d-sm-table-cell"]/a')
age = driver.find_elements(By.XPATH, '//td[@class="showAge "]/span')
value = driver.find_elements(By.XPATH, '//tr/td[10]')
fees = driver.find_elements(By.XPATH, '//td[@ class="showTxnFee"]/span')

with open('output.csv','a') as file:
    for i in range(len(method)):
        file.write(tranx[i].text + "," + method[i].text + "," + blook[i].text + "," + age[i].text + "," + value[i].text + "," + fees[i].text + "\n")