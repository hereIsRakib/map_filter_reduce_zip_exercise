from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


# 4 Combine all of the numbers that are in a list on this file using
# reduce (my_numbers and scores). What is the total?

def capitalize(item):
    return item.upper()


print(list(map(capitalize, my_pets)))

print(list(zip(my_strings, sorted(my_numbers))))


def over_50(item):
    return item / 50 >= 1


print(list(filter(over_50, scores)))


# 4 Combine all of the numbers that are in a list on this file using
# reduce (my_numbers and scores). What is the total?

def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_numbers+scores))
