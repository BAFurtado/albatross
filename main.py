import parameters as params
import networkx as nx
import numpy as np

from users import User
from platforms import Platform


class Model:
    def __init__(self, param):
        self.seed = np.random.RandomState(param['SEED'])
        self.param = param
        self.agents = list()
        self.platforms = list()
        # Create agents

        for i in range(param['N_AGENTS']):
            self.agents.append(User(self))

        for j in range(param['N_PLATFORMS']):
            p = Platform(self)
            p.create_page()
            self.platforms.append(p)

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

        pass
    # Outputs


def to_dict_from_module():
    return {k: getattr(params, k) for k in dir(params) if not k.startswith('_')}


if __name__ == '__main__':
    prs = to_dict_from_module()
    m1 = Model(prs)
