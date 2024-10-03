def sort_by_length(input_string):
    words = input_string.split()
    sorted_words = sorted(words, key=len)
    return ' '.join(sorted_words)

i= "This is a cool sentence"
o= sort_by_length(i)
print(o)  # Output: "a is This cool sentence"
