from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def test_browser_open(driver):

    print("===== 테스트 시작 =====")
    print("현재 URL:", driver.current_url)
    print("페이지 제목:", driver.title)

    search_box = driver.find_element(
        By.NAME,
        "q"
    )

    search_box.send_keys("자동화 구축 AI 추천")

    search_box.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.url_contains("search")
    )
    print("현재 URL:", driver.current_url)

    driver.back()

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, "q")
        )
    )
    print("===== 검색창 검수 완료 =====")
#################################################################################

    google_info = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'a[href^="https://about.google/"]'
            )
        )
    )

    google_info.click()

    wait.until(
        EC.url_contains("about.google")
    )
    print("현재 URL:", driver.current_url)

    driver.back()

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, "q")
        )
    )
    print("===== Google 정보 선택 검수완료 =====")
#################################################################################

    google_store = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'a[href^="https://store.google.com/"]'
            )
        )
    )

    google_store.click()

    wait.until(
        EC.url_contains("store.google.com")
    )
    print("현재 URL:", driver.current_url)

    driver.back()

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, "q")
        )
    )
    print("===== 스토어 선택 검수완료 =====")
#################################################################################

    google_email = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'a[href^="https://mail.google.com/"]'
            )
        )
    )

    google_email.click()

    wait.until(
        EC.url_contains("workspace.google.com")
    )
    print("현재 URL:", driver.current_url)

    driver.back()

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, "q")
        )
    )
    print("===== gmail 선택 검수완료 =====")
#################################################################################

    google_image = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'a[href^="https://www.google.com/imghp"]'
            )
        )
    )

    google_image.click()

    wait.until(
        EC.url_contains("https://www.google.com/imghp")
    )
    print("현재 URL:", driver.current_url)

    driver.back()

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, "q")
        )
    )
    print("===== 이미지 선택 검수완료 =====")
 #################################################################################

    google_apps = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'a[aria-label="Google 앱"], a[aria-label="Google apps"]'
            )
        )
    )

    google_apps.click()
    print("===== 구글 앱 검수완료 =====")
#################################################################################

    google_marketing = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'a[href*="/intl/"][href*="/ads/"]', ["google.com/intl/"], ["business.google.com"]
            )
        )
    )

    google_marketing.click()

    wait.until(
        EC.url_contains("https://business.google.com")
    )
    print("현재 URL:", driver.current_url)

    driver.back()

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, "q")
        )
    )
    print("===== 광고 선택 검수완료 =====")
#################################################################################

    google_business = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'a[href^="https://www.google.com/services/"]'
            )
        )
    )

    google_business.click()

    wait.until(
        EC.url_contains("https://business.google.com")
    )
    print("현재 URL:", driver.current_url)

    driver.back()

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, "q")
        )
    )
    print("===== 비즈니스 선택 검수완료 =====")
#################################################################################

    google_searchhow = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'a[href^="https://google.com/search/howsearchworks/"]'
            )
        )
    )

    google_searchhow.click()

    wait.until(
        EC.url_contains("https://www.google.com/search/howsearchworks")
    )
    print("현재 URL:", driver.current_url)

    driver.back()

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, "q")
        )
    )
    print("===== 검색의원리 선택 검수완료 =====")
#################################################################################

    google_privacy = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'a[href^="https://policies.google.com/privacy"]'
            )
        )
    )

    google_privacy.click()

    wait.until(
        EC.url_contains("https://policies.google.com/privacy")
    )
    print("현재 URL:", driver.current_url)

    driver.back()

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, "q")
        )
    )
    print("===== 개인정보처리방침 선택 검수완료 =====")
#################################################################################

    google_terms = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'a[href^="https://policies.google.com/terms"]'
            )
        )
    )

    google_terms.click()

    wait.until(
        EC.url_contains("https://policies.google.com/terms")
    )
    print("현재 URL:", driver.current_url)

    driver.back()

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, "q")
        )
    )
    print("===== 약관 선택 검수완료 =====")
#################################################################################
    google_setting = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//div[contains(text(), "설정") or contains(text(), "Settings")]'
            )
        )
    )

    google_setting.click()
    print("===== 설정 검수완료 =====")
#################################################################################

    print("===== 테스트 종료 =====")