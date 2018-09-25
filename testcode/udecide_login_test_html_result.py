#coding=utf-8
from selenium import webdriver
import unittest
import sys
import time
import importlib
from selenium.webdriver.common.by import By
import os
import HtmlTestRunner

importlib.reload(sys)

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
        title = self.driver.title
        now_url = self.driver.current_url
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
        self.assertEqual(login_name, 123)

    def tearDown(self):
        self.driver.quit()

class TestLogin_1(unittest.TestCase):

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
        print(login_name)
        self.assertEqual(login_name, "ADMIN")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='', report_title='udecide'))
