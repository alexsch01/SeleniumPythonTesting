from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("Hello World"+Keys.ENTER)
driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[3]/a').click()
