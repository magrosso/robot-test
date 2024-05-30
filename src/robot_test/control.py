import logging
# from robot.api.logger import logging

logger = logging.getLogger(f"{__name__} Logger")


def control_get_element() -> None:
    logger.info(f"{__name__} called")


def control_click_element():
    logger.warn(f"{__name__} called")
