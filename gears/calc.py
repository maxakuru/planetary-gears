"""Functions for calculating gear things and stuff
"""

def calc_gear_ratio(
    teeth_ring_one, 
    teeth_sun_one,
    teeth_planet_one, 
    teeth_ring_two,
    teeth_sun_two,
    teeth_planet_two):
    """Calculate the gear ratio of a two stage gearbox

    Args:
        teeth_ring_one (integer): num teeth in first ring
        teeth_sun_one (integer): num teeth in first sun
        teeth_planet_one (integer): num teeth in first planet
        teeth_ring_two (integer): num teeth in second ring
        teeth_sun_two (integer): num teeth in second sun
        teeth_planet_two (integer): num teeth in second planet

    Returns:
        number: the combined gear ratio
    """
    ring_to_planet_one = teeth_ring_one / teeth_planet_one
    ring_and_sun_one = teeth_ring_one + teeth_sun_one
    ratio = (((teeth_ring_two - (ring_to_planet_one * teeth_planet_two)) / teeth_ring_two) * (teeth_sun_one / ring_and_sun_one))
    
    if ratio == 0: 
        return 0

    return 1 / ratio

def calc_module_two(module_one, teeth_sun_one, teeth_planet_one, teeth_sun_two, teeth_planet_two):
    """Calculate module (size) of the second stage

    Args:
        module_one (integer): module size of first stage
        teeth_sun_one (integer): num teeth in first stage sun
        teeth_planet_one (integer): num teeth in each first stage planet
        teeth_sun_two (integer): num teeth in second stage sun
        teeth_planet_two (integer): num teeth in each second stage planet

    Returns:
        number: the module size to use for second stage
    """
    return module_one * (teeth_sun_one + teeth_planet_one) / (teeth_sun_two + teeth_planet_two)