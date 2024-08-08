from random_words import RandomWords
import random

r = RandomWords()
t = RandomWords()

domain_extensions_list = [".com", ".net", ".io", ".org"]

def generate_random_website():
    # We are generating two random words and combining them
    word1 = r.random_word()
    word2 = t.random_word()

    combined_word = word1 + word2
    
    # Select random domain
    domain = random.choice(domain_extensions_list)
    #final fake website
    return combined_word + domain

# Generate and Print 10000 random website names
for _ in range(1000):
    print(generate_random_website())

print("XXXX")


