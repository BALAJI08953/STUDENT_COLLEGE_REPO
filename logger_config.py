import logging


def setup_logger():
    logger = logging.getLogger("student_management")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("student.log")

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger