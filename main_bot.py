import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait():
    wait_time = randint(2, 5)
    sleep = time.sleep(wait_time)
    return sleep

def compare(adress):
    file = open("baza", "r")
    if adress in file.read():
        print("Już zalajkowane")
        file.close()
        return True
    else:
        file.close()

def loading():
    wait()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]")))
    current_url = driver.current_url
    if compare(current_url) != True:
        f = open("baza", "a")
        f.write(current_url + "\n")
        f.close()
        print("Lajkuje zdjęcie")
        wait()
        driver.find_element(By.CLASS_NAME, "fr66n").click()
        wait()
    driver.find_element(By.CSS_SELECTOR, "body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow").click()


# -- init bot
login = "type_username"
password = "type_password"
hash = input("Hash: #")
driver = webdriver.Chrome(r'path_to_chromedriver')
profile = 0


#-- login
print("Logowanie")
driver.get('https://www.instagram.com/accounts/login/')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_9nyy2")))
driver.find_element(By.NAME, "username").send_keys(login, Keys.F12)
driver.find_element(By.NAME, "password").send_keys(password, Keys.ENTER)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "aOOlW")))
wait()
driver.find_element(By.CLASS_NAME, "aOOlW").click()
print("Zalogowany!")

#-- get pics
driver.get("https://www.instagram.com/explore/tags/" + str(hash))
pictures = driver.find_elements(By.CLASS_NAME, "eLAPa")
pictures[1].click()


while profile != 120:
    loading()
    profile += 1
else:
    driver.quit()





