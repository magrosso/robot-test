import logging

from logging import Logger
from RPA.Windows import Windows
from RPA.core.windows import WindowsElements
from robot.api.deco import keyword, library


@library(scope="GLOBAL", version="1.0", doc_format="reST")
class Application:
    """Application library"""

    logger: Logger = logging.getLogger("Application Logger")

    rpa: Windows = Windows()

    app_root: WindowsElements = None

    def __init__(self) -> None:
        Application.logger.info("Application init")

    @keyword
    def start_application(self, arg: str):
        """Start application under test"""
        Application.logger.info(f"Start Application with {arg}")
        Application.rpa.windows_run("Calc.exe")

        Application.app_root = Application.rpa.control_window("name:Calculator")

        Application.rpa.set_global_timeout(3600)
        Application.init_application(self)

    @keyword
    def stop_application(self):
        """Stop application under test"""

        Application.logger.info("Stop Application")

        Application.rpa.close_window(locator=Application.app_root)

    @keyword
    def init_application(self):
        """Init application under test"""

        Application.logger.info("Init Application")

        Application.rpa.click(locator="id:clearButton type:button")
