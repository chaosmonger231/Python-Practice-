#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Python Excercise for Beginners (Solution)

def twinkle():
  
  indent_level = 8
  indent = ' ' * indent_level
  string = "Twinkle, twinkle, little star,"
  string2 = "How I wonder what you are!"
  
  indented_string = f"{indent}{string2}"
  
  finalPrint = string + "\n" + indented_string
  
  print(finalPrint)
  
  
def above():
  
  indent_level = 16
  indent = ' ' * indent_level
  string = "Up above the world so high,"
  string2= "Like a diamond in the sky."
  
  indented_string = f"{indent}{string}"
  indented_string2 = f"{indent}{string2}"
  
  
  print(indented_string)
  print(indented_string2)
  
twinkle()
above()
twinkle()
  
