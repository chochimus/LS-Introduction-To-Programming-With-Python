def upper_if_10_chars(text):
    if len(text) > 10:
        return text.upper()
    else:
        return text

print(upper_if_10_chars('hello world'))
print(upper_if_10_chars('goodbye'))