import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_experimental_option("detach", True)
options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.maximize_window()
driver.implicitly_wait(60)
driver.set_page_load_timeout(100)
wait = WebDriverWait(driver, 90)


driver.get("https://testautomationpractice.blogspot.com/")

# title = driver.title
# print(f'The title of the page is: {title}')
# assert 'Automation Testing Practice' in title
# driver.find_element(By.ID,"name").send_keys("Bob Marley")
#
# # driver.find_element(By.CSS_SELECTOR,"button[onclick='myFunctionAlert()']").click()
# select_country = driver.find_element(By.ID,"country")
# select = Select(select_country)
# select.select_by_value("japan")
# time.sleep(2)
# select.select_by_index(3)
# time.sleep(2)
# select.select_by_visible_text("Brazil")

# select_colors = driver.find_element(By.ID,"colors")
# select = Select(select_colors)
# if select.is_multiple:
#     select.select_by_value("red")
#     time.sleep(2)
#     select.select_by_index(2)

# Laptop = driver.find_element(By.XPATH,"//a[@class='nav-link'][normalize-space()='Laptop']")
action = ActionChains(driver)
# action.move_to_element(Laptop).perform()
# action.scroll_to_element(driver.find_element(By.CSS_SELECTOR,"img[alt='Headphone']")).perform()

name = wait.until(expected_conditions.element_to_be_clickable(driver.find_element(By.ID,"name")))
# wait.until(expected_conditions.element_to_be_clickable(name))
name.send_keys("Adolf Hitler")
# action.double_click(name).perform()
# time.sleep(2)
# action.context_click(name).perform()

# draggable_object = driver.find_element(By.ID,"draggable")
# drag_location = driver.find_element(By.ID,"droppable")
# action.scroll_to_element(draggable_object).perform()
# time.sleep(2)
# action.drag_and_drop(draggable_object,drag_location).perform()


# alert = Alert(driver)
# driver.find_element(By.CSS_SELECTOR,"button[onclick='myFunctionConfirm()']").click()
# time.sleep(2)
# alert.dismiss()

iframe = driver.find_element(By.ID,"frame-one796456169")
action.scroll_to_element(iframe)
driver.switch_to.frame(iframe)
driver.find_element(By.ID,"RESULT_TextField-0").send_keys("King Nora")
driver.switch_to.default_content()

draggable_object = driver.find_element(By.ID,"draggable")
drag_location = driver.find_element(By.ID,"droppable")
action.scroll_to_element(draggable_object).perform()
time.sleep(2)
action.drag_and_drop(draggable_object,drag_location).perform()












