#coding=utf-8
from selenium import webdriver
import unittest
import sys
import time
import importlib
from selenium.webdriver.common.by import By
import os
from HTMLTestRunner import HTMLTestRunner

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

    def test_login_user_error(self):
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
 
    def test_login_user_null(self):
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
        self.assertEqual(login_name, "ADMIN")

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

if __name__ == '__main__':

    report_title = 'Login module test report'
    desc = 'Detail login test for udecide'

    #date=time.strftime("%Y%m%d")
    datetime=time.strftime("%Y%m%d%H%M%S")
    
    path= 'reports/'  #+ date +"/login/"+datetime+"/"
 
    report_path = path + datetime +"_report.html"
 
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    
    #define a test container
    testsuite = unittest.TestSuite()
    
    #add test case into the container
    testsuite.addTest(TestLogin("test_login"))
    testsuite.addTest(TestLogin("test_login_user_error"))
    #testsuite.addTest(TestLogin("test_login_user_null"))
    
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)
    
    report.close()
