# Funtion to recursively search for user's inputted number
def recursive_search(numbers, target, start = 0):
    if start >= len(numbers):
        return False
    if numbers[start] == target:
        return True
    return recursive_search(numbers, target, start + 1)

numbers = [34, 67, 23, 54, 89, 14, 43]
numbers.sort()
target = int(input("Enter a number to search for: "))

# Checking if the number is in the list
found = recursive_search(numbers, target)

if found:
    print("Number was found in the list.")
else:
    print("Number was not found in the list.")