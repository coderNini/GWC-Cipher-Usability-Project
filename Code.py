#This program is the starter code for the Cipher Usability Project. 
# This code is inspired by Cracking Codes with Python: An Introduction to Building and Breaking Ciphers by Al Sweigart https://www.nostarch.com/crackingcodes (BSD Licensed)

import  string

# Global variables
runProgram = "yes"
initialPosition = 0
shiftedPosition = 0
shiftedMessage = ""
lettersLower = string.ascii_lowercase
lettersUpper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
possibleCharacters = lettersLower + lettersUpper + numbers + symbols

# Define the function called encryptOrDecrypt
def encryptOrDecrypt():
  global shiftedPosition
  if mode.lower() == "encrypt":
    shiftedPosition = initialPosition + key
  elif mode.lower() == "decrypt":
    shiftedPosition = initialPosition - key

# Define the function called wraparound
def wraparound():
  global shiftedPosition
  if shiftedPosition >= len(possibleCharacters):
    shiftedPosition = shiftedPosition - len(possibleCharacters)
  elif shiftedPosition < 0:
    shiftedPosition = shiftedPosition + len(possibleCharacters)
    
# Run code

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters: " + possibleCharacters + "\n\nLet's get started!\n")

while runProgram.lower() == "yes":
  # Receive user input
  initialMessage = input("What is your message? ")
  key = int(input("\nWhat is the key? Choose a number from 0 to 93. "))
  mode = input("\nDo you want to encrypt or decrypt? ")
  
  # Encrypt or decrypt the message
  for character in initialMessage:
    if character in possibleCharacters:
      initialPosition = possibleCharacters.find(character)
      encryptOrDecrypt()
      wraparound()
      shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]
  
    else:
      shiftedMessage = shiftedMessage + character
  
  # Print the shifted message
  if mode.lower() == "encrypt" or mode.lower() == "decrypt":
    print("\nYour " + mode.lower() + "ed message is: " + shiftedMessage)
    
    runProgram = input("\nDo you want to encrypt or decrypt another message? Type yes or no. ")
  else:
    print("\nOops! :( The program reads an error. Try again and make sure you type either 'encrypt' or 'decrypt.'")
  
  print ("\n")
  
  shiftedMessage = ""
