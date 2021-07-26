import math
from typing import Tuple

def range_around(goal_val: int, spread: int, min_val: int = 0, max_val: int = math.inf):
    """Get a range near a goal value

    Args:
        goal_val (number): mid point value for range
        spread (number): number on either side to add/subtract from mid point
        min_val (number, optional): lowest acceptable lower bound. Defaults to 0.
        max_val (number, optional): highest acceptable upper bound. Defaults to math.inf.

    Returns:
        (number, number): lower, upper tuple
    """
    lower = max(min_val, goal_val - spread)
    upper = min(max_val, goal_val + spread)
    return (lower, upper)

def is_between(num: int, range: Tuple[int, int]):
    return range[0] <= num <= range[1]