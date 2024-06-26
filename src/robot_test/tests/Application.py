from enum import Enum, auto
from RPA.core.windows.locators import WindowsElement

from robot.api.deco import library, keyword

from . import control


class Language(Enum):
    GERMAN = auto()  # noqa: F821
    ENGLISH = auto()


class LocKeys(Enum):
    APP_NAME = auto()
    DISPLAY = auto()
    THOUSAND_SEPARATOR = auto()
    DECIMAL_SEPARATOR = auto()


loc_names: dict[LocKeys, dict[Language, str]] = {
    LocKeys.DISPLAY: {
        Language.GERMAN: "Die Anzeige lautet",
        Language.ENGLISH: "Display is",
    },
    LocKeys.APP_NAME: {Language.GERMAN: "Rechner", Language.ENGLISH: "Calculator"},
    LocKeys.DECIMAL_SEPARATOR: {Language.GERMAN: ",", Language.ENGLISH: "."},
    LocKeys.THOUSAND_SEPARATOR: {Language.GERMAN: ".", Language.ENGLISH: ","},
}

root: WindowsElement = None


@library(scope="GLOBAL", auto_keywords=False)
class Application:
    lang: Language
    region: Language

    def __init__(
        self, lang: Language = Language.ENGLISH, region: Language = Language.ENGLISH
    ) -> None:
        Application.lang = lang
        Application.region = region

    @keyword
    def start_application(self) -> None:
        """Start application under test"""
        global root

        control.windows_run("Calc.exe")
        root = control.control_window(
            f"name:{loc_names[LocKeys.APP_NAME][Application.lang]}"
        )
        control.set_global_timeout(timeout=str(3600))

    @keyword
    def stop_application(self) -> None:
        """Stop application under test"""
        control.close_window(locator=root)

    @keyword
    def init_application(self) -> None:
        """Init application under test"""
        control.click(locator="id:clearButton type:button")
