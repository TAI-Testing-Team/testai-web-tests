
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("Moving up the testing leadership ladder: 3 lessons learned | TechBeacon")
    context.get_all_elements()