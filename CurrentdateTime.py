#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Python Basic Exercises for Beginners
#Problem 3: Write a Python program to display the current date and time.

#SampleFormat:

#Current date and time :
#2014-07-05 14:34:14
  
from datetime import datetime

#get current date and time

current_datetime = datetime.now()

#Format the current date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")


#print the result
print("Current date and time :")
print(formatted_datetime)
