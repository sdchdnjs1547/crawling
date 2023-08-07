from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import urllib.request
import os
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("공유얼굴")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 2.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            a = driver.find_elements(By.CSS_SELECTOR, ".mye4qd").click()
            
        except:
            break
    last_height = new_height

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1

for image in images:
    image.click()
    time.sleep(3)
    image_url = driver.find_element(By.CSS_SELECTOR, ".r48jcc").get_attribute("src")
    urllib.request.urlretrieve(image_url, str(count) + "공유.jpg")
    count += 1


driver.close()