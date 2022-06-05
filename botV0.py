from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #cap = DesiredCapabilities().CHROME
        #cap["marionette"] = False
        self.driver = webdriver.Firefox(executable_path = r"C:\Users\Lian Rodrigues\Desktop\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        #//input[@name="username"]
        #//input[@name="password"]
        #campoUsuario = driver.find_element_by_xpath("//input[@name="username"]")
        #botaoLogin = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        #botao_login.click
lianBot = InstagramBot('', '')
lianBot.login()