from ctypes import c_char_p, cdll

hello_lib = cdll.LoadLibrary("hello.so")
hello = hello_lib.hello
print hello("world")                    # this won't work!

# ==> need to set return type...
hello.restype = c_char_p
assert hello("world") == "hello, world"
