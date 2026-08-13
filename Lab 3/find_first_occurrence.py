def str_str(haystack, needle):
    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1

# Test Case 1
haystack = "sadbutsad"
needle = "sad"
print("Input:")
print("haystack =", haystack)
print("needle =", needle)
print("Output:", str_str(haystack, needle))

# Test Case 2
haystack = "leetcode"
needle = "leeto"
print("\nInput:")
print("haystack =", haystack)
print("needle =", needle)
print("Output:", str_str(haystack, needle))