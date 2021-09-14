'''
This script allows you to put focuse on a specific browser tap.
Useful for verification of links that open in a new browser tab by default.
Replace <your tab title> below.
'''

import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("Test AI - YouTube")
    context.get_all_elements()
