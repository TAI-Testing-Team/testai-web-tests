
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("Test automation tools: Top trends and challenges for 2020 | TechBeacon")
    context.get_all_elements()