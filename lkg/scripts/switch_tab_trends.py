
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("Top trends: 5 ways AI will change software testing | TechBeacon")
    context.get_all_elements()