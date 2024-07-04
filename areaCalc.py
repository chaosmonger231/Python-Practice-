#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Python Basic Exercises for Beginners
#Problem 3: Write a Python program that calculates the area of a circle based on the radius entered by the user

#Sample Output:

#r = 1.1
#Area = 3.8013271108436504
  
#import Module here
import math


def main():
    """
    This is the main function of the script.
    It is executed when the script is run directly.
    """
    
    
    a = input("Enter Radius: ")
    x = float(a) #float for decimals
    
    # Your code goes here!
    area = math.pi * math.pow(x, 2)
    
    
    print("Radius is " + a)
    print("Area is " + str(area))
    


if __name__ == "__main__":
    main()