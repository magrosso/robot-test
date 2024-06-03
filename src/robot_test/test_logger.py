import logging
import logging.config
from pathlib import Path
import json


class TestLogger:
    def __init__(self, name: str) -> None:
        config_file = Path("src/robot_test/logging_config/stdout.json")
        with open(config_file) as f_in:
            config = json.load(f_in)
        logging.config.dictConfig(config)
        self.test_logger = logging.getLogger(name)
