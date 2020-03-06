# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import xlwt

browser = webdriver.Firefox()
browser.get("https://www.bilibili.com/")

input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="nav_searchform"]/input')))

submit = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="nav_searchform"]/div/button')))
input.send_keys('zhexue')
submit.click()
all_h = browser.window_handles
browser.switch_to.window(all_h[1])
