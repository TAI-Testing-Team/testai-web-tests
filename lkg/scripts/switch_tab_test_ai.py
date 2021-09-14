
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("Test.ai Raises $11M Series A To Test Every App In The World")
    context.get_all_elements()