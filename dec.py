from typing import Callable

def decorator(word):
    def wrapper1(func: Callable):
        def wrapper2(*args, **kwargs):
            print(f"word: {word}")
            result = func(*args, **kwargs)
            print("После вызова")
            return result
    
        return wrapper2
    return wrapper1
    


@decorator(word="")
def shlyuha():
    print("Вызов функции")
    return "stroku"


a = shlyuha()