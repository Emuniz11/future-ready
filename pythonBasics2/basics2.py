# # 2D Array
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][1] = 20
# for row in matrix:
#     for item in row:
#         print(item)

# # List Methods
# numbers = [5, 2, 7, 1, 7, 4]
# numbers.append(20)
# print(numbers)
#
# numbers.insert(0, 10)
# print(numbers)
#
# numbers.remove(2)
# print(numbers)
#
# numbers.pop()
# print(numbers)
#
# print(numbers.count(7))
#
# print(numbers.index(5))
#
# print(10 in numbers)
#
# numbers.sort()
# print(numbers)
#
# numbers.reverse()
# print(numbers)
#
# numbers2 = numbers.copy()
# numbers.pop()
# print(numbers2)
# print(numbers)
#
# numbers.clear()
# print(numbers)

# numbers = [1, 4, 7, 3, 4, 5, 8, 7]
# for number in numbers:
#     if numbers.count(number) > 1:
#         numbers.remove(number)
# print(numbers)
# or
# numbers = [1, 4, 7, 3, 4, 5, 8, 7]
# unique = []
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)

# # Tuple (immutable) only able to get info from tuple - cannot mutate
# numbers = (1, 2, 3)
# print(numbers[0])

# # Unpacking
# coordinates = (1, 2, 3)
# # x = coordinates[0]
# # y = coordinates[1]
# # z = coordinates[2]
# # is the same as
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)
# # this works for lists to
# coordinates = [1, 2, 3]
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)

# # Dictionaries (key/value) pairs
# customer = {
#     'name': 'John Smith',
#     'age': 30,
#     'is_verified': True
# }
# print(customer['name'])
# print(customer.get('name'))
# # if key doesn't exist .get will not give an error
# # but it is possible to give a value to that key that does not exist
# print(customer.get('birthday'))
# print(customer.get('birthday', 'Jan 1 1990'))
# # see this key still does not exist
# print(customer.get('birthday'))
# # this is how to properly add a new key/value pair
# customer['birthday'] = 'Jan 1 1990'
# print(customer['birthday'])
#
# customer['name'] = 'Eric'
# print(customer["name"])

# # phone_number = input('What is your phone number? ')
# phone_number = '1234567890'
# digit_mapping = {
#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four',
#     '5': 'Five',
#     '6': 'Six',
#     '7': 'Seven',
#     '8': 'Eight',
#     '9': 'Nine'
# }
# output = ''
# for character in phone_number:
#     # the '!' in get method is what is got when there is not mapping for that character
#     # in this case 0 is not mapped
#     output += digit_mapping.get(character, '!') + ' '
# print(output)

# # Emojis
# message = input('> ')
# words = message.split(' ')
# print(words)
# # on mac: ctrl+command+space to bring up list of emojis
# # on windows: windowskey+period
# emojis = {
#     ':)': '😊',
#     ':(': '😢'
# }
# output = ''
# for word in words:
#     output += emojis.get(word, word) + ' '
# print(output)

# # Functions (def is short for define)
# # double line break after function definition is best practice
# # Difference between function and method: methods are associated with Objects of the class they belong to.
# # Functions are not associated with any Object
# def greet_user():
#     print('Hi there!')
#     print('Welcome aboard')
#
#
# print('Function call:')
# greet_user()
# print('Finish')

# # Parameters - are place holders in methods/functions for receiving information (place holder name in greet_user
# # Argument - are the actual pieces of information supplied to method/function (value of user_name)
# # ?Find out if methods/functions can be overloaded?
# def greet_user(first_name, last_name):
#     print(f'Hello {first_name} {last_name}!')
#     print('Welcome aboard')
#
#
# print('Start')
# user_first_name = 'Eric'
# user_last_name = 'Smith'
# greet_user(user_first_name, user_last_name)
# greet_user('Rosa', 'Linda')
# print('Finish')

# # Keyword Arguments - may only mix keyword arguments and positional arguments if
# # positional argument comes first ex: greet_user('Rosa', last_name='Linda')
# # this is wrong: greet_user(last_name='Linda', 'Rosa')
# def greet_user(first_name, last_name):
#     print(f'Hello {first_name} {last_name}!')
#     print('Welcome aboard')
#
#
# print('Start')
# user_first_name = 'Eric'
# user_last_name = 'Smith'
# # See how the position of the parameters don't line up with the actual function parameters
# greet_user(last_name=user_first_name, first_name=user_last_name)
# greet_user('Rosa', 'Linda')
# print('Finish')

# # Return Statement -
# def square(number):
#     return number * number
#
#
# result = square(3)
# print(result)
# print(square(3))

# # Return Statement Default - by default a function returns None. Happens when there is no return statement
# # so when print(square(3)) is called it actually print the return statement None
# def square(number):
#     print(number * number)
#
#
# print(square(3))

# # Creating Reusable Functions
# def emoji_conversion(user_input):
#     words = user_input.split(' ')
#     output = ''
#     emojis = {
#         ':)': '😊',
#         ':(': '😢'
#     }
#     for word in words:
#         output += emojis.get(word, word) + ' '
#     return output
#
#
# coded_input = 'What a great day :)'
# print(emoji_conversion(user_input=coded_input))

# # Exceptions
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0')
# except ValueError:
#     print('InvalidValue error')

# # Comments
# # Do not comment the obvious
# # Use comment to explain whys and hows
# print('Sky is blue')
