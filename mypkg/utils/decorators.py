# useful decorators in python 
from functools import wraps
from time import time

def timing(f):
    """
    decorator to measure the time taken by a function
    from https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
    usage:
    @timing
    def my_function():
        pass
    or 
    my_function = timing(my_function)
    """
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap