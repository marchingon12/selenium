from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

url = "https://google.com"

driver.get(url)