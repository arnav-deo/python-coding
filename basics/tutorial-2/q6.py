numbers = [4, 9, 1, 7, 3]

largest_element = 0

for elements in numbers:
    print(f"current element - {elements}, largest element - {largest_element}")
    if elements > largest_element:
        print(f"Assigining {elements} to largest_element")
        largest_element= elements

print(largest_element)

