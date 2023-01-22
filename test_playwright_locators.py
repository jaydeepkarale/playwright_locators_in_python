import json
import logging
import sys
import re

from logging import getLogger

from playwright.sync_api import sync_playwright, expect

# setup basic loggig for our project which will display the time, log level & log message
logger = getLogger("getbyroledemo")
logging.basicConfig(
    stream=sys.stdout,
    format="%(message)s",
    level=logging.DEBUG,
)


def test_homepage_contains_search_button():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://ecommerce-playground.lambdatest.io/")
        search_button_locator = page.get_by_role(role="button", name="Search")
        expect(search_button_locator).to_have_class("type-text")
        
        
def test_product_details_text_should_be_visible():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=product/product&path=57&product_id=28"
        )
        brand_text_locator = page.get_by_text(text="Brand:", exact=True)
        viewed_text_locator = page.get_by_text(text="Viewed:", exact=True)
        points_text_locator = page.get_by_text(text="Reward Points:", exact=True)
        availability_text_locator = page.get_by_text(text="Availability", exact=True)
        expect(brand_text_locator).to_be_visible()
        expect(viewed_text_locator).to_be_visible()
        expect(points_text_locator).to_be_visible()
        expect(availability_text_locator).not_to_be_visible()

def test_product_name_to_appear_more_than_once():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=product/product&path=57&product_id=28"
        )
        brand_name_locator = page.get_by_text(re.compile("htc", re.IGNORECASE))
        expect(brand_name_locator).to_have_count(10)

def test_exactly_one_email_and_password_field():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(
            "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
        )
        email_address_locator = page.get_by_label(text="E-Mail Address", exact=True)
        password_locator = page.get_by_label(text="Password", exact=True)
        expect(email_address_locator).to_have_count(1)
        expect(password_locator).to_have_count(1)


def test_review_form_has_customername_customerreview_fields():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(
            "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&path=25&product_id=28"
        )
        name_locator = page.get_by_placeholder(text="Your Name", exact=True)
        review_locator = page.get_by_placeholder(text="Your Review", exact=True)
        expect(name_locator).to_have_count(1)
        expect(review_locator).to_have_count(1)

def test_logo_with_alt_text_should_be_visible():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(
            "https://ecommerce-playground.lambdatest.io/index.php?route=common/home"
        )
        logo_locator = page.get_by_alt_text(text="Poco Electro", exact=True).first
        expect(logo_locator).to_be_visible()            

def test_display_count_of_all_elements_with_title_htc_touch_hd():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(
            "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&path=18&product_id=28"
        )
        alt_text_locator = page.get_by_title(text=re.compile("htc touch hd", re.IGNORECASE))
        expect(alt_text_locator).to_have_count(20)
         

def test_locator_filter_by_another_locator():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(
            "https://www.lambdatest.com/selenium-playground/"
        )
        base_locator = page.get_by_role("listitem")        
        list_heading_locator = base_locator.filter(
            has=page.get_by_text(text=re.compile("input form submit", re.IGNORECASE))
            )    
        expect(list_heading_locator).to_have_text('Input Form Submit')

def test_locator_filter_by_text():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(
            "https://www.lambdatest.com/selenium-playground/"
        )
        base_locator = page.get_by_role("listitem")
        table_list_locator = base_locator.filter(
            has_text=re.compile("table", re.IGNORECASE)
            )    
        expect(table_list_locator).to_have_count(5)

def test_locator_chaining():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(
            "https://www.lambdatest.com/selenium-playground/"
        )
        input_form_locator = page.get_by_role("listitem").get_by_text(text=re.compile("input form submit", re.IGNORECASE))
        expect(input_form_locator).to_have_attribute(name="href", value=re.compile("input-form-demo", re.IGNORECASE))
