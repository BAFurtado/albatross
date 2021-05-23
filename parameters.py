import numpy as np

# GENERAL
N_USERS = 10
N_PLATFORMS = 2
N_ADVERTISERS = 3
N_PAGE_ADVERTISERS_CAN_AFFORD = 10
DISTRIBUTION_INTRINSIC_VALUE = 'uniform'
# DISTRIBUTION_INTRINSIC_VALUE = 'normal'

SEED = 0

# PLATFORMS
# Number to divide absolute page value
PAGE_COST_DENOMINATOR = 10

# TODO. Test different distributions


def possible_preferences_functions():
    # Some possible rules. We'll need more rules
    a = lambda x: x ** 2
    b = lambda x: -x
    c = lambda x: x
    # d = 1 / value
    return (a, b, c)#, d
