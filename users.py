import numpy as np


class User:
    """ Optimizes their experience. Gain.
    """
    # TODO: Basic behaviour is with increasing engagement level:
    #  1. view (visit) 2. like (signal to the platform) 3. propagate (forcibly include into netword)
    def __init__(self, model):
        self.friends = list()
        self.history = list()
        self.entertainment = 0
        self.model = model
        self.intrinsic_value = self.model.param['possible_preferences_functions']

    def go_to_page(self):
        pass
        # Choose the page
        # 1. Choose randomly if you have 0 options
        # 2. Check your history and choose from there probabilistic
        # 2. Get push/incentive from network
        # 3. It might use number of likes as a signal attractor
        chosen_page = None
        # Calculate the gain from vising the page.
        # If you get more value you may stay longer
        self.entertainment += self.intrinsic_value(chosen_page)
        # Condition on self.entertainment you may like.
        # If you like it, you signal it to the platform
        chosen_page.likes += 1
        # If you love it, you include it (forcibly) into your network
        self.history.append(chosen_page)

    def decision_to_stay(self):
        # Level of threshold of adherence
        pass

    def add_friend(self, friend):
        # Network is static
        self.append(friend)



