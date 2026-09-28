from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(driver):

    print("===== 로그인 테스트 시작 =====")

    wait = WebDriverWait(driver, 10)

    login_button = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-testid="login-button"]')
        )
    )

    print("===== 로그인 버튼 찾기 성공 =====")

    login_button.click()

    print("===== 로그인 버튼 클릭 성공 =====")