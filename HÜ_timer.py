import functools
import time

def decorator_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Funktion {func.__name__} wurde in {duration}s ausgeführt")
        return value
    return wrapper

@decorator_time
def add(a,b,c,*args):
    ergebnis = a+b+c
    print(ergebnis)
    print("Ungültige Übergabe: ", args)

add(1,2,3,4)