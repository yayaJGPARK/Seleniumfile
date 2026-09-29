# Selenium Web Automation Test

Python + Selenium + pytest 기반의 웹 UI 자동화 테스트 프로젝트입니다.

## 1. 프로젝트 목적

Selenium WebDriver와 pytest를 활용하여 웹 서비스의 주요 기능을 자동화 테스트하고, 반복적으로 수행되는 UI 검증을 자동화하는 것을 목적으로 합니다.

주요 테스트 항목:

* 웹 페이지 접속 및 기본 동작 검증
* 웹 Form 입력 검증
* Login 기능 테스트
* Element 탐색 및 상호작용
* 브라우저 동작 검증
* Page Object Model 기반 테스트 구성

## 2. 테스트 환경

| 항목             | 환경                 |
| -------------- | ------------------ |
| Language       | Python 3.14        |
| Test Framework | pytest             |
| Automation     | Selenium WebDriver |
| Browser        | Google Chrome      |
| OS             | Windows / Linux    |
| CI             | GitHub Actions     |

## 3. 프로젝트 구조

```text
Seleniumfile/
├─ pages/
│  └─ test_web_login.py
├─ tests/
│  ├─ test_browser.py
│  └─ test_web_form_input.py
├─ 클로드tests/
│  ├─ test_01.py
│  ├─ test_02.py
│  └─ test_03.py
├─ .github/
│  └─ workflows/
│     └─ selenium.yml
├─ conftest.py
├─ .gitignore
└─ README.md
```

## 4. 테스트 환경 구성

`conftest.py`의 pytest Fixture를 활용하여 테스트에 필요한 Chrome WebDriver를 공통으로 관리합니다.

```python
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    yield driver

    driver.quit()
```

각 테스트 함수 실행 시 새로운 WebDriver를 생성하고 테스트가 종료되면 브라우저를 종료하도록 구성했습니다.

## 5. Chrome 실행 설정

GitHub Actions와 같은 CI 환경에서도 테스트를 실행할 수 있도록 Chrome Headless 환경을 지원합니다.

```python
options = webdriver.ChromeOptions()

options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
```

이를 통해 로컬 환경뿐만 아니라 GUI가 없는 Linux 기반 CI 환경에서도 Selenium 테스트를 실행할 수 있도록 구성했습니다.

## 6. 테스트 실행

프로젝트 루트에서 다음 명령어로 전체 테스트를 실행할 수 있습니다.

```bash
pytest
```

특정 테스트 파일만 실행:

```bash
pytest tests/test_browser.py
```

특정 테스트 디렉터리 실행:

```bash
pytest tests/
```

## 7. 주요 테스트 내용

### Web Form Input

웹 페이지의 Input 요소를 탐색하고 값을 입력한 후 정상적으로 입력되었는지 검증합니다.

### Browser Test

Chrome WebDriver를 이용하여 웹 페이지 접속 및 기본적인 브라우저 동작을 검증합니다.

### Login Test

Login 페이지의 UI 요소를 탐색하고 로그인 관련 동작을 검증합니다.

## 8. Page Object Model

페이지별 요소와 동작을 분리하여 테스트 코드의 유지보수성을 높일 수 있도록 Page Object Model 구조를 적용하고 있습니다.

```text
Test
 ↓
Page Object
 ↓
Web Element
 ↓
Selenium WebDriver
```

페이지 요소 및 동작을 별도의 파일에서 관리함으로써 동일한 요소를 여러 테스트에서 재사용할 수 있도록 구성합니다.

## 9. WebDriver 대기

웹 요소가 동적으로 로딩되는 상황을 고려하여 Selenium의 Explicit Wait를 활용할 수 있도록 구성합니다.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "example")
    )
)
```

고정된 `sleep()` 방식보다 요소의 상태를 기준으로 대기하여 테스트 안정성을 높이는 것을 목표로 합니다.

## 10. GitHub Actions

GitHub Actions를 이용하여 Push 또는 Pull Request 발생 시 Selenium 테스트를 자동으로 실행하도록 구성했습니다.

```text
Git Push
   ↓
GitHub Act
```
