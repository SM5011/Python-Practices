def sort_data(grocery_codes):
    print(sorted(grocery_codes))

def reverse_data(grocery_codes):
    print(list(reversed(grocery_codes)))

def sort_with_reverse(grocery_codes):
    print(sorted(grocery_codes, reverse=True))

grocery_codes = [181, 178, 187, 182, 192, 189, 202, 201]

print("Sorted grocery codes:")
sort_data(grocery_codes)

print("Reversed grocery codes:")
reverse_data(grocery_codes)

print("Sorted grocery codes in reverse order:")
sort_with_reverse(grocery_codes)
