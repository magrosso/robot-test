*** Settings ***
Test Tags    math
Library    Application.py
Library    Test.py
# Library    control.py
Suite Setup    Start Application    start_parameter
Suite Teardown    Stop Application
Test Setup    Init Application

*** Test Cases ***
Test Addition
    [Documentation]    Verify addition
    Test Addition    4    4    8
    Test Addition    90    8    98
    Test Addition    0100    0    100
    Test Addition    9    92    101
    Test Addition    698    -92    606
    Test Addition    3214    3214    6428

Test Subtraction
    [Documentation]    Verify subtraction
    Test Subtraction    9    3    6
    Test Subtraction    178    1    177
    Test Subtraction    0    7    -7
    Test Subtraction    -6    -5    -1
    Test Subtraction    -6003    1    -6004

Test Multiplication
    [Documentation]    Verify multiplication
    Test Multiplication    1    5    5
    Test Multiplication    10    5    50
    Test Multiplication    -1    79    -79
    Test Multiplication    -41    -79    3239
    Test Multiplication    0    25    0
    Test Multiplication    0    0    0
    Test Multiplication    10000    1    10000

