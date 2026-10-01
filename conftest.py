"""
conftest.py
- Selenium + pytest 공통 설정
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://www.google.com/"


@pytest.fixture(scope="function")
def driver():
    """
    각 테스트 함수마다 새로운 Chrome WebDriver를 생성하고
    테스트가 끝나면 Chrome을 종료한다.
    """

    print("시작 해보자고")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Chrome 브라우저 실행
    driver = webdriver.Chrome(options=options)

    driver.get(BASE_URL)

    yield driver

    print("종료 할꺼임")

    driver.quit()