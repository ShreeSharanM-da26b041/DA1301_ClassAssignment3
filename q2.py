from typing import List


def surviving_ships(ships: List[int]) -> List[int]:
    """
    Problem 2: Spaceship collisions.

    Given a list of ship engine powers (sign = direction: positive is
    right, negative is left), resolve all collisions between ships
    moving toward each other and return the engine powers (with sign)
    of the ships that remain.

    Args:
        ships: list of signed engine powers.

    Returns:
        List of signed engine powers of surviving ships, left to right.
    """
    l = []
    for i in ships:
        alive = True
        while alive and l and i<0 and l[-1]>0:
            if l[-1]<abs(i):
                l.pop()
            elif l[-1]==abs(i):
                l.pop()
                alive=False
            else:
                alive=False
        if alive:
            l.append(i)
    return l
    pass


if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8, -8]))     # expected: []
