"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import randint
import keyring

def part1(num):
    a= "type a number"
      print(a)
      x = int(input"type a number"))
      if x%2 == 0:
      print ("Even")
      else:
      print("Odd")
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """


def part2():
    x = print(randint(1, 9))
       print("guess a number between 1 and 9")
       y = int(input("guess a number between 1 and 9"))
       while ( y != input("exit")):
       if x == y:
       print("you guessed exactly right")
       
       else if x < y:
       print("your number is too high")
       
       else if x > y:
       print("your number is too low")
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """


def part3(string):
    print("type a word")
       y = string(input("type a word"))
              if y == y[::-1]:
              print("is a palindrome")
              else:
              print("is not a palindrome")
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """


def part4a(filename, username, password):
service_id = 'PASSWORD'

keyring.set_password (filename, 'madzt', 'freddie68')

    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """

def part4b(filename, password=None):
    print(keyring.set_password)
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """


if __name__ == "__main__":
    if part1(3)
    print(odd)# odd!
    part1(4)
    print(event)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
