from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

# Constants
# -----------------------------------------------------------------------------------------------------------------------------------------------
TELERIK_SITE = "https://www.telerik.com/"

# Asserts
# -----------------------------------------------------------------------------------------------------------------------------------------------
def simple_assert(gotten_val, expected_val):
    assert gotten_val == expected_val, f"Assertion failed, expected: {expected_val}, got: {gotten_val}"


def boolean_assert(value, message):
    assert value, message

# Tests
# ----------------------------------------------------------------------------------

class TestClass:

    # Setup and Teardown for the whole test class
    # scope defines which tests a single invocation of the fixture will apply for
    @pytest.fixture(scope="class")
    def load_driver(self):
        
        # Selenium 4.6 and above use a BETA version of Selenium Manager which automatically handles the browser drivers
        # If we have an older version, or if Selenium Managers somehow does not work on your system, follow this guide for installing the correct driver:
        # https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

        driver = webdriver.Chrome()
        driver.maximize_window()

        # NOT THE BEST SOLUTION BUT USE IT AS A PLACEHOLDER
        # WARNING: THIS DOES NOT WORK WITH EXPLICIT WAIT
        driver.implicitly_wait(10)

        yield driver

        print('RUN CLASS TEARDOWN')

        driver.quit()
    

    # Setup and Teardown for every single test
    @pytest.fixture
    def get_telerik_site(self, load_driver):

        driver = load_driver

        # Load iceberry website
        driver.get(TELERIK_SITE)

        yield driver

        print('RUN TEST TEARDOWN')

        driver.delete_all_cookies()

    def test_telerik_url(self, get_telerik_site):
        # Load Selenium webdriver
        driver = get_telerik_site

        boolean_assert("telerik" in driver.current_url, f"Expected telerik in url, got: {driver.current_url}")

    def test_telerik_demos_url(self, get_telerik_site):
        driver = get_telerik_site

        # driver.fullscreen_window()
        

        # Find demos page link
        demos_link = driver.find_element(By.LINK_TEXT, "DEMOS") 
        # Navigate to demos page
        demos_link.click()

        boolean_assert("demos" in driver.current_url, f"Expected demos in url, got: {driver.current_url}")

    def test_telerik_search(self, get_telerik_site):

        driver = get_telerik_site
        # Set the browser window on fullscreen mode
        # driver.fullscreen_window()
        # Find link for search function on site
        search_link = driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-search-wrapper")
        # Go to search page on telerik website
        search_link.click()
        # Assert that search is part of the search page url 
        boolean_assert("search" in driver.current_url, f"Expected search in url, got: {driver.current_url}")
        # # Find header which contains text "Search"
        # section = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div/div/div/h2")
        # # Assert that header reads "Search"
        # simple_assert(section.text, "Searc")

    def test_search_page(self, get_telerik_site):

        driver = get_telerik_site

        driver.get("https://www.telerik.com/search")

        # driver.fullscreen_window()
        # # Find link for search function on site
        # search_link = driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-search-wrapper")

        # search_link.click()

        section = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div/div/div/h2")

        simple_assert(section.text, "Search")

    def test_search_func(self, get_telerik_site):

        driver = get_telerik_site
        # Find link for search function on site
        search_link = driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-search-wrapper")

        search_link.click()

        search_field = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div/div/div/tk-site-search/div/div/input")

        # popup_accept = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/button[2]")

        # popup_accept.click()

        search_field.send_keys("load testing")

        click_search = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div/div/div/tk-site-search/div/button")

        click_search.click()

        first_search_result = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[2]/div/div/div[3]/ul/li[1]/h4/a/b")

        simple_assert(first_search_result.text, "Load Testing")

    def test_link_from_search(self, get_telerik_site):

        driver = get_telerik_site

        search_link = driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-search-wrapper")

        search_link.click()

        search_field = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div/div/div/tk-site-search/div/div/input")

        search_field.send_keys("load testing")

        click_search = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div/div/div/tk-site-search/div/button")

        click_search.click()

        first_search_result = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[2]/div/div/div[3]/ul/li[1]/h4/a/b")

        first_search_result.click()

        boolean_assert("load-testing" in driver.current_url, f"Expected load-testing in url, got: {driver.current_url}")

    def test_more_about_devcraft(self, get_telerik_site):

        driver = get_telerik_site

        devcraft_link = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div/div[2]/a")

        devcraft_link.click()

        boolean_assert("devcraft" in driver.current_url, f"Expected devcraft in url, got: {driver.current_url}")

    def test_contact_us_page(self, get_telerik_site):

        driver = get_telerik_site

        contact_us_link = driver.find_element(By.XPATH, "/html/body/div[2]/footer/div/div[1]/div[2]/div[1]/div[4]/ul/li[1]/a")

        contact_us_link.click()
        
        boolean_assert("contact" in driver.current_url, f"Expected contact in url, got: {driver.current_url}")


    

        