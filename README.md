# python_playwright_locators

The purpose of this repository is to demonstrate Playwright Locators. Playwright is a browser automation & web testing framework which enables reliable end-to-end testing for modern web apps.

# Version Check
The required libraries necessary to run this code are
python==3.9.12
pytest==7.2.1
playwright==1.29.1
pytest-playwright

# Setup & Installation
Python installation remains standard and is out of scope

To install the recommended Playwright, Pytest & pytest-playwright use the single command below

```pip install pytest-playwright```

# Username & Accesskey for running tests on LambdaTest cloud grid
In order to run the tests on cloud grid you will need to create an account and obtain the username & access key from the [LambdaTest Profile Page](https://accounts.lambdatest.com/detail/profile)

Once obtained this needs to be updated in the ```sample.env``` file

# Running All The Tests
1. Clone the repository
2. Install the dependencies mentioned above
3. Fire the command ```pytest -v test_playwright_locators.py ```

# Running Individual Tests
1. Clone the repository
2. Install the dependencies mentioned above
3. Fire the command ```pytest -v test_playwright_locators.py::<name_of_individual_test> ```
