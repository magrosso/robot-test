import logging
import control

logger = logging.getLogger(f"{__name__} Logger")


def test_addition(num_left: int, num_right: int):
    """Addition Test"""
    logger.info(f"{__name__}({num_left}, {num_right})")
    if not _enter_number(num_left):
        raise ValueError
    control.click(locator="id:plusButton type:button")
    if not _enter_number(num_right):
        raise ValueError
    control.click(locator="id:equalButton type:button")
    result: int = _get_result()
    if result != num_left + num_right:
        raise AssertionError(f"{num_left} + {num_right} != {result}")


def test_subtraction(num_left: int, num_right: int):
    """Subtraction Test"""
    logger.info(f"{__name__}({num_left}, {num_right})")
    if not _enter_number(num_left):
        raise ValueError
    control.click(locator="id:minusButton type:button")
    if not _enter_number(num_right):
        raise ValueError
    control.click(locator="id:equalButton type:button")
    result: int = _get_result()
    if result != num_left - num_right:
        raise AssertionError(f"{num_left} - {num_right} != {result}")


def test_fail(arg: str):
    """Failure test"""
    logger.info(f"Called: {__name__}({arg})")
    raise AssertionError


def _get_result() -> int:
    result_display: str = control.get_attribute(
        locator="id:CalculatorResults", attribute="Name"
    )
    logger.info(f'Result: "{result_display}"')
    return int(result_display.removeprefix("Display is "))


def _enter_number(num: int) -> bool:
    try:
        num_str = str(num)
    except ValueError:
        return False

    is_negative = False
    for pos, digit in enumerate(num_str):
        if digit.isdigit():
            control.click(locator=f"id:num{digit}Button type:button")
        elif digit == ".":
            control.click(locator="id:decimalSeparatorButton type:button")
        elif pos == 0 and digit == "-":
            is_negative = True
        else:
            return False
    if is_negative:
        control.click(locator="id:negateButton type:button")

    return True
