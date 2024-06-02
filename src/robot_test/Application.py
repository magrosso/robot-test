import logging

from RPA.core.windows.locators import WindowsElement
from robot.api.deco import keyword

import control


class Application:
    """Application library"""

    def __init__(self) -> None:
        self.app_root: WindowsElement = None

    @keyword
    def start_application(self, arg: str):
        """Start application under test"""
        control.windows_run("Calc.exe")
        self.app_root = control.control_window("name:Calculator")
        control.set_global_timeout(timeout=3600)

    @keyword
    def stop_application(self):
        """Stop application under test"""
        control.close_window(locator=self.app_root)

    @keyword
    def init_application(self):
        """Init application under test"""
        control.click(locator="id:clearButton type:button")
