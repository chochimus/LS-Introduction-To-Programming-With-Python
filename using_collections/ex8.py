text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29 

# first is using index from newly produced string from splice,
# second is using original indexing of string, but only looking in
# the range 21-35