import numpy as np


class User:
    """ Optimizes their experience. Gain.
    """
    def __init__(self, model):
        self.friends = list()
        self.history = list()
        self.entertainment = 0
        self.model = model
        self.intrinsic_value = self.model.param['possible_w_functions']

    def go_to_page(self):
        pass
        # Choose the page
        # 1. Choose randomly if you have 0 options
        # 2. Check your history and choose from there probabilistic
        # 2. Get push/incentive from network
        # 3.
        page_value = None
        # Calculate the gain from vising the page.
        # If you get more value you may stay longer
        self.entertainment += self.intrinsic_value(page_value)

    def decision_to_stay(self):
        # Level of threshold of adherence
        pass

    def add_friend(self, friend):
        self.append(friend)

