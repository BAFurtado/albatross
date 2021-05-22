import numpy as np


class Page:
    def __init__(self, model, distribution):
        self.model = model
        if distribution == 'uniform':
            self.preferences = np.random.uniform(-1, 1)
        elif distribution == 'normal':
            # return a sample (or samples) from the “standard normal” distribution.
            self.preferences = np.random.randn() * np.random.choice([1, -1])
        self.cost = abs(self.preferences) / self.model.param['PAGE_COST_DENOMINATOR']

class Platform:
    """ Optimize engagement: number of visitors x time spent
    """
    def __init__(self, model):
        self.model = model
        self.pages = list()
        self.page_maintenance = None

    def create_page(self):
        self.pages.append(Page(self.model, self.model.param['DISTRIBUTION_INTRINSIC_VALUE']))

    def update_gains(self):
        # Get your pages return in terms number of users * time
        pass

    def pay_investors(self):
        pass
