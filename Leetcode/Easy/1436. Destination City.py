from typing import List

"""
We need to find out the city which doesn't have a path outgoing to another city.
We can do that by creating a set of all cities which do have a path outgoing from them.
After that we can iterate through the list again and check which city isn't in our set as that is the city which doesn't have an outgoing path
then we simply return it
"""


def solution(paths: List[List[str]]) -> str:
    destinations = set()
    for path in paths:
        destinations.add(path[0])
    for path in paths:
        if path[1] not in destinations:
            return path[1]
    return ''