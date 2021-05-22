import numpy as np


class Page:
    def __init__(self, distribution):
        if distribution == 'uniform':
            self.w = np.random.uniform(-1, 1)
        elif distribution == 'normal':
            # return a sample (or samples) from the “standard normal” distribution.
            self.w = np.random.randn() * np.random.choice([1, -1])


class Platform:
    def __init__(self, model):
        self.model = model
        self.pages = list()

    def create_page(self):
        self.pages.append(Page(self.model.param['DISTRIBUTION_INTRINSIC_VALUE']))
