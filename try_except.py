def devide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Error: You can not devide by zero')

print(devide(4, 2))
print(devide(10, 3))
print(devide(5, 0))
print(devide(33, 2))