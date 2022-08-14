import scrapy
import csv

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

# https://anilist.co/search/manga/top-100

class Aniscrap (scrapy.Spider):
    name = 'anispider'
    start_urls = ["https://anilist.co/search/manga/top-100"]

    def parse (self,response):

        driver= webdriver.Chrome()

        driver.execute_script("window.scrollBy(0 , 100000 );")
        
        driver.get("https://anilist.co/search/manga/top-100")
        
        try:
            element_present = EC.presence_of_element_located((By.ID, 'element_id'))
            WebDriverWait(driver, 10).until(element_present)
        except TimeoutException:
            soup = bs(driver.page_source,'lxml')
        
        splitsoup = (soup.prettify())
        print(splitsoup)

        with open('dataviz.csv','w',newline='',encoding="utf-8") as csvfile:
            csvWriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csvWriter.writerow(splitsoup)
            
