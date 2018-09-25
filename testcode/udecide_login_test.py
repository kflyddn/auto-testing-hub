#coding=utf-8
from selenium import webdriver
import unittest
import sys
import time
import importlib
from selenium.webdriver.common.by import By
import logging
import os

importlib.reload(sys)
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#logging.basicConfig(level=logging.INFO,
#                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                    datefmt='%a, %d %b %Y %H:%M:%S',
#                    filename='../testlog/log_test.log',
#                    filemode='w')
#logger = logging.getLogger()

class TestLogin(unittest.TestCase):

    def setUp(self):
        firefox_capabilities ={
            "browserName": "firefox",
            "version": "61.0.2",
            "maxInstances": 3,
            "platform": "ANY",
            "javascriptEnabled": True,
            "marionette": True,
        }
        try:
            self.driver = webdriver.Remote("http://192.168.86.19:4444/wd/hub",desired_capabilities=firefox_capabilities)
            
            self.driver.get("https://udecide-demo.digitalalchemy.net.au/login")
        except Exception as e:
            self.driver.quit()

    def test_login(self):
        print("test login page of udecide")
        try:
            title = self.driver.title
            print(title)
            now_url = self.driver.current_url
            print(now_url)
            username = "udecide"
            password = "@uDec1de"
            
            self.driver.find_element_by_id("username").clear()
            self.driver.find_element_by_id("username").send_keys(username)
            
            self.driver.find_element_by_id("password").clear()
            self.driver.find_element_by_id("password").send_keys(password)
            
            #self.driver.find_element_by_css_selector("button").click()
            #self.driver.find_element_by_id("submit").click()
            self.driver.find_element_by_tag_name("button").click()
            time.sleep(10)
            
            #login_name = self.driver.find_element_by_xpath('html/body/div[2]').text
            login_name = self.driver.find_element_by_link_text("ADMIN").text
            #login_name = self.driver.find_element_by_xpath('html/body/div[3]/div[2]/ul/li[1]/a/strong').text
            print(login_name)
            #assert login_name == "ADMINaaaaaaaaaaaaa"
            self.assertTrue(login_name == "ADMINaaaaaaaaaaaaa")
            print("test case %r = %r", 'login page test', 'OK')
            #assert login_name == "You are now logged in. Welcome back!"
        except Exception as e:
            print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n")
            print(str(e))

    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()