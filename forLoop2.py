#Get all the even numbers from 0 - 50
even_nums = []
for i in range(1,51):
    if i % 2 == 0:
        even_nums.append(i)

#print(even_nums)

#Better way of writing although mine loops simpler
even_nums1 = []
for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        even_nums1.append(number)

#print(even_nums1)

#Best Practice 

evens = [number for number in range(1,51) if number % 2 == 0]

print(evens)