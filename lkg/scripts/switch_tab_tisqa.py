
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("TISQA takeaways: Why testers need AI, more for QA pros | TechBeacon")
    context.get_all_elements()