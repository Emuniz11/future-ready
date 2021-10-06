# print("Eric Muniz")
# print('o----')
# print(' ||||')
# print('*' * 10)
#
# price = 10
# price = 20
# rating = 4.9
# name = 'Hank'
# is_published = True
# print(price)
#
# full_name = 'John Smith'
# age = 20
# is_new = True
#
# name = input('What is your name? ')
# print('Hi ' +  name)
# f_color = input('What is your favorite color? ')
# print(name + '\'s favorite color is ' + f_color)

# # Get Type and Casting
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2021 - int(birth_year)
# print(type(age))
# print('You are ' + str(age) + ' years old')

# wieght_lbs = input('How many pounds do you wiegh? ')
# weight_kg = float(wieght_lbs) * .454
# print('You weigh ' + str(weight_kg) + " kilograms!")

# # Single and Double Quotes
# course = 'Python\'s Course for Beginners'
# print(course)
# # or
# course = "Python's Course for Beginners"
# print(course)
# # or
# course = 'Python"s course for beginners'
# print(course)

# # Multi-line string
# course = '''
# Hi Eric
#
# Here is my first email to you.
#
# Thank you!
# '''
# print(course)

# # String Manipulation
# course = 'Python for beginners'
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[3:])
# print(course[:5])

# name = 'Jennifer'
# print(name[1:-1])

# # Formatted Strings
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# print(message)
# msg = f'{first} [{last}] is a coder'
# print(msg)

# # Type length: len (general purpose)
# course = 'Python for Beginners'
# print(course)
# print(len(course))
# print(course.upper())
# print(course.lower())
# # find/replace is case sensitive
# print(course.find('n'))
# print(course.find('Beginners'))
# print(course.replace('Beginners', 'Absolute Beginners'))
# print('Python' in course)
# print('python' in course)

# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)
# x = 10
# x = x + 3
# print(x)
# # Enhanced Assignment Operator
# x = 10
# x += 3
# print(x)
# x -= 3
# print(x)

# # Operation Precedence
# # parenthesis > exponents > mult/div > add/sub
# x = 10 + 3 * 2
# print(x)
# x = 10 + 3 * 2 ** 2
# print(x)
# x = (2 + 3) * 10 - 3
# print(x)

# # Round/Absolute Value
# # Python 3 math module is different from Python 2 math module!
# import math
# x = -2.9
# print(round(x))
# print(abs(x))
# print(math.ceil(2.6))
# print(math.floor(2.6))

# # if/elif/else Statement
# is_hot = False
# is_cold = False
# if is_hot:
#     print('It\'s a hot day.')
#     print('Drink plenty of water!')
# elif is_cold:
#     print('It\'s a cold day.')
#     print('Wear warm cloths!')
# else:
#     print('It\'s a lovely day!')
# print('Enjoy your day.')

# house_cost = 1000000
# has_good_credit = False
# down_payment = 0.0
# if has_good_credit:
#     print('You have good credit.')
#     down_payment = float(house_cost) * .1
# else:
#     print('You have not so good credit.')
#     down_payment = float(house_cost) * .2
# print(f'Your down payment will be ${down_payment} on a ${house_cost} house')

# # Logical Operators and/or/not
# has_high_income = False
# has_good_credit = True
# has_criminal_record = False
# if has_good_credit and has_high_income:
#     print('Eligible for loan')
# if has_good_credit or has_high_income:
#     print('Eligible for smaller loan')
# if has_good_credit and not has_criminal_record:
#     print('You are not a criminal')

# # Comparison Operators
# tep = 30
# if tep > 30:
#     print('It\'s a hot day.')
# elif tep == 30:
#     print('It\'s 30 out here.')
# else:
#     print('It\'s not a hot day.')

# name = 'An' * 30
# if len(name)<3:
#     print('Name is too short.')
# elif len(name)>50:
#     print('Name is too long.')
# else:
#     print('Name looks good!')

# weight = input('How much do you weigh? ')
# scale = input('Is that in (L)bs or (K)g: ')
# mult = .454
#
# if scale.upper() == 'L':
#     weight = float(weight) * mult
#     print('You are ' + str(weight) + ' kilograms.')
# elif scale.upper() == 'K':
#     weight = float(weight) / mult
#     print('You are ' + str(weight) + ' pounds.')

# # While Loops
# i = 1
# while i<=5:
#     print('*' * i)
#     i += 1
# print('DONE')

# print('Game: \nGuess a number between 1 and 10\nYou will only have three guesses!')
# guess_count = 0
# guess_limit = 3
# secret_number = 5
# guess = -1
# while guess_count<guess_limit:
#     guess = int(input('What is your guess? '))
#     if guess != secret_number:
#         guess_count += 1
#     elif guess == secret_number:
#         print('You win!')
#         break
# else:
#     print('You lose...')

# started = False
# while True:
#     command = input('> ').lower()
#     if command == 'help':
#         print('''
# Commands:
# start
# stop
# quit
#         ''')
#     elif command == 'stop' and not started:
#         print('Car is already stopped.')
#     elif command == 'start':
#         if started:
#             print('Car is already started.')
#         else:
#             started = True
#             print('Car started... let\'s go!')
#     elif command == 'stop':
#         if not started:
#             print('Car is already stopped.')
#         else:
#             started = False
#             print('Car stopped.')
#     elif command == 'quit':
#         break
#     else:
#         print('Invalid input.')

# # For Loop
# for item in [1, 5, 10, 3, 6, 9]:
#     print(item)

# # range(exclusive) - range(inclusive, exclusive) - range(inclusive, exclusive, step)
# for item in range(5, 10, 2):
#     print(item)

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f'This is the total: {total}')

# # Nested Loop
# x = [0, 1, 2, 3]
# y = [0, 1, 2, 3]
# for x_num in x:
#     for y_num in y:
#         print(f'({x[x_num]},{y[y_num]})')
# or
# for x in range(4):
#     for y in range(4):
#         print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]
# for index in range(len(numbers)):
#     i = 0
#     for num in range(numbers[index]):
#         i += 1
#         if i == numbers[index]:
#             print('*' * i)

# numbers = [5, 2, 5, 2, 2]
# for num in numbers:
#     output = ''
#     for count in range(num):
#         output += 'x'
#     print(output)

# # Lists
# names = ['John', 'Bob', 'Mosh', 'Sam', 'Marry']
# print(names[-1])
# print(names[0])
# print(names[1:4])
# print(names[:-1])
# names[0] = 'Jon'
# print(names[0])

# numbers = [13, 5, 10, 2, 8, 1, 20]
# largest_number = 0
# for num in numbers:
#     if largest_number < num:
#         largest_number = num
# print(f'This is the largest number: {largest_number}')

# Stopped at 2:02:11 2D Lists