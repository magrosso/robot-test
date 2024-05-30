*** Settings ***
Library    Application.py
Library    Test.py
Suite Setup    Start Application    start_parameter
Suite Teardown    Stop Application
Test Setup    Init Application

*** Test Cases ***
Test Addition
    [Documentation]    Cannot handle thousand separator when entering more than 3 digits!
    Test Addition    4    4
    Test Addition    90    8
    Test Addition    0100    0
    Test Addition    9    92
    Test Addition    698    -92

Test Subtraction
    [Documentation]    Cannot handle thousand separator when entering more than 3 digits!
    Test Subtraction    9    3
    Test Subtraction    178    1
    Test Subtraction    0    7
    Test Subtraction    -6    -5
    
