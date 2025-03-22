# day-10
# Anagram checker
def is_anagram(word1, word2):
    word1 = "".join(word1.split()).lower()
    word2 = "".join(word2.split()).lower()
    if sorted(word1) == sorted(word2):
        return True
    return False
print("Anagram Checker 🔄")
first_word = input("Enter First Word: ")
second_word = input("Enter Second Word: ")
if is_anagram(first_word, second_word):
    print(" ✅ Yes it's a anagram!")
else:
    print(" ❌ No it's not an anagram")
  