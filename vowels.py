def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in text:
        if char not in vowels:
            result += char
    
    return result

# Prompt user for input text
input_text = input("Enter a text: ")

# Remove vowels and display the result
output_text = remove_vowels(input_text)
print("Text without vowels:", output_text)
