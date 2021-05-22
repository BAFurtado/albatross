import parameters as params
from users import User
from platforms import Platform


class Model:
    def __init__(self, param):
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




    def step(self):
        pass

    # Outputs


def to_dict_from_module():
    return {k: getattr(params, k) for k in dir(params) if not k.startswith('_')}


if __name__ == '__main__':
    prs = to_dict_from_module()
    m1 = Model(prs)
