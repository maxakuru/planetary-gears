from __future__ import annotations

from typing import List
from .calc import calc_gear_ratio, calc_module_with_diameter
from .config import *
from .util import is_between

class Stage:
    def __init__(self, n_planets: int, t_ring: int, t_sun: int, t_planet: int, module: int | float = None, outer_diameter: int | float = None):
        self.n_planets = n_planets
        self.n_teeth_sun = t_sun
        self.n_teeth_planet = t_planet
        self.n_teeth_ring = t_ring

        # may be None, if it's the first stage
        self.module = module
        if self.module is None and outer_diameter is not None:
            self.module = calc_module_with_diameter(outer_diameter, self.n_teeth_ring)
    
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return """
<Stage: 
    n_planets={self.n_planets}
    n_teeth_ring={self.n_teeth_ring}
    n_teeth_sun={self.n_teeth_sun} 
    n_teeth_planet={self.n_teeth_planet} >""".format(self=self)

    def pitch_diameter(self, n_teeth: int = None):
        if n_teeth is None: n_teeth = self.n_teeth_ring
        return n_teeth * self.module

    def outer_diameter(self, n_teeth: int = None):
        return self.pitch_diameter(n_teeth) + 2*self.module

    def get_next_module(self, next_stage: Stage):
        """Calculate module (size) of the next stage

        Args:
            next_stage (Stage): next stage, following self

        Returns:
            number: the module size to use for next stage
        """
        if self.module is None:
            raise Exception("can't calculate next module without current module")

        return self.module * (
            (self.n_teeth_sun + self.n_teeth_planet) / 
            (next_stage.n_teeth_sun + next_stage.n_teeth_planet)
        )

    def is_valid_combine(self, next_stage: Stage):
        """Check whether next stage is compatible with current

        Two stages are compatible if:
        1. same number of planets
        2. next module is above the defined minimum (calculated from self's module)
        3. probably other stuff

        Args:
            next_stage (Stage): next stage

        Returns:
            bool
        """

        return self.n_planets == next_stage.n_planets and self.get_next_module(next_stage) >= min_teeth_module

    def combine_with(self, next_stage: Stage):
        if not self.is_valid_combine(next_stage):
            return False
        return Combo([self, next_stage.with_module(self.get_next_module(next_stage))])

    def with_module(self, module: float | int):
        return Stage(self.n_planets, self.n_teeth_ring, self.n_teeth_sun, self.n_teeth_planet, module, None)

    ### Statics
    @staticmethod
    def is_valid(n_planets: int, t_ring: int, t_sun: int, t_planet: int, outer_diameter: float | int = None, min_module: float | int = min_teeth_module):
        """Check that a stage's parameters are valid 
        (evenly spaced gears, valid number of teeth)
        """
        if not is_between(t_planet, range_teeth_planet): return False
        if not is_between(t_ring, range_teeth_ring): return False
        if not is_between(t_sun, range_teeth_sun): return False
        if not is_between(n_planets, range_num_planets): return False

        expect_teeth_ring = t_sun + (t_planet*2)
        if expect_teeth_ring != t_ring: 
            return False

        expect_whole = (t_sun + t_ring) / n_planets
        mod = expect_whole%1
        # some fudge..
        if mod > 0.01:
            return False
        
        if outer_diameter is None:
            return True
        
        module = calc_module_with_diameter(outer_diameter, t_ring)
        # print('module: ', outer_diameter, t_ring, module)
        return module >= min_teeth_module


class Combo:
    def __init__(self, stages: List[Stage], prev_combo: Combo = None):
        self.ratio = 0
        self.stages = stages

        if prev_combo:
            self.ratio = None # todo
            raise NotImplementedError()
        else:
            [s0, s1] = self.stages[-2:]
            self.ratio = calc_gear_ratio(
                s0.n_teeth_ring, s0.n_teeth_sun, s0.n_teeth_planet, 
                s1.n_teeth_ring, s1.n_teeth_sun, s1.n_teeth_planet
            )

    def combine_with(self, next_stage: Stage):
        last_stage = self.stages[-1]
        if not last_stage.is_valid_combine(next_stage):
            return False
        return Combo([*self.stages, next_stage], self)
        
    def get_csv_line(self):
        d = ''
        for s in self.stages:
            d += '{},{},{},{},'.format(
                s.module, s.n_teeth_ring, s.n_teeth_sun, s.n_teeth_planet)
        if d.endswith(','): d = d[:-1]
        
        return '{},{},{}\n'.format(self.ratio, self.stages[0].n_planets, d)

    ### Statics
    @staticmethod 
    def get_csv_header(num_stages: int):
        common_headers = ["ratio", "N_planets"]
        stage_headers = ["module", "NT_ring", "NT_sun", "NT_planet"]


        inds = list(range(0, num_stages))
        stgs = []
        for i in inds:
            stg = ",".join(['{}{}'.format(h, str(i)) for h in stage_headers])
            stgs.append(stg)
        return "{},{}\n".format(",".join(common_headers), ",".join(stgs))