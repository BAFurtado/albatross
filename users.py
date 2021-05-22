import numpy as np


class User:
    pass

    def __init__(self, model):
        self.model = model
        self.intrinsic_value = self.model.param['possible_w_functions'](.5)
        print(np.random.choice(self.intrinsic_value))

    def go_to_page(self):
        pass

    def decision_to_stay(self):
        pass

