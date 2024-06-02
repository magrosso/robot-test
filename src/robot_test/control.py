import logging

from RPA.core.windows.locators import WindowsElement
from RPA.Windows import Windows

import test_logger

test_logger.setup_logging()

win = Windows()
win.logger.setLevel(logging.WARN)

logger = logging.getLogger(__name__)


def print_tree():
    logger.info("print_tree()")
    win.print_tree()


def set_global_timeout(timeout: str):
    win.set_global_timeout(timeout=timeout)
    logger.info(f"set_global_timeout({timeout=})")


def windows_run(text: str) -> None:
    logger.info(f"windows_run({text=})")
    win.windows_run(text=text)


def close_window(locator: str) -> None:
    logger.info(f"close_window({locator=})")
    win.close_window(locator=locator)


def get_attribute(locator: str, attribute: str) -> str:
    logger.info(f"get_attribute({locator=}, {attribute=})")
    return win.get_attribute(locator, attribute)


def get_element(locator: str) -> WindowsElement:
    logger.info(f"get_element({locator=})")
    return win.get_element(locator=locator)


def control_window(locator: str) -> WindowsElement:
    logger.info(f"control_window({locator=})")
    return win.control_window(locator=locator)


def click(locator: str):
    logger.info(f"click({locator=})")
    win.click(locator=locator)
