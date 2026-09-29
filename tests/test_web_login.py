from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def test_login(driver):
    print("===== 테스트 시작 =====")
    print("현재 URL:", driver.current_url)
    print("페이지 제목:", driver.title)
    print("===== 로그인 테스트 시작 =====")

    wait = WebDriverWait(driver, 10)

    login_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'a[href^="https://accounts.google.com/ServiceLogin"]'
            )
        )
    )
    login_button.click()

    print("===== 로그인 버튼 클릭 성공 =====")
###############################################
    email_box = driver.find_element(
        By.NAME,
        "identifier"
    )

    email_box.send_keys("jegun1009@gmail.com")

    email_box.send_keys(Keys.ENTER)
    print("===== 이메일 입력 성공 =====")
###############################################
    try:
        password_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.NAME, "Passwd")
            )
        )

        password_box.send_keys("비밀번호")
        password_box.send_keys(Keys.ENTER)

        print("===== 비밀번호 입력 성공 =====")


    except Exception as e:

        print("\n================================")

        print("❌ 비밀번호 입력 단계 실패")

        print("================================")

        print("현재 URL:", driver.current_url)

        print("페이지 제목:", driver.title)

        print("실패 원인:", type(e).__name__)

        print("상세 내용:", e)

        print("================================\n")