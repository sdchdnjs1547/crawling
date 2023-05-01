from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import urllib.request
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("손흥민")
elem.send_keys(Keys.RETURN)

image = driver.find_element(By.CSS_SELECTOR, '.rg_i')
image.click()
time.sleep(10)
image_url = driver.find_element(By.CSS_SELECTOR, '.n3VNCb').get_attribute('src')
urllib.request.urlretrieve(image_url, "test.jpg")


# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()