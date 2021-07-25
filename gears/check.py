
def check_stage(teeth_ring, teeth_sun, teeth_planet, num_planets):
    """Check that a stage's parameters are valid 
    (evenly spaced gears, valid number of teeth)

    Args:
        teeth_ring (integer): num teeth in ring
        teeth_sun (integer): num teeth in sun
        teeth_planet (integer): num teeth in each planet
        num_planets (integer): num planets

    Returns:
        boolean: whether it is a valid configuration or not
    """

    # print('teeth_ring: ', teeth_ring)
    # print('teeth_sun: ', teeth_sun)
    # print('teeth_planet: ', teeth_planet)
    # print('num_planets: ', num_planets)

    if teeth_planet < 4: return False
    if teeth_ring < 4: return False
    if teeth_sun < 4: return False
    if num_planets < 1: return False

    expect_teeth_ring = teeth_sun + (teeth_planet*2)
    # print('expect_teeth_ring: ', expect_teeth_ring)
    if expect_teeth_ring != teeth_ring: 
        return False


    expect_whole = (teeth_sun + teeth_ring) / num_planets
    # print('expect_whole: ', expect_whole)
    return float(expect_whole).is_integer()

