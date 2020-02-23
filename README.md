# docler_test_task_python

Automation testing for this project were implemented using Python programming language due to it's my main language for development. It includes gherkin scripts, test cases written using Page Object pattern, pages (methods for different pages), CI integration with Circle CI and Jenkins tools (config files at the project root) and Allure reporting

# Integration with Circle CI
[![CircleCI](https://circleci.com/gh/vitaliisotnichenko/docler_test_task_python.svg?style=svg)](https://circleci.com/gh/vitaliisotnichenko/docler_test_task_python)

When you click on this badge you will redirect to. the CircleCI website. There you have a chance click last build and explore all occurences on different stages building the project and tests

# Allure Reports
Below I've attached some reporting using probably the best reporting tool Allure
There we can see that only 17 test cases passed (77 %) and 5 test cases were failed (basically bugs related to Form page)

![Image alt](https://github.com/vitaliisotnichenko/python-web-qa/raw/master/Allure_graphs.png)


# Project structure
1. src/pages - contains files with pageobjects methods (base_page, error_page, form_page, home_page)
2. tests/resources - contains files written in gherkin format - design.feature,form.feature
3. tests/tests_docler_test_task.py - filt with test cases written using PageObject Pattern
It includes paramterize tests and mark by different groups
4. Conftest.py in the root of the project - contains fixture (it's analog of Before and After methods). In particular, it initialize the browser before each test and quit from the browser after each test)
5. global_scope.py - contains CONSTANTS
6. Jenkinsfile - file in groovy-dsl format to integrate with CI Jenkins tool
7. requirements.txt - contains all libraries needed for our project (pytest, webdriver-manager, selenium, requests, allure)
8. .circleci directory contains config file which helps to run out test automation framework in the cloud (CircleCI).
It consist of different stages:
- spin up environment
- preparaing env variables
- checkout code
- install dependencies
- run high priority test cases
- run moderate priority test cases
- run low priority test cases
- install Allure CLI
- generate report
- uploading artifacts

# Run the project
1. git clone repository
2. make sure that python3 installed on the server
3. create isolated virtual environment using command - python3 -m venv venv
4. activate virtual environment - . venv/bin/activate
5. install dependencies - pip install -r requirements.txt
6. run test cases with high priority and save results to allure directory - python3 -m pytest tests/tests_docler_test_task.py -m high -v --alluredir ~/repo/raw_test_result_jsons
7. run test cases with moderate priority and save results to allure directory - python3 -m pytest tests/tests_docler_test_task.py -m moderate -v --alluredir ~/repo/raw_test_result_jsons
8. run test cases with low priority and save results to allure directory - python3 -m pytest tests/tests_docler_test_task.py -m moderate -v --alluredir ~/repo/raw_test_result_jsons


