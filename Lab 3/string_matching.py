def string_matching(words):
    result = []

    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break

    return result

# Test Case 1
words = ["mass", "as", "hero", "superhero"]
print("Input:", words)
print("Output:", string_matching(words))

# Test Case 2
words = ["leetcode", "et", "code"]
print("\nInput:", words)
print("Output:", string_matching(words))

# Test Case 3
words = ["blue", "green", "bu"]
print("\nInput:", words)
print("Output:", string_matching(words))