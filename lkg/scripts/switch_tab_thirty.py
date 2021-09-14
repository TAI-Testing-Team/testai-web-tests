
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("33 test automation leaders to follow in 2019 | TechBeacon")
    context.get_all_elements()