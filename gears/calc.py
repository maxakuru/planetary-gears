"""Functions for calculating gear things and stuff
"""

from __future__ import annotations


def calc_gear_ratio(
    teeth_ring_one: int, 
    teeth_sun_one: int,
    teeth_planet_one: int, 
    teeth_ring_two: int,
    teeth_sun_two: int,
    teeth_planet_two: int):
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


def calc_module_with_diameter(outer_diameter: int | float, num_teeth: int):
    """An estimated module, mostly for spur gears

    Args:
        outer_diameter (number): outside diameter (tip of tooth)
        num_teeth (integer): number of teeth

    Returns:
        number: module
    """
    # PD = M * Z
    # OD = 2M + PD, assumes square area of tooth
    # so, M = OD/2Z

    return outer_diameter / (2*num_teeth)

def calc_pitch_diameter(num_teeth: int, module: int | float):
    return num_teeth * module

def calc_outside_diameter(pitch_diameter: int | float, module: int | float):
    return pitch_diameter + 2*module