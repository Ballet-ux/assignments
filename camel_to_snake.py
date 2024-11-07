def camel_to_snake(camel_case_name):
    snake_case_name = ""
    
    for char in camel_case_name:
        if char.isupper():
            snake_case_name += "_" + char.lower()
        else:
            snake_case_name += char
    
    return snake_case_name

# Prompt user for camel case variable name
camel_case_name = input("Enter a variable name in camel case: ")

# Convert to snake case
snake_case_name = camel_to_snake(camel_case_name)

# Output the snake case variable name
print("The snake case version is:", snake_case_name)
