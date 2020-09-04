from typing import List


def solution(paths: List[List[str]]) -> str:
    destenations = set()
    for path in paths:
        destenations.add(path[0])
    for path in paths:
        if path[1] not in destenations:
            return path[1]
    return ''