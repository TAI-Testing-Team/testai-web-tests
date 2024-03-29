import logging
import time

log = logging.getLogger(__name__)


def run(context):
    try:
        if element_exists(context, 'div_test_ai_news'):

            # The scripting API supports hybrid element detection mode.
            # In this particular case, default element detection is not sufficient as there is a nested WebView.
            # Using enable_image_mode we can instruct the test.ai system to use AI to detect elements on the screen.
            context.enable_image_mode()

            context.perform_gesture('swipe_up', '')
            context.perform_gesture('tap', 'lnk_intro_image')
            context.perform_gesture('tap', 'lnk_test_ai_raises_image')
            context.perform_gesture('tap', 'lnk_two_image')
            context.perform_gesture('tap', 'lnk_art_int_software_image')
            context.perform_gesture('tap', 'lnk_becoming_image')
            context.perform_gesture('tap', 'lnk_future_software_image')
            
    finally:
        context.disable_image_mode()
        context.get_all_elements()


def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0