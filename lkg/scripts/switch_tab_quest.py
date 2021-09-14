
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("The Quest for Quality in AI - TechCentral.ie")
    context.get_all_elements()