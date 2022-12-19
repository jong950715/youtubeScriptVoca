import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from definitions import getRootDir
from selenium.webdriver.common.by import By

_url = 'http://m.endic.naver.com/search.nhn?searchOption=entryIdiom&query=' + 'like'
crawl_api = "크롤할 api"

options = webdriver.ChromeOptions()

# headless 옵션 설정
#options.add_argument('headless')
options.add_argument("no-sandbox")

# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
#options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# 드라이버 생성
driver = webdriver.Chrome(options=options)

driver.get(_url)
driver.implicitly_wait(3000)
soup = BeautifulSoup(driver.page_source, 'html.parser')
ps = soup.select_one('div.component_keyword.has-saving-function div.row').select('li.mean_item')

for p in ps:
    print(p.text.replace("\n","").replace('\t',""))
