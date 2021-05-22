

class Advertiser:
    """ Optimize gains from investing in platforms.
        Invest in platforms and collects gains
    """
    # TODO. Use the likes of the page to value
    def __init__(self, model):
        self.model = model
        self.investment_size = self.model.param['N_PAGE_ADVERTISERS_CAN_AFFORD']

    def choose_platform(self):
        # Constrained by self.investment_size
        # First at random
        # Then a function of returns
        # Some new ones at random (innovation)
        pass

    def invest_amount(self):
        pass

    def collect_return(self):
        pass
