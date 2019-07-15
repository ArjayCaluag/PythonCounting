print('Python Hangman')
print('You have 10 guesses!')
import random

def get_guess():
  hide = "-" * len(secret_word)
  total_guesses = 10 

  while total_guesses > -1 and not hide == secret_word:
    
    print(hide)
    print ("Amount of guesses left: " + str(total_guesses))
    
  
    guess = input("Take a guess:")
    
    
    if len(guess) != 1:
      print ("Your guess must be one letter at a time")
      

    elif guess in secret_word:
      print ("Correct!")
      hide = update_hide(secret_word, hide, guess)
      total_guesses -= 1

    else:
      print ("Wrong, try again!")
      total_guesses -= 1
    
  if total_guesses < 0:
    print ("You lose. The word was: " + str(secret_word))
  
  else:
    print ("Congrats! You figured out the word: " + str(secret_word))
    

def update_hide(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess    
      
    else:
   
      result = result + cur_dash[i]
      
  return result
    
words = ["yearup", "arjay", "melody"]
secret_word = random.choice(words)
get_guess()