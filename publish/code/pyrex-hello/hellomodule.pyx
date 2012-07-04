cdef extern from "hello.h":
    char * hello(char *s)

def hello_fn(s=None):
    return hello(s)
