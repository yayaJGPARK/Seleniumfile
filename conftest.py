"""
conftest.py
- Selenium + pytest 공통 설정
"""

import pytest
from selenium import webdriver

BASE_URL = "https://www.google.com/"

@pytest.fixture(scope="function")
def driver():
    """
    각 테스트 함수마다 새로운 Chrome WebDriver를 생성하고
    테스트가 끝나면 Chrome을 종료한다.
    """
    print("시작 해보자고")

    # Chrome 브라우저 실행
    driver = webdriver.Chrome()

    driver.get(BASE_URL)

    # 테스트 코드에 driver 전달
    yield driver

    print("종료 할꺼임")

    # 테스트 종료 후 Chrome 종료
    driver.quit()