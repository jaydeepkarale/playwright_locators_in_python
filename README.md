# Playwright Locators In Python

The purpose of this repository is to demonstrate Playwright Locators. Playwright is a browser automation & web testing framework which enables reliable end-to-end testing for modern web apps.

# Version Check
The required libraries necessary to run this code are

python==3.12.4

pytest==8.2.2

playwright==1.44.0


# Setup & Installation
Python installation remains standard and is out of scope

To install the recommended Playwright, Pytest & pytest-playwright use requirements.txt file provided with this repo
```pip install -r requirements.txt```

Alternatively you can also use the command
```pip install pytest-playwright```

# Username & Accesskey for running tests on LambdaTest cloud grid
In order to run the tests on cloud grid you will need to create an account and obtain the username & access key from the [LambdaTest Account Settings Page](https://accounts.lambdatest.com/security)

Once obtained this needs to be updated in the ```.env``` file 

# Running All The Tests
1. Clone the repository
2. Install the dependencies mentioned above
3. Run the command ```pytest -v test_playwright_locators.py ```

# Running Individual Tests
1. Clone the repository
2. Install the dependencies mentioned above
3. Run the command ```pytest -v -k test_playwright_locators.py::<name_of_individual_test> ```
