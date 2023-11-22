from uzwords import words
import random as r

def get_word(): # Function for getting random word from uzwords.py file
    word = r.choice(words)
    while "-" in word or ' ' in word:
        word = r.choice(words)
    return word.upper()

def display(user_letters, word): # Display function that for used letters and new found letters
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play(): # Main function for play game
    word = get_word() #Random word from uzwords.py
    word_letters = set(word) #Removing twice used letters
    user_letters = ""
    print(f"I thougth a word and lenght is equal {len(word)}. Can you find?")
    print(word)
    while len(word_letters) > 0:
        print(display(user_letters, word))
        if len(user_letters) > 0:
            print(f"Your used letters untill this time: {user_letters}")

        letter = input("Input letter: ").upper()
        if letter in user_letters:
            print("You used this letter. Please input another letter: ")
            continue
        
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} is right.")
        else:
            print("This letter is not given in word.")
        
        user_letters += letter
    return print(f"Congratulations! {word} word is found {len(user_letters)} attemps.")
play()