# Необходимо разработать класс Point2D, на базе которого можно будет созда-
# вать объекты, эмулирующие точки на плоскости. Объекты двумерных точек
# должны обладать следующим поведением:
#  set (для установления новых координат (x, y) текущего объекта-точки; по
# умолчанию точка находится в нулевой позиции);
#  get (для просмотра текущих координат объекта-точки);
#  calculate_distance (принимает ещё один объект-точку и вычисляет рас-
# стояние на плоскости с использованием теоремы Пифагора между приня-
# той точкой и текущей точкой; если в качестве параметра принята не точка,
# должен возвращаться код ошибки, например, значение -1).


class Point2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_info(self):
        return f"Point: x = {self.x}, y = {self.y}"

    def calculate_distance(self, point2):
        dist = ((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2) ** 0.5
        return dist


def main():
    point1 = Point2d()
    print(point1.get_info())
    point2 = Point2d(3, 4)
    print(point2.get_info())

    distance = point1.calculate_distance(point2)

    msg = f"The distance: {distance}" if distance != -1 else "Error..."

    print(msg)


main()