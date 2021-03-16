# Requirements
**Python**:
 - pytest
 - selenium
 - allure-pytest 
 - allure-python-commons
 
chromedriver (edit **DRIVER_PATH** in test_main.py)


# Usage
**Perform tests:** pytest --alluredir=allure_reports/ .\test_main.py

**View results in Allure:** allure serve .\allure_reports\
