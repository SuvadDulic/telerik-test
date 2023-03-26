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

        boolean_assert("telerik" in driver.current_url, f"Expected telerik \
        in url, got: {driver.current_url}")

    def test_telerik_demos_url(self, get_telerik_site):
        driver = get_telerik_site

        # driver.fullscreen_window()
        

        # Find demos page link
        demos_link = driver.find_element(By.LINK_TEXT, "DEMOS") 
        # Navigate to demos page
        demos_link.click()

        boolean_assert("demos" in driver.current_url, f"Expected demos in url,\
                         got: {driver.current_url}")

    def test_search_page(self, get_telerik_site):

        driver = get_telerik_site

        # driver.get("https://www.telerik.com/search")
        
        # Find link for search function on site
        search_link = driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-search-wrapper")

        search_link.click()
        # Find header which contains text "Search"
        section = driver.find_element(By.XPATH, \
                            "/html/body/div[2]/div/section[1]/div/div/div/h2")
        # Assert that header reads "Search"
        simple_assert(section.text, "Search")

    def test_search_func(self, get_telerik_site):

        driver = get_telerik_site
        # Find link for search function on site
        search_link = driver.find_element(By.CSS_SELECTOR, \
            "#js-tlrk-nav-search-wrapper")

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

        page_header = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/h1")

        boolean_assert("Load Testing" in page_header.text, f"Expected header to contain Load Testing, got: {page_header.text}")

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

    def test_go_to_pricing_page(self, get_telerik_site):

        driver = get_telerik_site

        pricing_page_link = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/nav/section/div/div[1]/ul[1]/li[5]/a")

        pricing_page_link.click()

        pricing_header = driver.find_element(By.LINK_TEXT, "Pricing")

        simple_assert(pricing_header.text, "Pricing")

    def test_put_in_shopping_cart(self, get_telerik_site):

        driver = get_telerik_site

        pricing_page_link = driver.find_element(By.CSS_SELECTOR, \
        "#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(5) > a")

        pricing_page_link.click()

        footer = driver.find_element(By.XPATH, "/html/body/nav")
        scroll_origin = ScrollOrigin.from_element(footer)
        ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, 450)\
        .perform()

        devcraft_ui_buy_link = driver.find_element(By.XPATH, \
        "/html/body/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/table/thead/tr[5]/th[1]/div/a")

        devc_ui_price_price_page = driver.find_element(By.XPATH, \
        "/html/body/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/table/thead/tr[4]/th[1]/div/h3/span[2]")

        price_text_pricing_page = devc_ui_price_price_page.text

        devcraft_ui_buy_link.click()

        # popup_accept_2 = driver.find_element(By.XPATH, \
        # "/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[2]")

        # popup_accept_2.click()

        devc_ui_price_shopping_page = driver.find_element(By.XPATH, \
        "//*[@id='801']/td[2]/div[1]/span[2]/span")

        boolean_assert(price_text_pricing_page in devc_ui_price_shopping_page.text, \
        f"Expected same price in link text")

    def test_go_to_blogs_page(self, get_telerik_site):

        driver = get_telerik_site

        blogs_link = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/nav/section/div/div[1]/ul[1]/li[3]/a")

        blogs_link.click()

        boolean_assert("blogs" in driver.current_url, f"Expected blogs in url, got: {driver.current_url}")

    def test_first_blog(self, get_telerik_site):

        driver = get_telerik_site

        blogs_link = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/nav/section/div/div[1]/ul[1]/li[3]/a")

        blogs_link.click()

        footer = driver.find_element(By.XPATH, "/html/body/nav")
        scroll_origin = ScrollOrigin.from_element(footer)
        ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, 500)\
        .perform()

        first_blog_link = driver.find_element(By.XPATH, "//*[@id='ContentPlaceholder1_C146_Col00']/div/div[2]/h2/a")

        first_blog_link.click()

        first_blog_header = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div/h1/span")

        boolean_assert("March 2023 Telerik" in first_blog_header.text, \
        f"Expected March 2023 Telerik as header for blog, got: {first_blog_header.text}")

    def test_docs_support_page(self, get_telerik_site):

        driver = get_telerik_site

        docs_supp_link = driver.find_element(By.CSS_SELECTOR, \
            "#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(4) > a")

        docs_supp_link.click()

        boolean_assert("support" in driver.current_url, f"Expected support in url, got: {driver.current_url}")
    
    def test_kendoui_doc(self, get_telerik_site):

        driver = get_telerik_site

        docs_supp_link = driver.find_element(By.CSS_SELECTOR, \
            "#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(4) > a")

        docs_supp_link.click()

        kendo_ui_link = driver.find_element(\
            By.CSS_SELECTOR, \
            "#ContentPlaceholder1_C002_Col00 > div > div > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a")

        kendo_ui_link.click()

        footer = driver.find_element(By.XPATH, "/html/body/nav/section")
        scroll_origin = ScrollOrigin.from_element(footer)
        ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, 600)\
        .perform()

        kendo_ui_doc_link = driver.find_element(By.XPATH, \
            "/html/body/div[2]/section[1]/div/div[1]/div[2]/div[2]/ul/li[1]/a")

        kendo_ui_doc_link.click()

        kendo_ui_doc_header = driver.find_element(By.XPATH, \
            "/html/body/div[3]/div[2]/div/div[2]/div/div/article/h1/a")

        boolean_assert("Kendo" in kendo_ui_doc_header.text, \
            f"Expected Kendo in page header, got: {kendo_ui_doc_header.text}")