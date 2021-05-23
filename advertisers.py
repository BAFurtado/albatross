import numpy as np

class Advertiser:
    """ Optimize gains from investing in platforms.
        Invest in platforms and collects gains
    """
    # TODO. Use the likes of the page to value
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.model = model
        self.investment_size = self.model.param['N_PAGE_ADVERTISERS_CAN_AFFORD']

    def choose_n_platforms(self):
        current_platforms = model.platforms.copy()
        platform_engagements = [platform.engagement for platform in current_platforms]
        for platform_index in np.argsort(platform_engagements)[-8:]:
            current_platforms[platform_index].no_of_advertisements += 1
            del current_platforms[platform_index]
        number_of_innovations = 2
        for platform in np.random.choice(current_platforms, number_of_innovations):
            platform.no_of_advertisements += 1

    def invest_amount(self):
        pass

    def collect_return(self):
        pass

    def step(self):
        print("Ad step")
        self.choose_n_platforms()
