# LANGAGE: Python

def distance(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    return (dx * dx + dy * dy) ** 0.5


def clamp(val, min_val, max_val):
    return max(min_val, min(max_val, val))