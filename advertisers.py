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
        current_platforms = self.model.platforms.copy()
        platform_engagements = [platform.engagement for platform in current_platforms]
        top_platforms = np.argsort(platform_engagements)
        for platform_index in top_platforms[-8:]:
            current_platforms[platform_index].no_of_advertisements += 1
            # del current_platforms[platform_index]
        number_of_innovations = 2
        current_platforms = np.array(current_platforms)
        for platform in np.random.choice(current_platforms[top_platforms[:-8]], number_of_innovations):
            platform.no_of_advertisements += 1

    def invest_amount(self):
        pass

    def collect_return(self):
        pass

    def step(self):
        self.choose_n_platforms()
