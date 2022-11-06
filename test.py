from point2d import Point2d

if __name__ == "__main__":
    point1 = Point2d()
    point2 = Point2d()
    point1.set()
    assert point1.get() == "Current point coordinates (0,0)."
    point1.set(0, 0)
    assert point1.get() == "Current point coordinates (0,0)."
    point1.set(1, 1)
    assert point1.get() == "Current point coordinates (1,1)."
    point1.set(5, 7)
    assert point1.get() == "Current point coordinates (5,7)."
    assert point1.calculate_distance(point1) == 0
    point1.set(1, 1)
    point2.set(1, 1)
    assert point1.calculate_distance(point2) == 0
    point1.set(0, 0)
    point2.set(3, 4)
    assert point1.calculate_distance(point2) == 5
    point1.set(1, 3)
    point2.set(3, 1)
    assert round(point1.calculate_distance(point2), 3) == 2.828
    point1.set(1, 1)
    point2.set(2, 2)
    assert round(point1.calculate_distance(point2), 3) == 1.414
    assert point1.calculate_distance("point") == -1
    assert point1.calculate_distance(10) == -1
    assert point1.calculate_distance(7.5) == -1
    assert point1.calculate_distance(True) == -1
    assert point1.calculate_distance([]) == -1
    assert point1.calculate_distance(object()) == -1
