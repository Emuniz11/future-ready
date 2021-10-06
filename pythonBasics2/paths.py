from pathlib import Path

# There are two kinds of paths: Absolut and Relative

# Absolute ex.
# for Windows: c:\Program Files\Microsoft
# for Mac: /usr/local/bin

# This application will give examples of Relative Paths

# check to see if directory exists
# path = Path("ecommerce")
# print(path.exists())
#
# path = Path("ecommerce1")
# print(path.exists())

# create a directory
# path = Path('emails')
# print(path.mkdir())

# remove directory
# path.rmdir()

# file search
path = Path()
# * will search ever thing, all file and all directories
# for file in path.glob('*'):
#     print(file)

# *.* will get all the files and not the directories
# for file in path.glob('*.*'):
#     print(file)

# *.py will get all .py files
# for file in path.glob('*.py'):
#     print(file)

# *.xls will get all excel spreadsheets
# print(path.glob('*.xls'))
