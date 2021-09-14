import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("testai_DataSheet_v4.0.pdf")
    context.get_all_elements()