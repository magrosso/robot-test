import logging

# from RPA.Windows.keywords import ActionKeywords as action
# from RPA.Windows.keywords import ElementKeywords as elem
# from RPA.Windows.keywords import WindowKeywords as win
from RPA.Windows.keywords.window import WindowsElement
# import RPA.Windows.keywords.window as win
# from RPA.Windows.keywords import LocatorKeywords as loc
# from RPA.core.windows.locators import WindowsElement

from RPA.Windows import Windows

win = Windows()

logger = logging.getLogger(f"{__name__} Logger")


def set_global_timeout(timeout: float):
    win.set_global_timeout(timeout=timeout)


def windows_run(text: str) -> None:
    win.windows_run(text=text)


def close_window(locator: str) -> None:
    win.close_window(locator=locator)


def get_attribute(locator: str, attribute: str) -> str:
    return win.get_attribute(locator, attribute)


def get_element(locator: str) -> WindowsElement:
    return win.get_element(locator=locator)


def control_window(locator: str) -> WindowsElement:
    return win.control_window(locator=locator)


def click(locator: str):
    win.click(locator=locator)
