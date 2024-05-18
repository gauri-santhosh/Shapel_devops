# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestNewsletter():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_newsletter(self):
    self.driver.get("http://localhost:5000/")
    self.driver.set_window_size(817, 613)
    self.driver.find_element(By.CSS_SELECTOR, "form > input").click()
    self.driver.find_element(By.CSS_SELECTOR, "form > input").send_keys("priyanka.whee@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(2)").click()
  
