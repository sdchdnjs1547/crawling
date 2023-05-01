from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request

# 크롬 드라이버 경로
driver_path = 'chromedriver.exe'

# 크롬 드라이버 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless')  # 화면 표시하지 않음
options.add_argument('--disable-gpu')  # GPU 사용 안 함
options.add_argument('--no-sandbox')  # Sandbox 모드 비활성화
options.add_argument('--disable-dev-shm-usage')  # 공유 메모리 사용 안 함

# 크롬 드라이버 실행 및 구글 이미지 검색 페이지 접속
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get('https://www.google.com/imghp')

# 검색어 입력
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('손흥민')
search_box.send_keys(Keys.ENTER)

# 검색 결과 중 첫 번째 이미지 클릭
image = driver.find_element(By.CSS_SELECTOR, '.rg_i')
image.click()

# 이미지 URL 가져오기
image_url = driver.find_element(By.CSS_SELECTOR, '.n3VNCb').get_attribute('src')

# 이미지 다운로드
urllib.request.urlretrieve(image_url, 'son_heung_min.jpg')

# 드라이버 종료
driver.quit()
