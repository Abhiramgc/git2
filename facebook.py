import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
#print("complete")
driver=webdriver.Chrome(r'C:/Users/Abhiram/Desktop/chromedriver.exe')
driver.get('https://en-gb.facebook.com/')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_id('email').send_keys('goldwyn.makeabhi@gmail.com')
driver.find_element_by_id('pass').send_keys('abhiram')
driver.find_element_by_id('u_0_2').click()
