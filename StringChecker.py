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
    names = ["JOE", "MARK", "MAYA"]
    
    a = str(input("Give me a name: "))
    
    print("Your name is " + a )
    if a in names:
      print("WORD MATCHES")
    else:
      print("Words Doesnt Match With List")
    
  
    # Your code goes here
    

if __name__ == "__main__":
    main()
