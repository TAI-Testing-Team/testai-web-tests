
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("Will AI and Machine Learning Take Over Software Testing?: An Interview with Jason Arbon | CMCrossroads")
    context.get_all_elements()