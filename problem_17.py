# Problem 17: Capitalize first letter of each word
# Find and fix the error

def capitalize_words(text):
    words = text.split()
    capitalize = []
    for word in words:
        capitalize.append(word.capitalize())
    return " ".join(capitalize)

sentence = "hello world from python"
print(capitalize_words(sentence))
