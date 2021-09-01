#get a word
#draw the lines for all the letters
#ask the user for input for the letters
#see if user input is right or wrong
#if right: fill the word in the correct areas
#if wrong: person loses a life
import random

def check (correct, dashes, guess):
  for i in len(correct):
    result = ''
    if correct[i] == guess:
      result = result + guess
    else:
      result = result + dashes[i] 
      lives -= 1
def blanks(word):
  global lives
  lives = 20
  while lives > 0:
    global f
    f = '_ ' * len(word)
    print ('Here it is:', '_ ' * len(word))
    q = input('Put in a letter:')
    check(randomword, f, q)

def createword():
  word_list = ['glass','book','phone','monitor','computer','keyboard','mouse','pencil','closet','markers', ]
  global randomword
  randomindex = random.randint(0,9)
  randomword = word_list[randomindex]
  blanks(randomword) 

def main():
  print ('Hello, welcome to Hangman!')
  print ('You have 5 lives to fill in the blanks of a random object. Good Luck!')
  createword()
    
main()




