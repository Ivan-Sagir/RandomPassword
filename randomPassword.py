import random

name = input("What's your name? ")
pas = ''

for x in range(10):
    pas = pas + random.choice(list("1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")) 
print("Hello " + name + ", your password is " + pas)
