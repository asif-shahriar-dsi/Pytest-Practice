import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(30)
wait = WebDriverWait(30)
wait.until(expected_conditions.element_to_be_clickable())

name = driver.find_element(By.ID,"name")

btn_search = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
btn_search.is_displayed()
actions = ActionChains(driver)
# actions.move_to_element(btn_search).context_click(btn_search).perform()
name.send_keys("Bla")
# actions.double_click(name).context_click(name).perform()
drag_object = driver.find_element(By.ID,"draggable")
drag_location = driver.find_element(By.ID,"droppable")
actions.scroll_to_element(drag_object).perform()
actions.drag_and_drop(drag_object,drag_location).perform()

btn_alert = driver.find_element(By.CSS_SELECTOR,"button[onclick='myFunctionConfirm()']")
btn_alert.click()
alert = Alert(driver)
time.sleep(2)
alert.accept()
text_after_accepting_alert = driver.find_element(By.ID,"demo").text
assert 'You pressed OK!' in text_after_accepting_alert

print(driver.title)
assert 'Automation Testing Practice' in driver.page_source
btn_alert.click()

alert.dismiss()
driver.find_element(By.CSS_SELECTOR,"button[onclick='myFunctionPrompt()']").click()

alert.send_keys("bla bla")
alert.accept()
select = Select(driver.find_element(By.ID,"colors"))
if select.is_multiple:
    select.select_by_value("blue")
    select.select_by_value("green")
iframe = driver.find_element(By.ID,"frame-one796456169")
iframe.screenshot("Iframe SS.png")
driver.switch_to.frame(iframe)
driver.find_element(By.ID,"RESULT_TextField-0").send_keys("Into the iframe")
driver.switch_to.default_content()

iframe.screenshot("Iframe SS.png") #SS of an element
driver.save_screenshot("D:\\SS\\Full_Page.png") #SS of a page

time.sleep(6)

