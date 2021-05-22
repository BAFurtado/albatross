import numpy as np

# GENERAL
N_AGENTS = 10
N_PLATFORMS = 2
DISTRIBUTION_INTRINSIC_VALUE = 'uniform'
# DISTRIBUTION_INTRINSIC_VALUE = 'normal'

SEED = 0

# PLATFORMS
# Number to divide absolute page value
PAGE_COST_DENOMINATOR = 10

# TODO. Test different distributions


def possible_preferences_functions(value):
    # Some possible rules. We'll need more rules
    a = value ** 2
    b = 1 / value
    c = -value
    d = value
    return a, b, c, d



