import logging
import control

logger = logging.getLogger(f"{__name__} Logger")


def test_addition(num_left: int, num_right: int, exp_result: int) -> None:
    """Addition Test"""
    logger.info(f"{__name__}({num_left}, {num_right})")
    if not _enter_number(num_left):
        raise ValueError
    control.click(locator="id:plusButton type:button")
    if not _enter_number(num_right):
        raise ValueError
    control.click(locator="id:equalButton type:button")
    result: int = _get_result()
    if result != exp_result:
        raise AssertionError(f"{result} != {exp_result}")


def test_subtraction(num_left: int, num_right: int, exp_result: int) -> None:
    """Subtraction Test"""
    logger.info(f"{__name__}({num_left}, {num_right})")
    if not _enter_number(num_left):
        raise ValueError
    control.click(locator="id:minusButton type:button")
    if not _enter_number(num_right):
        raise ValueError
    control.click(locator="id:equalButton type:button")
    result: int = _get_result()
    if result != exp_result:
        raise AssertionError(f"{result} != {exp_result}")


def test_multiplication(num_left: int, num_right: int, exp_result: int) -> None:
    """Multiplication Test

    Args:
        num_left (int): _description_
        num_right (int): _description_
        exp_result (int): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_
        AssertionError: _description_
    """
    logger.info(f"{__name__}({num_left}, {num_right})")
    if not _enter_number(num_left):
        raise ValueError
    control.click(locator="id:multiplyButton type:button")
    if not _enter_number(num_right):
        raise ValueError
    control.click(locator="id:equalButton type:button")
    result: int = _get_result()
    if result != exp_result:
        raise AssertionError(f"{result} != {exp_result}")


def test_fail(arg: str) -> None:
    """Failure test"""
    logger.info(f"Called: {__name__}({arg})")
    raise AssertionError


def _get_result() -> int:
    result_display: str = control.get_attribute(
        locator="id:CalculatorResults", attribute="Name"
    )
    logger.info(f'Result: "{result_display}"')
    val: str = result_display.removeprefix("Display is ")
    # remove thousand separator
    return int(val.replace(".", ""))


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
