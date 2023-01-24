import json
import os
import re
import subprocess
import sys
import urllib

import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect, sync_playwright

load_dotenv("sample.env")

capabilities = {
    'browserName': 'Chrome',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    'browserVersion': 'latest',
    'LT:Options': {
        'platform': 'Windows 10',
        'build': 'Playwright Locators Demo Build',
        'name': 'Playwright Locators Test For Windows 10 & Chrome',
        'user': os.getenv('LT_USERNAME'),
        'accessKey': os.getenv('LT_ACCESS_KEY'),
        'network': True,
        'video': True,
        'visual': True,
        'console': True,
        'tunnel': False,   # Add tunnel configuration if testing locally hosted webpage
        'tunnelName': '',  # Optional
        'geoLocation': '', # country code can be fetched from https://www.lambdatest.com/capabilities-generator/
    }
}


@pytest.fixture(name="local_grid_page")
def playwright_local_grid_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        yield page

@pytest.fixture(name="cloud_grid_page")
def playwright_local_grid_page():    
    with sync_playwright() as playwright:
        playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
        capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion        
        lt_cdp_url = 'wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse.quote(json.dumps(capabilities))    
        browser = playwright.chromium.connect(lt_cdp_url)
        page = browser.new_page()    
        yield page


# replace cloud_grid_page with local_grid_page while running on local
def test_homepage_contains_search_button(cloud_grid_page):
    cloud_grid_page.goto("https://ecommerce-playground.lambdatest.io/")
    search_button_locator = cloud_grid_page.get_by_role(role="button", name="Search")
    expect(search_button_locator).to_have_class("type-text")
        

# replace cloud_grid_page with local_grid_page while running on local
def test_product_details_text_should_be_visible(cloud_grid_page):    
    cloud_grid_page.goto(
        "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&path=57&product_id=28"
    )
    brand_text_locator = cloud_grid_page.get_by_text(text="Brand:", exact=True)
    viewed_text_locator = cloud_grid_page.get_by_text(text="Viewed:", exact=True)
    points_text_locator = cloud_grid_page.get_by_text(text="Reward Points:", exact=True)
    availability_text_locator = cloud_grid_page.get_by_text(text="Availability", exact=True)
    expect(brand_text_locator).to_be_visible()
    expect(viewed_text_locator).to_be_visible()
    expect(points_text_locator).to_be_visible()
    expect(availability_text_locator).not_to_be_visible()


# replace cloud_grid_page with local_grid_page while running on local
def test_product_name_to_appear_more_than_once(cloud_grid_page):    
    cloud_grid_page.goto(
        "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&path=57&product_id=28"
    )
    brand_name_locator = cloud_grid_page.get_by_text(re.compile("htc", re.IGNORECASE))
    expect(brand_name_locator).to_have_count(10)


# replace cloud_grid_page with local_grid_page while running on local
def test_exactly_one_email_and_password_field(cloud_grid_page):    
    cloud_grid_page.goto(
        "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
    )
    email_address_locator = cloud_grid_page.get_by_label(text="E-Mail Address", exact=True)
    password_locator = cloud_grid_page.get_by_label(text="Password", exact=True)
    expect(email_address_locator).to_have_count(1)
    expect(password_locator).to_have_count(1)

# replace cloud_grid_page with local_grid_page while running on local
def test_review_form_has_customername_customerreview_fields(cloud_grid_page):    
    cloud_grid_page.goto(
        "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&path=25&product_id=28"
    )
    name_locator = cloud_grid_page.get_by_placeholder(text="Your Name", exact=True)
    review_locator = cloud_grid_page.get_by_placeholder(text="Your Review", exact=True)
    expect(name_locator).to_have_count(1)
    expect(review_locator).to_have_count(1)

# replace cloud_grid_page with local_grid_page while running on local
def test_logo_with_alt_text_should_be_visible(cloud_grid_page):
    cloud_grid_page.goto(
        "https://ecommerce-playground.lambdatest.io/index.php?route=common/home"
    )
    logo_locator = cloud_grid_page.get_by_alt_text(text="Poco Electro", exact=True).first
    expect(logo_locator).to_be_visible()


# replace cloud_grid_page with local_grid_page while running on local
def test_display_count_of_all_elements_with_title_htc_touch_hd(cloud_grid_page):    
    cloud_grid_page.goto(
        "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&path=18&product_id=28"
    )
    alt_text_locator = cloud_grid_page.get_by_title(text=re.compile("htc touch hd", re.IGNORECASE))
    expect(alt_text_locator).to_have_count(20)

      
# replace cloud_grid_page with local_grid_page while running on local
def test_locator_filter_by_another_locator(cloud_grid_page):
    cloud_grid_page.goto(
        "https://www.lambdatest.com/selenium-playground/"
    )
    base_locator = cloud_grid_page.get_by_role("listitem")
    list_heading_locator = base_locator.filter(
        has=cloud_grid_page.get_by_text(text=re.compile("input form submit", re.IGNORECASE))
        )    
    expect(list_heading_locator).to_have_text('Input Form Submit')

# replace cloud_grid_page with local_grid_page while running on local
def test_locator_filter_by_text(cloud_grid_page):
    cloud_grid_page.goto(
        "https://www.lambdatest.com/selenium-playground/"
    )
    base_locator = cloud_grid_page.get_by_role("listitem")
    table_list_locator = base_locator.filter(
        has_text=re.compile("table", re.IGNORECASE)
        )    
    expect(table_list_locator).to_have_count(5)

# replace cloud_grid_page with local_grid_page while running on local
def test_locator_chaining(cloud_grid_page):    
    cloud_grid_page.goto(
        "https://www.lambdatest.com/selenium-playground/"
    )
    input_form_locator = cloud_grid_page.get_by_role("listitem").get_by_text(text=re.compile("input form submit", re.IGNORECASE))
    expect(input_form_locator).to_have_attribute(name="href", value=re.compile("input-form-demo", re.IGNORECASE))    
