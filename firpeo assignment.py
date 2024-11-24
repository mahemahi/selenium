import time
from time import sleep
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
print("List of items passed")
# Getting started with chrome driver
service = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service=service)
print("chrome opened successfully")
#1.Navigate to the FitPeo Homepage using url:
driver.get("https://www.fitpeo.com/")
print("website homepage successfully")
driver.maximize_window()
driver.implicitly_wait(30)
#2.Navigate to the Revenue Calculator Page using Tab:
link=driver.find_element(By.LINK_TEXT,"Revenue Calculator").click()
print("Revenue calculator successfully clicked")
time.sleep(2)
# Scroll Down to the Slider section
driver.find_element(By.XPATH, "//*[@id=\":r0:\"]").send_keys()
print("scrolled to scrolled")
# 3.Adjust the Slider to value 820
actions= ActionChains(driver)
text=driver.find_element(By.XPATH, "//*[@id=\":r0:\"]")
text.send_keys(Keys.BACKSPACE)
text.send_keys(Keys.BACKSPACE)
text.send_keys(Keys.BACKSPACE)
print("added value of 820")
# 4.adding the value as 820
text.send_keys(820)
time.sleep(2)
#5.verifying the 820 value is present or not
text_field = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@id=':r0:'])"))
)
assert text_field.get_attribute("value") == "820"
print("Element 820 is Displayed")

# 6.Validate Slider Value:
actions.click(text_field).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
actions.send_keys('560').perform()
assert text_field.get_attribute("value") == "560"
# 7.Select CPT Codes CPT-99091, CPT-99453, CPT-99454, and CPT-99474.
CPT_99091 = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[1]"))
)
CPT_99091.click()

print("CPT_99091 is clicked")
CPT_99453 = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[2]"))
)
CPT_99453.click()
print("CPT_99453 is clicked")
CPT_99454 = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[3]"))
)
CPT_99454.click()
print("CPT_99454 is clicked")
CPT_99474 = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[8]"))
)
CPT_99474.click()
print("CPT_99474 is clicked")
# 8.9.Total Recurring Reimbursement in Header
total_reimbursement_header: WebElement = WebDriverWait(driver, 50).until(
    EC.visibility_of_element_located((By.XPATH, "(//div[@class='MuiToolbar-root MuiToolbar-gutters MuiToolbar-regular css-1lnu3ao'])/p[4]/p"))
)
assert total_reimbursement_header.text == "$110700"
time.sleep(5)
total_reimbursement = WebDriverWait(driver, 50).until(
    EC.visibility_of_element_located((By.XPATH, "(//div[@class='MuiBox-root css-m1khva'])/p[2]"))
)
print(total_reimbursement.text)
print("Total Recurtimering Reimbursement for all Patients Per Month: shows the value $110700")
driver.quit()