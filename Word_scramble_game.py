# Word Scrambling Game
# given is a list of around 20 words of common games , food items , places and items , the game randomly selects a word from the list and scrambles it, user have to guess the word

import random

my_list = ['Minecraft', 'Fortnite', 'Roblox', 'Candy Land', 'Mario Kart', 'Apple', 'Pizza' , 'Noodles' , 'Coffee', 'Burger', 'Ice Cream', 'China', 'India', 'the United States', 'Belgium', 'Badminton', 'Germany', 'France', 'Knife', 'Laptop' ]

print(f"Given list is {my_list}")

computer = random.choice(my_list)

def shuffle_str(word) :
    chars = list(word)
    random.shuffle(chars)
    scramble = ''.join(chars)
    return scramble


scramble_word =  shuffle_str(computer)

print(f"The scrambled word is : {scramble_word}")

print("You have 3 attempts to guess the correct word from the given list, with each guess your score decreases by 10. After 3 attempts, your score will be zero. Maximum score is 30")

count = 3
while(count > 0):
    user_input = input('Enter your guess : ')
    if(user_input == computer):
        print("Correct ! ")
        break
    
    else :
        count -= 1
        print(f"Remaining guesses are : {count}")
    


print(f"Your score is {count*10}")
if(count == 0):
    print("You failed !")
    print(f"The correct word is {computer}")