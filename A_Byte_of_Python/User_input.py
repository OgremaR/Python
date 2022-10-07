def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)

something2 = input('Введите текст: ')
import re
something = re.sub("[^А-я]","",something2)

if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")