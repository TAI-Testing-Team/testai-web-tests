
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("AI in software testing has arrived. Here's why robots rule.")
    context.get_all_elements()