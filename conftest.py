import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Choose browser:Chrome or Firefox')
    parser.addoption('--language', action='store', default='en',
                     help='Language preferences')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser')
    language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option(
                'prefs', {'intl.accept_languages': language})
        print('\nStar chrome browser.\n')
        driver = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', language)
        print('\nStart firefox browser.\n')
        driver = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser should be "chrome" or "firefox"')
    yield driver
    print(f'\nQuit {browser_name} browser.')
    driver.quit()
