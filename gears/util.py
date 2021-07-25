import math

def range_around(goal_val, spread, min_val = 0, max_val = math.inf):
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