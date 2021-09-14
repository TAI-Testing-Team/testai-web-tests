import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("Bridging the gap between AI use and value | Business Post")
    context.get_all_elements()