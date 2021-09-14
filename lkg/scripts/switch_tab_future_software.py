import logging
import time
#-*- coding: utf-8 -*-

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("The Future of Software Testing with AI: An Interview with Jason Arbon | StickyMinds")
    context.get_all_elements()