import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

HOME_URL = "https://www.google.com"

# (이름, 클릭할 링크 CSS 셀렉터, 이동 후 URL에 포함되어야 할 문자열들 - 하나라도 만족하면 통과)
LINK_CASES = [
    ("Google 정보", 'a[href^="https://about.google/"]', ["about.google"]),
    ("스토어", 'a[href^="https://store.google.com/"]', ["store.google.com"]),
    # Gmail은 지역/로그인 상태에 따라 도착 URL이 달라질 수 있어 여러 후보 허용
    ("Gmail", 'a[href^="https://mail.google.com/"]',
     ["workspace.google.com", "mail.google.com", "accounts.google.com"]),
    ("이미지", 'a[href^="https://www.google.com/imghp"]', ["/imghp"]),
    # 광고와 비즈니스는 서로 다른 버튼이지만 도착 URL은 동일
    ("광고", 'a[href*="/intl/"][href*="/ads/"]', ["google.com/intl/"], ["business.google.com"]),
    ("비즈니스", 'a[href^="https://www.google.com/services/"]', ["business.google.com"]),
    ("개인정보처리방침", 'a[href^="https://policies.google.com/privacy"]',
     ["policies.google.com/privacy"]),
    ("약관", 'a[href^="https://policies.google.com/terms"]',
     ["policies.google.com/terms"]),
]


@pytest.fixture(autouse=True)
def go_home(driver):
    """각 테스트를 항상 구글 홈에서 시작 (driver fixture는 기존 것을 사용)"""
    driver.get(HOME_URL)


def wait_for_home(driver, wait):
    wait.until(EC.url_contains("google.com"))
    wait.until(EC.presence_of_element_located((By.NAME, "q")))


def test_search(driver):
    wait = WebDriverWait(driver, 10)
    print("현재 URL:", driver.current_url)
    print("페이지 제목:", driver.title)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("자동화 구축 AI 추천", Keys.ENTER)

    wait.until(EC.url_contains("/search"))
    assert "q=" in driver.current_url, f"검색 URL 이상: {driver.current_url}"
    print("현재 URL:", driver.current_url)

    driver.back()
    wait_for_home(driver, wait)
    print("===== 검색창 검수 완료 =====")


@pytest.mark.parametrize("name, selector, expected_list", LINK_CASES,
                         ids=[c[0] for c in LINK_CASES])
def test_link_navigation(driver, name, selector, expected_list):
    wait = WebDriverWait(driver, 10)

    link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    link.click()

    wait.until(EC.any_of(*[EC.url_contains(e) for e in expected_list]))
    current = driver.current_url
    print("현재 URL:", current)
    assert any(e in current for e in expected_list), \
        f"{name} 이동 실패: {current}"

    driver.back()
    wait_for_home(driver, wait)
    print(f"===== {name} 선택 검수완료 =====")


def test_google_apps(driver):
    wait = WebDriverWait(driver, 10)

    apps = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a[aria-label="Google 앱"], a[aria-label="Google apps"]')))
    apps.click()

    # 앱 메뉴는 iframe으로 열리므로 실제로 열렸는지 확인
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'iframe[src*="widget/app"]')))
    print("===== 구글 앱 검수완료 =====")


def test_settings(driver):
    wait = WebDriverWait(driver, 10)

    setting = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[contains(text(), "설정") or contains(text(), "Settings")]')))
    setting.click()

    # 설정 메뉴가 열렸는지 확인 (예: 검색 설정 링크 노출)
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'a[href*="/preferences"]')))
    print("===== 설정 검수완료 =====")