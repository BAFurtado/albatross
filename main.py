import parameters as params
import networkx as nx
import numpy as np

import analysis

from users import User
from platforms import Platform
from advertisers import Advertiser

from mesa import Model
from schedule import RandomActivationByBreed

class AlbatrossModel(Model):
    def __init__(self, param):
        self.seed = np.random.RandomState(param['SEED'])
        self.param = param
        self.users = list()
        self.platforms = list()
        self.advertisers = list()
        self.schedule = RandomActivationByBreed(self)

        for i in range(param['N_USERS']):
            new_user = User(unique_id = i, model = self)
            self.users.append(new_user)
            self.schedule.add(new_user)

        for j in range(param['N_PLATFORMS']):
            new_platform = Platform(unique_id = j, model = self)
            for m in range(param['PAGES_PER_PLATFORM']):
                new_platform.create_page()
            self.platforms.append(new_platform)
            self.schedule.add(new_platform)

        for k in range(param['N_ADVERTISERS']):
            new_advertiser = Advertiser(unique_id = k, model = self)
            self.advertisers.append(new_advertiser)
            self.schedule.add(new_advertiser)

        # Random network
        for agent in self.users:
            if np.random.random() > .5:
                pass

        # TODO. Make the network a typical small world network

    def step(self):
        self.schedule.step()
    # Outputs
    # Which pattern are you going to use to "validate".
    # TODO: find pattern to replicate
    # Observe evolution of


def to_dict_from_module():
    return {k: getattr(params, k) for k in dir(params) if not k.startswith('_')}


if __name__ == '__main__':
    #Things to decide:
    # 1. Which scheduler to use?
    #       1. Is there an ordinality to the agent function calls?
    #               1. How does t = 0 "REALLY" look like?

    prs = to_dict_from_module()
    # TODO include scenarios.
    m1 = AlbatrossModel(prs)
    m1.step()
