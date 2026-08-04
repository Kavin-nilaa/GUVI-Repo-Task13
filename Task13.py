from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")

actions = ActionChains(driver)

frame = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(frame)

source = driver.find_element(By.ID,"draggable")
target = driver.find_element(By.ID,"droppable")

actions.drag_and_drop(source,target).perform() #to drag the source to the target

driver.switch_to.default_content()
driver.quit()
