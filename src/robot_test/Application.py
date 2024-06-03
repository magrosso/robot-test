from RPA.core.windows.locators import WindowsElement

import control

root: WindowsElement = None


def start_application(arg: str) -> None:
    """Start application under test"""
    global root
    control.windows_run("Calc.exe")
    root = control.control_window("name:Calculator")
    control.set_global_timeout(timeout=3600)


def stop_application() -> None:
    """Stop application under test"""
    control.close_window(locator=root)


def init_application() -> None:
    """Init application under test"""
    control.click(locator="id:clearButton type:button")
