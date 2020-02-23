Feature: Form
    As the user,
    I'd like to verify the form functionality


    Background:
      Given the user navigates to the website

    Scenario: Verify visibility form elements
      When the user click at the "Form" button
      Then the user should see active input field at the page
      And the user is able to click the submit button

    Scenario: Send the form with filled input field
      When the user click at the "Form" button
      And the user type input field
      And the user click "Go" button
      Then the user should redirect to the Hello page
      And the user should see hello text contains user name

    Scenario: Send the form with empty input field
      When the user click at the "Form" button
      And the user leave the input field empty
      And the user click "Go" button
      Then the user should redirect to the Hello page
      And the user should see hello text without user name

    Scenario: Send the form with double name separate spaces inside input field
      When the user click at the "Form" button
      And the user type in input field double name with spaces
      And the user click "Go" button
      Then the user should redirect to the Hello page
      And the user should see hello text with correct user name

    Scenario: Send the form with specific letters from other alphabets inside input field
      When the user click at the "Form" button
      And the user type in input field specific letters from other alphabets
      And the user click "Go" button
      Then the user should redirect to the Hello page
      And the user should see hello text with correct user name


    Scenario: Send the form with spaces before inside input field
      When the user click at the "Form" button
      And the user type in input field user name followed by spaces
      And the user click "Go" button
      Then the user should redirect to the Hello page
      And the user should see hello text with correct user name without extra symbols
