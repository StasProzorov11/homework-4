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