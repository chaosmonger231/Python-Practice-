#Personal Project
#Personal:

#Write a Python program that checks if a
#string inpute matches with list

#Sample Output:

#input: BABY
#output: Word "BABY" matches
  
#import Module here

def main():
    """
    This is the main function of the script.
    It is executed when the script is run directly.
    """
    names = ["А"
             "Б"
             "В"
             "Г"
             "Д"
             "Е"
             "Ё"
             "Ж"
             "З" "И" "Й" "К" "Л" "М" "Н" "О" "П" "Р" "С" "Т" "У"
             "Ф" "Х" "Ц" "Ч" "Ш" "Щ" "Ъ" "Ы" "Ь" "Э" "Ю" "Я" "а"
             "б" "в" "г" "д" "е" "ё" "ж" "з" "и" "й" "к" "л" "м"
             "н" "о" "п" "р" "с" "т" "у" "ф" "х" "ц" "ч" "ш" "щ"
             "ъ" "ы" "ь" "э" "ю" "я"]  #cyrllic letter "a"
    
    a = str(input("Give me a name: "))
    
    print("Your name is " + a )

    matches = [letter for letter in names if letter in a]
    if matches:
      print("LETTER MATCHES")
    else:
      print("Words Doesnt Match With List")
    
  
    # Your code goes here
    

if __name__ == "__main__":
    main()
