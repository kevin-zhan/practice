def remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers

numbers = [2,1,5,3,3]
print remove_smallest(numbers)

