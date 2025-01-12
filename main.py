import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


#acessar site 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.starplus.com/pt-br/home")
driver.maximize_window()

#entrar na tela de login
time.sleep(5)
driver.find_element("xpath",'//a[@href="/login"]').click()

#colocar email e senha
time.sleep(4)
driver.find_element("xpath",'//input[@aria-label="E-mail"]').send_keys(os.environ.get("email"))
driver.find_element("xpath",'//button[@data-testid="login-continue-button"]').click()
time.sleep(3)
driver.find_element("xpath",'//input[@aria-describedby="password__error"]').send_keys(os.environ.get("password"))
driver.find_element("xpath",'//button[@data-testid="password-continue-login"]').click()

#escolher o perfil
time.sleep(3)
driver.find_element("xpath",'//div[@class="sc-qrIAp sc-gtfDJT eromxt profile-avatar"]').click()

#entrar no ultimo ep assitido
time.sleep(6)
driver.get("https://www.starplus.com/pt-br/series/swat/Hm2Kv5LjHqS9")
time.sleep(5)
driver.find_element("xpath",'//button[@data-testid="play-button"]').click()
time.sleep(5)
#tela cheia
a = driver.find_element("xpath",'//div[@class="overlay overlay__controls overlay__controls--visually-hide"]')
ActionChains(driver).move_to_element(a).perform()
driver.find_element("xpath",'//button[@class="control-icon-btn fullscreen-icon"]').click()

#verificar se a tela ainda esta cheia
fullscreen = True
while fullscreen == True:
    try:
        driver.find_element("xpath",'//button[@class="control-icon-btn exit-fullscreen-icon"]')
    except:
        time.sleep(5)
        a = driver.find_element("xpath",'//div[@class="overlay overlay__controls overlay__controls--visually-hide"]')
        ActionChains(driver).move_to_element(a).perform()
        driver.find_element("xpath",'//button[@class="control-icon-btn fullscreen-icon"]').click()