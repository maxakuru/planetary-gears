"""Calculates gear ratio sets

Heavily inspired by:
https://www.youtube.com/watch?v=5a1w9daIybc&ab_channel=GearDownForWhat%3F
http://www.thecatalystis.com/gears/
"""

import itertools
from gears.util import range_around
from gears.check import check_stage
from gears.calc import calc_gear_ratio

# TODO: calc module sizes, rank outputs

# ==== Constraints ====
# == Both Stages ==
req_num_planets = 3 # both stages use same number of planets
## == First stage ==
req_teeth_ring_one = 42
req_teeth_sun_one = 18
req_teeth_planet_one = 12
req_module_one = 1 # module size


range_teeth_ring_two = range_around(req_teeth_ring_one, 10, 4, 72)
range_teeth_sun_two = range_around(req_teeth_sun_one, 10, 4, 62)
range_teeth_planet_two = range_around(req_teeth_planet_one, 10, 4, 42)

# first check the first stage requirements
valid = check_stage(req_teeth_ring_one, req_teeth_sun_one, req_teeth_planet_one, req_num_planets)
if not valid: 
    print("First stage is invalid.")
    exit(1)

# [ t_ring[], t_sun[], t_planet[] ]
options_set = [
    range(*range_teeth_ring_two), 
    range(*range_teeth_sun_two), 
    range(*range_teeth_planet_two)
]

permus = list(itertools.product(*options_set))
valid_permus = []

for t_ring_two, t_sun_two, t_planet_two in permus:
    valid = check_stage(t_ring_two, t_sun_two, t_planet_two, req_num_planets)
    if valid:
        # TODO: rank the permutation based on goal parameters
        print('got valid stage: ')
        print('     ring teeth: ', t_ring_two)
        print('     sun teeth: ', t_sun_two)
        print('     planet teeth: ', t_planet_two)

        ratio = calc_gear_ratio(req_teeth_ring_one, req_teeth_sun_one, req_teeth_planet_one, t_ring_two, t_sun_two, t_planet_two)
        print('     ratio: ', ratio)

        valid_permus.append([t_ring_two, t_sun_two, t_planet_two, ratio])

# print("Valid permutations: ", valid_permus)