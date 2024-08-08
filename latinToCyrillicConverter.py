sample_Website =["google.com", "romeo.org", "germаny.net", "а", "axxx"]
#cyrillic unicode list of a, o, e, r
cyrillic_letters = ['\u0430', '\u043e', '\u0435', '\u0433']
#latin unicode list of a, o, e, r
latin_letters = ['\u0061', '\u006F', '\u0065', '\u0072' ]

def letter_Converter(websites, latin, cyrillic):
    #create a dictionary
    letter_map = dict(zip(latin, cyrillic))

    #replace latin letters with cyrillic letters in each website
    updated_list = []
    for website in websites:
        updated_website = website
        for latin_letter, cyrillic_letter in letter_map.items():
            updated_website = updated_website.replace(latin_letter, cyrillic_letter)
        updated_list.append(updated_website)

    return updated_list


updated_list = letter_Converter(sample_Website, latin_letters, cyrillic_letters)

print(updated_list)


"""

def letters_checker(websites, letters):
    for website in websites:
        for letter in letters:
            if letter in website:
                print(f"'{letter}' found in '{website}'")

#checks for a type of letter on the list
letters_checker(sample_Website, cyrillic_letters)

"""

#test code
#print(sample_Website[0])
#print("this is y")
#print ("this is cyrillic" + " " + '\u0072')