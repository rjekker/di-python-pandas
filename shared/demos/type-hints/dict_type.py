from typing import Dict, List, Any


def max_avg(d: Dict[Any, List[float]]) -> float:
    return max([sum(l)/len(l) for l in d.values()])
