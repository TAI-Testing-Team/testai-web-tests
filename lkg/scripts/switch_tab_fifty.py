import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("50 of the Best DevOps Podcasts - Security Boulevard")
    context.get_all_elements()