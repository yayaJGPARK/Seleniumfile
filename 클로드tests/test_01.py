import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

FOOTER_LINKS = [
    ("Google 정보", 'a[href^="https://about.google/"]',           "about.google"),
    ("스토어",      'a[href^="https://store.google.com/"]',       "store.google.com"),
    ("이미지",      'a[href^="https://www.google.com/imghp"]',    "/imghp"),
    ("개인정보",    'a[href^="https://policies.google.com/privacy"]', "policies.google.com/privacy"),
    ("약관",        'a[href^="https://policies.google.com/terms"]',   "policies.google.com/terms"),
]


def wait_for_home(driver, wait):
    wait.until(EC.presence_of_element_located((By.NAME, "q")))


def test_search(driver):
    wait = WebDriverWait(driver, 10)
    box = driver.find_element(By.NAME, "q")
    box.send_keys("자동화 구축 AI 추천", Keys.ENTER)
    wait.until(EC.url_contains("/search"))
    assert "q=" in driver.current_url
    driver.back()
    wait_for_home(driver, wait)


@pytest.mark.parametrize("name, selector, expected", FOOTER_LINKS)
def test_link_navigation(driver, name, selector, expected):
    wait = WebDriverWait(driver, 10)
    link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    link.click()
    wait.until(EC.url_contains(expected))
    assert expected in driver.current_url, f"{name} 이동 실패: {driver.current_url}"
    driver.back()
    wait_for_home(driver, wait)