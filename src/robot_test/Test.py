import logging
import control
from enum import Enum, auto

logger = logging.getLogger(f"{__name__} Logger")


class Display(Enum):
    GERMAN = auto()
    ENGLISH = auto()


def test_addition(num_left: int, num_right: int, exp_result: int) -> None:
    """Addition Test"""
    logger.info(f"{__name__}({num_left}, {num_right})")
    if not _enter_number(num_left):
        raise ValueError
    control.click(locator="id:plusButton type:button")
    if not _enter_number(num_right):
        raise ValueError
    control.click(locator="id:equalButton type:button")
    result: float = _get_result(display=Display.GERMAN)
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
    result: float = _get_result(display=Display.GERMAN)
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
    result: float = _get_result(display=Display.GERMAN)
    if result != exp_result:
        raise AssertionError(f"{result} != {exp_result}")


def test_division() -> None:
    """Division Test

    Args:
        num_left (int): _description_
        num_right (int): _description_
        exp_result (int): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_
        AssertionError: _description_
    """
    test_params: tuple[tuple[int, int, float], ...] = (
        (1, 2, 0.5),
        (10, 2, 5),
        (0, 2, 0),
        (102, 2, 51),
    )
    for num_left, num_right, exp_result in test_params:
        logger.info(f"{__name__}({num_left}, {num_right})")
        if not _enter_number(num_left):
            raise ValueError
        control.click(locator="id:divideButton type:button")
        if not _enter_number(num_right):
            raise ValueError
        control.click(locator="id:equalButton type:button")
        result: float = _get_result(display=Display.GERMAN)
        if result != exp_result:
            raise AssertionError(f"{result} != {exp_result}")


def _get_result(display: Display) -> float:
    val: str = _get_result_as_string()
    if display == Display.GERMAN:
        thousand_sep = "."
        decimal_sep = ","
        val = val.replace(thousand_sep, "").replace(decimal_sep, ".")
    elif display == Display.ENGLISH:
        thousand_sep = ","
        val = val.replace(thousand_sep, "")
    # remove thousand separator
    return float(val)


def _get_result_as_string() -> str:
    result_display: str = control.get_attribute(
        locator="id:CalculatorResults", attribute="Name"
    )
    logger.info(f'Result Display: "{result_display}"')
    return result_display.removeprefix("Display is ")


def _enter_number(num: float) -> bool:
    try:
        num_str = str(num)
    except ValueError:
        return False

    decimal_separator = "."  # a decimla point denotes a decimal number
    minus_sign = "-"  # a leading - denotes a negative number
    plus_sign = "+"  # a leading + denotes a positive number

    number_sign = num_str[0]
    signed: bool = number_sign in (minus_sign, plus_sign)

    for digit in num_str[1 if signed else 0 :]:
        if digit.isdigit():
            control.click(locator=f"id:num{digit}Button type:button")
        elif digit == decimal_separator:
            control.click(locator="id:decimalSeparatorButton type:button")
        else:
            return False
    if signed and number_sign == minus_sign:
        control.click(locator="id:negateButton type:button")

    return True
