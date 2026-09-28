from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_web_form(driver):

    wait = WebDriverWait(driver, 10)

    # 1. Text 입력
    text_box = wait.until(
        EC.visibility_of_element_located((By.NAME, "my-text"))
    )
    text_box.send_keys("Hello Selenium")

    input("Text 입력 확인 → Enter를 누르면 다음 단계")

    # 2. Password 입력
    password = wait.until(
        EC.visibility_of_element_located((By.NAME, "my-password"))
    )
    password.send_keys("1234")

    input("Password 입력 확인 → Enter를 누르면 다음 단계")

    # 3. Checkbox 선택
    checkbox = wait.until(
        EC.element_to_be_clickable((By.ID, "my-check-1"))
    )
    checkbox.click()

    input("Checkbox 선택 확인 → Enter를 누르면 다음 단계")

    # 4. Radio button 선택
    radio = wait.until(
        EC.element_to_be_clickable((By.ID, "my-radio-2"))
    )
    radio.click()

    input("Radio 선택 확인 → Enter를 누르면 다음 단계")

    # 5. Dropdown 선택
    dropdown_element = wait.until(
        EC.visibility_of_element_located((By.NAME, "my-select"))
    )

    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Two")

    input("Dropdown 선택 확인 → Enter를 누르면 다음 단계")

    # 6. Submit 버튼 클릭
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
    )
    button.click()

    input("Submit 클릭 확인 → Enter를 누르면 결과 확인")

    # 7. 결과 확인
    message = wait.until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert message.text == "Received!"

    print("테스트 성공!")