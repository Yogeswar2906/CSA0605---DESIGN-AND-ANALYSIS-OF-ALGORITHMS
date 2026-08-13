def first_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""

# Test Case 1
words = ["abc", "car", "ada", "racecar", "cool"]
print("Input:", words)
print("Output:", first_palindrome(words))

# Test Case 2
words = ["notapalindrome", "racecar"]
print("\nInput:", words)
print("Output:", first_palindrome(words))