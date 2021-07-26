"""Calculates gear ratio sets

Only applicable to split-ring planetary gearboxes with first stage being
driven by the sun gear and output captured from last stage's outer ring.

Inspo/refs:
https://www.sdp-si.com/resources/elements-of-metric-gear-technology/page4.php
https://www.youtube.com/watch?v=5a1w9daIybc&ab_channel=GearDownForWhat%3F (great channel!)
http://www.thecatalystis.com/gears/
https://juangg-projects.blogspot.com/2018/02/split-ring-compound-epicyclicplanetary.html
"""

import itertools
from typing import List
from datetime import datetime
from pathlib import Path
from gears.stage import Combo, Stage
from gears.config import *

def main():
    csv_str = Combo.get_csv_header(2)

    options_set = [
        range(*range_teeth_ring), 
        range(*range_teeth_sun), 
        range(*range_teeth_planet)
    ]
    option_permutations = list(itertools.product(*options_set))

    for n_planets in range(*range_num_planets):
        valid_stages = all_valid_stages(option_permutations, n_planets)
        for stageOne in valid_stages:
            for stageTwo in valid_stages:
                combo = stageOne.combine_with(stageTwo)
                if not combo:
                    continue
                csv_str += combo.get_csv_line()

    output_dir = "./output/"
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    csv_path = "{}{}.csv".format(output_dir, datetime.now())
    csv_file = open(csv_path, "w")
    csv_file.write(csv_str)
    csv_file.close()


def all_valid_stages(op_perms: List[int], n_planets: int) -> List[Stage]:
    """Get all valid stages for N planets as a list
    
    Args:
        op_perms: list of stage config permutations
        n_planets: number of planets

    Returns:
        Stage[]: list of stages
    """
    valid_stages = []
    for t_ring, t_sun, t_planet in op_perms:
        if Stage.is_valid(n_planets, t_ring, t_sun, t_planet, req_outer_diameter):
            valid_stages.append(Stage(n_planets, t_ring, t_sun, t_planet, None, req_outer_diameter))

    return valid_stages

if __name__ == "__main__":
    main()