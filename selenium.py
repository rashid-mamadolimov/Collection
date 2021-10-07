
from selenium import webdriver


driver = webdriver.Chrome("C:/Users/Rashid/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('http://apply.dataprocessors.com.au/')

jref = driver.find_element_by_name('jobref')
ans = driver.find_element_by_name('valuee')
count = len(driver.find_elements_by_xpath("//img[@src = 'filledO.gif']"))
but = driver.find_element_by_xpath("//input[@type = 'Submit']")

jref.send_keys('PO182')
ans.send_keys(count)
but.click()






