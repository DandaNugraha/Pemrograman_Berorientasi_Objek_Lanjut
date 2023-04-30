# NotImplementedError
try:
    raise NotImplementedError
except NotImplementedError:
    print("NotImplementedError raised")

# OSError
try:
    raise OSError
except OSError:
    print("OSError raised")

# OverflowError
try:
    num = int(1e100)
except OverflowError:
    print("OverflowError raised")

# RecursionError
def recurse():
    try:
        recurse()
    except RecursionError:
        print("RecursionError raised")

# ReferenceError
try:
    x = 10
    print(x)
except ReferenceError:
    print("ReferenceError raised")

# RuntimeError
try:
    raise RuntimeError
except RuntimeError:
    print("RuntimeError raised")

# StopAsyncIteration
try:
    raise StopAsyncIteration
except StopAsyncIteration:
    print("StopAsyncIteration raised")

# StopIteration
try:
    raise StopIteration
except StopIteration:
    print("StopIteration raised")

# SyntaxError
try:
    eval('print(')
except SyntaxError:
    print("SyntaxError raised")

# SystemError
try:
    raise SystemError
except SystemError:
    print("SystemError raised")

# SystemExit
try:
    raise SystemExit
except SystemExit:
    print("SystemExit raised")

# TabError
try:
    s = '\t'
    print(s)
except TabError:
    print("TabError raised")
    
# TypeError
try:
    a = 5 + 's'
except TypeError:
    print("TypeError raised")

# UnboundLocalError
try:
    x = 10
    def foo():
        x += 1
        print(x)
    foo()
except UnboundLocalError:
    print("UnboundLocalError raised")

# UnicodeErrors
try:
    a = '\u00E9'
except UnicodeError:
    print("UnicodeError raised")

# UnicodeEncodeError
try:
    b = '\u00E9'
    b.encode("ascii")
except UnicodeEncodeError:
    print("UnicodeEncodeError raised")

# UnicodeDecodeError
try:
    c = b'\xE9'
    c.decode("ascii")
except UnicodeDecodeError:
    print("UnicodeDecodeError raised")

# UnicodeTranslateError
try:
    d = '\u00E9'
    e = d.encode("ascii","replace")
except UnicodeTranslateError:
    print("UnicodeTranslateError raised")

# ValueError
try:
    f = int('s')
except ValueError:
    print("ValueError raised")

# ZeroDivisionError
try:
    g = 1/0
except ZeroDivisionError:
    print("ZeroDivisionError raised")
