## Day 2 - String & manipulation

text = """Python is a powerful programming language. It's easy to learn
and versatile!
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

#String Indexing and slicing

print(text[0])   #First Character
print(text[-1])  #Last Character
print(text[0:15])  #Slice 0 to 15
print(text[:6])   #From start to 5
print(text[7:])   #7 to end

#String Methods



## Exercise 2 ##

# Count Character
count_char=len (text)

# Count Word
word = text.split()
word_count = len(word)


# Count Sentence


#Display Result
print(f"Count Character:{count_char}")
print(f"Count Word:{word_count}")