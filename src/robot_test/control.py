import logging


# import RPA.Windows.keywords.ActionKeywords as action
# import RPA.Windows.keywords.ElementKeywords as elem
# import RPA.Windows.keywords.WindowKeywords as win
# import RPA.Windows.keywords.LocatorKeywords as loc
# from RPA.Windows.keywords.window import WindowKeywords

# import RPA.Windows.keywords.window

from RPA.core.windows.locators import WindowsElement
from RPA.Windows import Windows

win = Windows()

logger = logging.getLogger(f"{__name__} Logger")


def print_tree():
    win.print_tree()


def set_global_timeout(timeout: str):
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
