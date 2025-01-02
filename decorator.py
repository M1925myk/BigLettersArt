def stringify(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)
    return wrapper

@stringify
def bugagi(a, b):
    return a + b


result = bugagi(15, 30)
print(result)
print(type(result))
