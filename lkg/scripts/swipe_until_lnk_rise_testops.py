import logging
import time
import os

log = logging.getLogger(__name__)

MAX_SWIPES = 10


def run(context):
    sign_up = False
    attempts = 0

    sign_up = element_exists(context, 'lnk_rise_testops')
    
    while not sign_up and attempts <= MAX_SWIPES:
        attempts += 1
        context.perform_gesture('swipe_up', '')
        sign_up = element_exists(context, 'lnk_rise_testops')

    context.verify(['lnk_rise_testops'])


def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0
