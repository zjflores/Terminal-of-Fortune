phrase1 = "wheel of fortune cookie"
blank1 = ["_", "_", "_", "_", "_", " ", "_", "_", " ", "_", "_", "_", "_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_"]
category1 = "before & after"

phrase2 = "hell is other people"
blank2 = ["_", "_", "_", "_", " ", "_", "_", " ", "_", "_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_"]
category2 = "quotes"

phrase3 = "ruby on rails"
blank3 = ["_", "_", "_", "_", " ", "_", "_", " ", "_", "_", "_", "_", "_"]
category3 = "technology"

phrases_list = [phrase1, phrase2, phrase3]

blanks_dictionary = { 
    phrase1: blank1,
    phrase2: blank2,
    phrase3: blank3
    }

category_dictionary ={
    phrase1: category1,
    phrase2: category2,
    phrase3: category3
}

guessed_letters_dictionary = {}
hint_dictionary = {}

def greet_user():
    name = input("Hello, what is your name?")
    print("Welcome to Terminal of Fortune, {}".format(name))
greet_user()

def basic_rules():
    print(""" 
    Let's quickly go over the basics. 
    
    Each turn you will guess a letter to try to complete your word. Your guesses will be limited to twice the number of letters in your phrase. 
    
    If you know the answer, you may correctly guess the completed phrase to finish the game.""")
    print()
    print()
basic_rules()

def start_game():
    while True:
        play = input("Now that you know the gist, are you ready to play?")
        if play.lower() == "yes":
            print ("Come on down!")
            break
        elif play.lower() == "no":
            print("You are the weakest link. Goodbye.")
            break
        else:
            print("Reply hazy, try again.")
            print()
start_game()
print()

import random
chosen_phrase = random.choice(phrases_list)
corresponding_blanks = (blanks_dictionary[chosen_phrase])
output = (" ".join(corresponding_blanks))
print("Your word is {}.".format(output))
print("Category: {}".format(category_dictionary[chosen_phrase]))

def offer_hint():
    print("""
    You seem to be having some trouble. You have the option of receiving a hint. Terminal of Fortune will run 3 random letters you have not guessed yet. There is no guarantee that the letters selected will be in your phrase, but it will at least rule out a few options for you.
    """)
    hint = input("Would you like a hint?")

    if hint.lower() == "yes":
        #loop guessed letters through alaphabet
        begin = ord("a")
        end = ord("z")
        
        # for letter in guessed_letters_dictionary:
        for num in range(begin, end + 1):
            letter = chr(num)
            if letter not in guessed_letters_dictionary:
                hint_dictionary[ord(letter)] = letter
        return hint_play(chosen_phrase)

    if hint.lower() == "no":
        print("You seem confident. I hope it pays off.")
                        

def print_blanks():
    output = (" ".join(corresponding_blanks))
    print("Your word is now: {}.".format(output))

def game_play(chosen_phrase):
    i = 1
    
    while i <= int(len(chosen_phrase) * 1.5):
        print()

        if i == int(len(chosen_phrase) * 0.75) :

            offer_hint()

        guessed_letter = input("Guess a letter.")
        guessed_letters_dictionary[guessed_letter] = True

        if guessed_letter == chosen_phrase:
            return you_win()
            
        for index in range(len(chosen_phrase)):
            
            if chosen_phrase[index].lower() == guessed_letter.lower():
                corresponding_blanks[index] = guessed_letter
           
        if guessed_letter.lower() in chosen_phrase:
            print()
            print("You chose wisely.")
        
        elif guessed_letter not in chosen_phrase:
            print("Sorry {} is not in:".format(guessed_letter))


        print_blanks()
        if not "_" in corresponding_blanks:
            return you_win()
            
        i = i + 1
    you_lose()

def hint_play(chosen_phrase):
    i = 0
    while i < 3:
        hint_keys = list(hint_dictionary.keys())
        hint_index = random.choice(hint_keys)
        guessed_letter = hint_dictionary[hint_index]
        
        guessed_letters_dictionary[guessed_letter] = True
        del hint_dictionary[hint_index]

        for index in range(len(chosen_phrase)): 
            if chosen_phrase[index].lower() == guessed_letter:
                corresponding_blanks[index] = guessed_letter
           
        if guessed_letter not in chosen_phrase:
            print("{} is not in:".format(guessed_letter.upper()))
            
        print_blanks()
        
        if not "_" in corresponding_blanks:
            return you_win()

        i = i + 1
    

def play_again(): 
    play_again = input("Would you like to play again?")
    if play_again.lower() == "yes":
        print()
        global chosen_phrase 
        chosen_phrase = random.choice(phrases_list)
        
        corresponding_blanks = (blanks_dictionary[chosen_phrase])

        output = (" ".join(corresponding_blanks))

        print("Your word is {}.".format(output))
        print("Category: {}".format(category_dictionary[chosen_phrase]))

        return game_play(chosen_phrase)
        
    else:
        print("Now, sashay away.")

def you_win():
    prize_list = ["A NEW CAR", "$25,000", "$25,000", "$25,000", "$25,000", "$25,000","$30,000", "$30,000", "$30,000", "$35,000", "$35,000", "$35,000", "$50,000", "$50,000", "$100,000", "$1,000,000"]  
    prize = random.choice(prize_list)
    print()
    print()
    print("CONGRATULATIONS! You just won {}!".format(prize))
    print()
    phrases_list.remove(chosen_phrase)
    if len(phrases_list) > 0:
        return play_again()
    else:
        print("Your tour ends here.")

def you_lose():
    print()
    print()
    print("Better luck next time!")
    print()
    phrases_list.remove(chosen_phrase)
    if len(phrases_list) > 0:
        return play_again()
    else:
        print("Your tour ends here.")

game_play(chosen_phrase)



