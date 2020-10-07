# Antonio Alvarez
# 1796498

user_word = input()
word = ""
word_reverse = ""
for i in range(len(user_word)):
   if user_word[i].isalpha():
       word += user_word[i].lower()
       word_reverse = user_word[i].lower() + word_reverse
if word == word_reverse:
   print(user_word + " is a palindrome")
else:
   print(user_word + " is not a palindrome")