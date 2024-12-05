class Figure:
    unit = "cm"
    def calculate_area(self):
        raise NotImplementedError
    def info(self):
        raise NotImplementedError
class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length
    def calculate_area(self):
        return self.__side_length * 2
    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{Figure.unit}, area: {area}{Figure.unit}")
class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def calculate_area(self):
        return self.__length * self.__width
    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {area}{Figure.unit}")
figures = [
    Square(5),
    Square(10),
    Rectangle(5, 8),
    Rectangle(3, 7),
    Rectangle(12, 5),]
for figure in figures:
    figure.info()

