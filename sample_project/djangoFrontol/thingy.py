from frontol.apps import FrontolConfig


class MyFrontolConfig(FrontolConfig):
    external_actions = {
        'calculate_receipt': lambda x: print(x)
    }
