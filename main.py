# 1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку.
# Виведіть обидві кількості на екран. (використовувати цикл)

# try :
#     text = str ( input ( "Enter text and numbers : " ) )
#     numbers = 0
#     letters = 0
#
#     for i in text :
#         if i.isdigit () :
#             numbers += 1
#         elif i.isalpha () :
#             letters += 1
#
#     print ( f"numbers - {numbers}" )
#     print ( f"letters - {letters}" )
#
# except TypeError :
#     print ( "Error" )
#
# except Exception as error :
#     print ( f"Error occurred: {error}" )
#  2. Користувач вводить з клавіатури рядок та символ для пошуку.
# # # Порахуйте скільки разів у рядку зустрічається потрібний символ.
# # # Отримане число виведіть на екран.
# try:
#  text = str(input("Enter text and numbers : "))
#  numbers = str(input("Enter a symbol to search : "))
#  quantity = 0
#
#  for i in text:
#     if i == numbers:
#         quantity += 1
#  print(f"Numbers {numbers} occurs {quantity} times")
# except TypeError:
#  print("Error")
#
# except Exception as error:
#  print(f"Error occurred: {error}")
# 3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
# try:
#  text = str ( input ( "Enter text : " ) )
#  search = str ( input ( "Enter a search word : " ) )
#  replacement = str ( input ( "Enter a replacement word : " ) )
#
#  replacement_word = text.replace (search , replacement )
#  print(f"replacement_word : {replacement_word}")
# except TypeError:
#  print("Error")
#
# except Exception as error:
#  print(f"Error occurred: {error}")

# 4. Дано рядок. (зробити зрізи)
#
# text = str ( input ( "Enter text : " ) )
# sentence = text
#
# # - Спершу виведіть третій символ цього рядка.
#
# print(sentence [2])
#
# # - У другому рядку виведіть передостанній символ цього рядка.
#
# print(sentence [-2])
#
# # - У третьому рядку виведіть перші п'ять символів цього рядка.
#
# print(sentence [0:5])
#
# # - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
#
# print(sentence [:-2])
#
# # - У п('ятому рядку виведіть усі символи з парними індексами '
# #       '(вважаючи, що індексація починається з 0, тому символи виводяться з першого).)
#
# print(sentence [::2])
#
# # - У шостому рядку виведіть усі символи з непарними індексами, тобто,
# # починаючи з другого символу рядка.
#
# print(sentence[1::2])
#
# # - У сьомому рядку виведіть усі символи у зворотному порядку.
#
# print(sentence[::-1])
#
# # - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку,
# # починаючи з останнього.
#
# print(sentence[::-2])
#
# # - У дев'ятому рядку виведіть довжину цього рядка.
#
# print(len(text))

#Додатково:

# Є певний текст. Реалізуйте наступну функціональність:
#
# ■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;

# text = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
#         "lorem Ipsum has been the industry's standard dummy text ever since the 1500s. "
#         "when an unknown printer took a galley of type and scrambled it to make a type specimen book."
#         "it has survived not only five centuries, but also the leap into electronic typesetting."
#         "remaining essentially unchanged."
#         "it was popularised in the 1960s with the release of Letraset sheets containing. "
#         "lorem Ipsum passages. "
#         "and more recently with desktop publishing software. "
#         "like Aldus PageMaker including versions of Lorem Ipsum")
# text2 = text.split('.')
# for i in text2:
#     print(i.strip().capitalize(),end="."+"\n")
# ■ Порахуйте скільки разів цифри зустрічаються у тексті;
# numbers = 0
# for i in text:
#  if i.isdigit():
#   numbers +=1
# if numbers == 0:
#   print("No numbers found")
# else:
#   print(f"Numbers = {numbers}")

# ■ Порахуйте скільки разів розділові знаки зустрічаються в тексті;

# signs = [':', ';', ',', '.', '!', '?']
# signs_lst = []
#
# for i in text :
#  if i in signs :
#   signs_lst.append ( i )
#
# print (f"Signs = {len ( signs_lst ) }")
#
# # ■ Порахуйте кількість знаків оклику в тексті.
#
# exclamation_marks = text.count ( "!" )
# print(f"Exclamation marks = {exclamation_marks}")