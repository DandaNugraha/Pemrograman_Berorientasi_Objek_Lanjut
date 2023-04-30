1. NotImplemented Error

Contoh:
python
class MyClass:
    def __eq__(self, other):
        return NotImplemented

obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)


Output:

NotImplemented


2. OSError

Contoh:
python
import os

try:
    os.mkdir("mydir")
except OSError as error:
    print(error)


Output:

[Errno 17] File exists: 'mydir'


3. OverflowError

Contoh:
python
import math

try:
    math.exp(1000)
except OverflowError as error:
    print(error)


Output:

math range error


4. RecursionError

Contoh:
python
def recursive_function(n):
    if n == 0:
        return
    recursive_function(n-1)

recursive_function(1000)


Output:

RecursionError: maximum recursion depth exceeded in comparison


5. ReferenceError

Contoh:
python
def my_function():
    my_var = "Hello"
    return my_var

my_var = my_function()
print(my_var)
del my_var
print(my_var)


Output:

Hello
NameError: name 'my_var' is not defined


6. RuntimeError

Contoh:
python
def my_function():
    raise RuntimeError("Something went wrong")

try:
    my_function()
except RuntimeError as error:
    print(error)


Output:

Something went wrong


7. StopAsyncIteration

Contoh:
python
async def my_async_generator():
    for i in range(5):
        yield i
    raise StopAsyncIteration

async def my_async_function():
    async for i in my_async_generator():
        print(i)

asyncio.run(my_async_function())


Output:

0
1
2
3
4


8. StopIteration

Contoh:
python
my_list = [1, 2, 3]
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


Output:

1
2
3
StopIteration


9. SyntaxError

Contoh:
python
if True
    print("Hello")


Output:

SyntaxError: invalid syntax


10. SystemError

Contoh:
python
def my_function():
    return 1/0

try:
    my_function()
except SystemError as error:
    print(error)


Output:

NULL result without error in PyObject_Call


11. SystemExit

Contoh:
python
import sys

sys.exit(0)
print("Hello")


Output:

Process finished with exit code 0


12. TabError

Contoh:
python
if True:
print("Hello")


Output:

TabError: inconsistent use of tabs and spaces in indentation


13. TypeError

Contoh:
python
my_list = [1, 2, 3]
my_dict = {1: "one", 2: "two", 3: "three"}

print(my_list + my_dict)


Output:

TypeError: can only concatenate list (not "dict") to list


14. UnboundLocalError

Contoh:
python
def my_function():
    print(my_var)
    my_var = "Hello"

my_function()


Output:

UnboundLocalError: local variable 'my_var' referenced before assignment


15. UnicodeErrors

Contoh:
python
my_string = "Héllo"

try:
    my_string.encode('ascii')
except UnicodeEncodeError as error:
    print(error)

try:
    my_string.decode('ascii')
except UnicodeDecodeError as error:
    print(error)


Output:

'ascii' codec can't encode character '\xe9' in position 1: ordinal not in range(128)
'ascii' codec can't decode byte 0xe9 in position 1: ordinal not in range(128)


16. UnicodeEncodeError

Contoh:
python
my_string = "Héllo"
my_string.encode('ascii')


Output:

'ascii' codec can't encode character '\xe9' in position 1: ordinal not in range(128)


17. UnicodeDecodeError

Contoh:
python
my_string = b'H\xc3\xa9llo'
my_string.decode('ascii')


Output:

'ascii' codec can't decode byte 0xc3 in position 1: ordinal not in range(128)


18. UnicodeTranslateError

Contoh:
python
my_string = "Héllo"
my_string.translate({233: None})


Output:

ValueError: {233: None} is not a valid argument for translate()


19. ValueError

Contoh:
python
int("Hello")


Output:

ValueError: invalid literal for int() with base 10: 'Hello'


20. ZeroDivisionError

Contoh:
python
1/0


Output:

ZeroDivisionError: division by zero