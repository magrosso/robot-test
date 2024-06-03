*** Settings ***
Documentation    Test Windows Calculator
Test Tags    math
Library    Application.py
Library    Test.py
Suite Setup    Start Application    start_parameter
Suite Teardown    Stop Application
Test Setup    Init Application
Test Timeout    20 minutes


*** Test Cases ***
Test Addition
    [Documentation]    Verify addition
    [Template]    Test Addition
    num_left=4    num_right=-5    exp_result=-1
    # num_left=90    num_right=-8    exp_result=82
    # num_left=0100    num_right=0    exp_result=100
    # num_left=-9    num_right=92    exp_result=83
    # num_left=698    num_right=92    exp_result=790
    # num_left=3214    num_right=3214    exp_result=6428

Test Subtraction
    [Documentation]    Verify subtraction
    [Template]    Test Subtraction
    9    3    6
    178    1    177
    0    7    -7
    -6    -5    -1
    -6003    1    -6004

Test Multiplication
    [Documentation]    Verify multiplication
    [Template]    Test Multiplication
    1    5    5
    10    5    50
    -1    79    -79
    -41    -79    3239
    0    25    0
    0    0    0
    10000    1    10000

Test Division
    [Documentation]    Verify division
    Test Division


Test Squaring
    Enter Number    2
    Enter Operator   operator=SQUARE
    ${Result}    Get Result    GERMAN
    Should Be Equal    ${Result}    ${4.0}