import numpy as np

class Page:
    def __init__(self, model, distribution):
        self.model = model
        if distribution == 'uniform':
            self.w = np.random.uniform(-1, 1)
        elif distribution == 'normal':
            # return a sample (or samples) from the “standard normal” distribution.
            self.w = np.random.randn() * np.random.choice([1, -1])
        # self.cost = abs(self.w) / self.model.param['PAGE_COST_DENOMINATOR']
        self.visits = 0
        self.age = 0
        self.time_spent = 0

class Platform:
    """ Optimize engagement: number of visitors x time spent
    """
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.model = model
        self.pages = list()
        self.visits = 0
        self.active_users_count = 0
        self.engagement = None
        # self.time_spent = 0
        # self.page_w_threshold = np.random.uniform(-1, 0)
        self.no_of_advertisements = 0

    def regulate_pages(self):
        #Pages replacement
        replace_page_index = np.random.choice(list(range(len(self.pages))))
        self.pages[replace_page_index] = Page(self.model, self.model.param['DISTRIBUTION_INTRINSIC_VALUE'])

    def create_page(self):
        self.pages.append(Page(self.model, self.model.param['DISTRIBUTION_INTRINSIC_VALUE']))

    def update_gains(self):
        page_vists = np.array([page.visits for page in self.pages])
        page_times = np.array([page.time_spent for page in self.pages])
        self.engagement = np.sum(page_vists * page_times)

    def step(self):
        self.update_gains()
        self.regulate_pages()
