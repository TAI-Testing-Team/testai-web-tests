
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("202: AI for User Flow Verification with Jason Arbon")
    context.get_all_elements()