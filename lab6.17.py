# Dwayne Ellis
# October 6, 2020
# Password Modifier
# Scope: Write a program that takes a simple password and makes it stronger by replacing characters using the key below,
# and by appending "q*s" to the end of the input string.

user_input = input()
password = ''

for x in user_input:
    if x == 'i':
        password += "!"
    elif x == 'a':
        password += "@"
    elif x == 'm':
        password += "M"
    elif x == 'B':
        password += "8"
    elif x == 'o':
        password += "."
    else:
        password += x
password += "q*s"
print(password)
