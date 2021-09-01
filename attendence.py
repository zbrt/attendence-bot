#CREDITS OGGY
#zbrt.github.io - website


from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

#If your using linux . I prefer Firefox driver
driver = webdriver.Firefox()

#we are going to give a variable as 'url'
url = ('CLASROOM URL HERE')

driver.set_window_size(1024, 600)
driver.maximize_window()

#This gets the webpage URL opened up
driver.get(url)

#This finds the element and clicks or enters it 
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('USERNAME HERE')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys('PASSWORD HERE')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
time.sleep(1.5)

#change this to your class xpath
driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[5]/div[2]/aside/div/div[2]/div/div/div[1]/a').click()


