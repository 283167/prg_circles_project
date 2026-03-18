import matplotlib as plt



def euclid_distance(circle_1, circle_2):
    d = ((circle_2["x"] - circle_1["x"]) ** 2 + (circle_2["y"] - circle_1["y"]) ** 2) ** (1/2)
    return d

def radius_sum(circle_1, circle_2):
    return circle_1["r"] + circle_2["r"]

circle_1 = {"x": 0, "y": 0, "r": 2}
circle_2 = {"x": 3, "y": 0, "r": 1}

def has_intersection(d, r):
    result = {}
    if d > r:
        result.update({"intersects": False, "intersections_count": 0})
    elif d.isclose(r):
        result.update({"intersects": True, "intersections_count": 1})
    else:
        result.update({"intersects": True, "intersections_count": 2})