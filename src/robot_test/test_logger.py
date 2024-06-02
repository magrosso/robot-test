import logging
import logging.config
from pathlib import Path
import json

"D:\sw-dev\python\robot-test\src\robot_test\logging_config\stdout.json"


def setup_logging() -> None:
    # cwd = Path.cwd()
    config_file = Path("src/robot_test/logging_config/stdout.json")
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)
