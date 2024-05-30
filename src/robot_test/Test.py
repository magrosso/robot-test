import logging
# from typing import Optional, Union

from robot.api.deco import keyword, library

# from RPA.Windows import Windows
from Application import Application


@library(scope="GLOBAL", version="1.0", doc_format="reST")
class Test:
    """my lib"""

    def __init__(self) -> None:
        Application.logger.info("Test lib init")

    @keyword
    def test_addition(self, num_left: int, num_right: int):
        """Addition Test"""
        # Application.logger.info(f'test_addition()')
        # Application.rpa.click(locator='id:clearButton type:button')

        if not self._enter_number(num_left):
            raise ValueError
        Application.rpa.click(locator="id:plusButton type:button")
        if not self._enter_number(num_right):
            raise ValueError
        Application.rpa.click(locator="id:equalButton type:button")

        if self._get_result() != num_left + num_right:
            raise AssertionError

    @keyword
    def test_subtraction(self, num_left: int, num_right: int):
        """Subtraction Test"""
        if not self._enter_number(num_left):
            raise ValueError
        Application.rpa.click(locator="id:minusButton type:button")
        if not self._enter_number(num_right):
            raise ValueError
        Application.rpa.click(locator="id:equalButton type:button")

        if self._get_result() != num_left - num_right:
            raise AssertionError

    @keyword
    def test_fail(self, arg: str):
        """Failure test"""
        Application.logger.info(f"called: my_fail_function({arg})")
        raise AssertionError

    def _get_result(self) -> int:
        result_display: str = Application.rpa.get_attribute(
            locator="id:CalculatorResults", attribute="Name"
        )
        Application.logger.info(f'Result: "{result_display}"')
        return int(result_display.removeprefix("Display is "))

    def _enter_number(self, num: int) -> bool:
        try:
            num_str = str(num)
        except ValueError:
            return False

        is_negative = False
        for pos, digit in enumerate(num_str):
            if digit.isdigit():
                Application.rpa.click(locator=f"id:num{digit}Button type:button")
            elif digit == ".":
                Application.rpa.click(locator="id:decimalSeparatorButton type:button")
            elif pos == 0 and digit == "-":
                is_negative = True
            else:
                return False
        if is_negative:
            Application.rpa.click(locator="id:negateButton type:button")

        return True
