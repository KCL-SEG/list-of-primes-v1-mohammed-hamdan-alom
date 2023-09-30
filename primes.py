"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    
    # List of primes start empty
    # Add 2 to list
    # Go through every integer and see if its divisible by every number in list
    # If it isnt, add to the list
    # continue until the list is less than number_of_primes


    list = []

    i = 2
    list.append(i)
    while len(list) < number_of_primes:
        if all(i % j != 0 for j in list):
            list.append(i)
        i += 1
    return list
    
    


print(primes(10))