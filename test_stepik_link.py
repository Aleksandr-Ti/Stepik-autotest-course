from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, id):
    link = f"https://stepik.org/lesson/{id}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector(".ember-text-area").send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission").click()
    text = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert text == "Correct!"
