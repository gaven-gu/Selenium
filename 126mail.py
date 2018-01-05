#coding=utf-8

from selenium import webdriver

file_info = open('D:\qqmusic.txt')
values = file_info.readlines()
file_info.close()


for search in values:
    driver= webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    driver.quit()
