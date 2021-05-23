import numpy as np

class Advertiser:
    """ Optimize gains from investing in platforms.
        Invest in platforms and collects gains
    """
    # TODO. Use the likes of the page to value
    def __init__(self, model):
        self.model = model
        self.investment_size = self.model.param['N_PAGE_ADVERTISERS_CAN_AFFORD']

    def choose_n_platforms(self):
        current_platforms = model.platforms.copy()
        platform_engagements = [platform.engagement for platform in current_platforms]
        for platform_index in np.argsort(platform_engagements)[-8:]:
            current_platforms[platform_index].no_of_advertisements += 1



    def invest_amount(self):
        pass

    def collect_return(self):
        pass
