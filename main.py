import parameters as params
import networkx as nx
import numpy as np

import analysis

from users import User
from platforms import Platform
from advertisers import Advertiser

from mesa import Model
from schedule import RandomActivationByBreed

class AdEconomyModel(Model):
    def __init__(self, param):
        self.seed = np.random.RandomState(param['SEED'])
        self.param = param
        self.agents = list()
        self.platforms = list()
        self.advertisers = list()
        # Create agents

        for i in range(param['N_USERS']):
            self.agents.append(User(unique_id = i, model = self))

        for j in range(param['N_PLATFORMS']):
            p = Platform(unique_id = j, model = self)
            p.create_page()
            self.platforms.append(p)

        for k in range(param['N_ADVERTISERS']):
            self.advertisers.append(Advertiser(self))

        # Random network
        for agent in self.agents:
            if np.random.random() > .5:
                pass

        # TODO. Make the network a typical small world network

    def step(self):
        # AGENTS
        # For each agent, agents may pass or act
        # Decide on pages to visit
        # Visit pages
        # Random
        # Depends on their network
        # Have visited in the past
        # Gets reward

        # PLATFORMS
        # Collect numbers pass on to advertisers

        # ADVERTISERS
        # Get results.
        # Decide on maintenance or new pages
        pass
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
    m1 = Model(prs)
