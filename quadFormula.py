import math
import cmath

# This program will ask the user for the coefficient values of a quadratic equation
# then it will solve the equation, and return the results to the user
# Really i made this because I failed my math test, and got inspired to re-learn the quadratic formula

# roots, zeros and solutions will be used interchangeably throughout the comments

# Quadratic formula  = (-b +- sqrt(b^2 - 4ac)) / 2a

# Coefficient values
print("Please enter the values for the coefficients of the quadratic equation \n Refer to the quadratic formula. \n a, b, c are the coefficents, and example of this would be: \n ax^2 + bx + c = 0")

a = float(input("Please enter the coefficent value for A:"))
b = float(input("Please enter the coefficent value for B:"))
c = float(input("Please enter the coefficent value for C:"))

# Now taking the values the user inputs, we now are able to calculate the discriminant

discriminant = (b**2) - (4*a*c)

# Based off the discriminant alone, we can figure out the number of roots the equation has

# According to Khan Academy https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-formula-a1/a/discriminant-review
# If the discriminant is greater than 0, there are 2 real roots
# If the discriminant is negative, there are 2 imaginary roots
# If the discriminant is 0, there is a repeated real root

if discriminant == 0:
    print("There is a repeated real root")
else:
    if discriminant > 0:
        print("There are 2 real roots")
    else:
        print("There are 2 imaginary roots")

# Now we can calculate the roots

# Because the quadratic formula contains a +/-, we need to calculate both roots, so do this by creating 2 variables with same formula, but different signs

rootOne = (-b + math.sqrt(discriminant)) / (2*a)
rootTwo = (-b - math.sqrt(discriminant)) / (2*a)

# now we return the roots to the user

print("The roots are: ", rootOne, " and ", rootTwo)

# later I might make it so it can also return a physical graph for the user to see, but for now I guess this will work




