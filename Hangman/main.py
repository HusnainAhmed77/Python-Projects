import random
import hangman_art
from hangman_art import stages
from hangman_art import logo
import hangman_words
from hangman_words import word_list

print(logo)

num = random.randint(0,len(word_list)-1)

chosen_word = word_list[num]

word_length = len(chosen_word)

print(chosen_word)


display = []

for i in range(0,word_length):
    display.append("_")

print(display)

lives = 6

while "_" in display and lives >= 0:

  guess = input("Guess a letter for the game: ").lower()
  
  if guess in chosen_word:
    for l in range(word_length):
      if chosen_word[l] == guess:

        display[l] = guess
        print(display)
    
  else:
    print("Wrong Guess!")
    print(stages[lives])
    lives -= 1
    print(display)



if "_" not in display:
    print("You win!")
else:
    print("Game Over! The word was:", chosen_word)


print(logo)