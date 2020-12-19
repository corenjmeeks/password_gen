import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

password = []

for letter in range(15):
  	password.append(random.choice(letters+numbers+symbols))

str_password = "".join(password)
print(str_password)
