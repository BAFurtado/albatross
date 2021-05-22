import numpy as np


N_AGENTS = 10
N_PLATFORMS = 2
DISTRIBUTION_INTRINSIC_VALUE = 'uniform'
# DISTRIBUTION_INTRINSIC_VALUE = 'normal'

SEED = 0

# TODO. Test different distributions


def possible_w_functions(value):
    # Some possible rules. We'll need more rules
    a = value ** 2
    b = 1 / value
    c = -value
    d = value
    return a, b, c, d



