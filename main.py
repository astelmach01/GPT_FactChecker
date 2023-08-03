import os

import logging
from chatGPT import ChatGPT
from pathlib import Path

ROOT_DIR = Path(os.getcwd()).resolve()


def configure_logging():
    # Create a logger
    logger = logging.getLogger("my_logger")

    # Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.INFO)

    # Create a formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Create a console handler and set the formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    return logger


configure_logging()


def main():
    prompt = input("Enter your prompt:")

    chatGPT = ChatGPT(ROOT_DIR / "util.py")
    print(chatGPT.get_response(prompt))


if __name__ == "__main__":
    main()
