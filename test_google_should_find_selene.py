import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def browser_size():
    browser.open('https://google.com')
    browser.driver.set_window_size(1280, 960)

def test_google(browser_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_not_found(browser_size):
    browser.element('[name="q"]').should(be.blank).type('cvf7657567867876978987978085675464567567').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))