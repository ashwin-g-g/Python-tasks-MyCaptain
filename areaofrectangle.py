class Rectangle :
    area = 0
    def calculateArea(self, length, breadth):
        self.area = length*breadth
        return self.area
rec = Rectangle()
l = int(input("Enter the length of the rectangle : "))
b = int(input("Enter the breadth of the rectangle : "))
print("Area of rectangle = ", rec.calculateArea(l,b))
