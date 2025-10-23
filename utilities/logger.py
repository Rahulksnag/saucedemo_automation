import logging

def get_logger():
    logging.basicConfig(
        filename="./reports/test_log.log",
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    return logging.getLogger()
