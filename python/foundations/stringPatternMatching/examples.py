# the function group of match object instance returns the substring that matches the regular expression.
import re

string1 = "Welcome to python shell"
match =  re.search('pytho', string1)
print(match.group())
# try:
#     match = re.search("Pyth", string1)
#     print(match.group())
# except TypeError:
#     print("exception occured")
# finally:
#     print('completed')

string2 = "python shell"
match = re.search("shel*", string2)
print(match.group())




