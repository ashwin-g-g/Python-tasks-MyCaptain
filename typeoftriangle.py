side1 = input("Enter the 1st side of triangle: ")
side2= input("Enter the 2nd side of triangle: ")
side3= input("Enter the 3rd side of triangle: ")
if side1 == side2 and side2 == side3 and side1 == side3:
    print("Equilateral triangle")
elif side1 != side2 and side2 != side3 and side1 != side3:
    print("Scalene triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
