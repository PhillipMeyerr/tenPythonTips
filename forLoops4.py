# Looking a nested list comprehension
# This is the scrub way of doing things
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattend = []

for row in matrix:
    for num in row:
        flattend.append(num)
        continue
#print(flattend)
###
### Baller way to do this

flattend = []
flattend = [num for row in matrix for num in row]

print(flattend)
print("test")