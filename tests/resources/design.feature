import pytest_bdd

Feature: Page design
    As a user,
    I'd like to verify design of pages


    Background:
      Given the user navigates to the website

    Scenario Outline: Verify title at pages
      When the user click on the "<item>"
      Then "UI Testing Site" title will be shown on the "<item>"

      Examples: Item
        | item       |
        | home page  |
        | UI Testing |
        | Form       |
        | Error      |


      Scenario Outline: Verify Company Logo at pages
      When the user click on the "<item>"
      Then "Company Logo" will be shown on each page

      Examples: Item
        | item       |
        | home page  |
        | UI Testing |
        | Form       |
        | Error      |