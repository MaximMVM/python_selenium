#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# solve for https://stepik.org/lesson/181384/step/8?unit=156009

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

class Solution:
    def __init__(self, url):
        options = Options()
        options.add_argument("--headless") 
        self.browser = webdriver.Firefox(options=options, executable_path="./geckodriver")
        self.url = url
        
    def calc(self, x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    def find(self, by_type, elem):
        return self.browser.find_element(by_type, elem)
    
    def _test_(self):
        self.browser.get(self.url)
        wait = WebDriverWait(self.browser, 12)
        _id = 'price'
        btn1 = self.find(By.ID, 'book')
        wait.until(EC.text_to_be_present_in_element((By.ID, _id), '$100'))
        print('$100 click')
        btn1.click()
        x = self.find(By.ID, 'input_value').text
        ans = self.calc(x)
        field = self.find(By.ID, 'answer')
        field.send_keys(ans)
        btn2 = self.find(By.ID, 'solve')
        btn2.click()
        wait.until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        print(alert.text)
    def get_answer(self):
        try:
            self._test_()
        finally:
            self.end()
    
    def end(self):
        self.browser.quit()
        
solve = Solution('http://suninjuly.github.io/explicit_wait2.html')
solve.get_answer()
        
        
        
        
        
        
        
        
