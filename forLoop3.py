#Scrub way of finding if the first letter is a and last is y
options = ["any", "albany", "apple", "world", "hello", ""]
#valid_strings = []

for string in options:
    if len(string) <= 1:
        continue
    if string[0] != "a":
        continue
    if string[-1] != "y":
        continue
#   valid_strings.append(string)

###
### 
##
# Baller way
# remember that (string is being added to the list)
# As long as the conditions are met
# As such these are called comprehensions
# Notice no need to : after if bc it's inside conditional (array [])

options = ["any", "albany", "apple", "world", "hello", "" , "ay"]
valid_strings = [
    string
    for string in options
    if len(string) >= 1
    if string[0] == "a"
    if string[-1] == "y"
]

print(valid_strings)
print("This is a test")