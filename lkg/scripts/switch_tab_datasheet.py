#!/usr/bin/python
#-*- coding: utf-8 -*-

import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("Platform Data Sheet")
    context.get_all_elements()