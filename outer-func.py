def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func("Hi")
hello_func = outer_func("Hello")

# print(my_func.__name__)
hi_func()
hello_func()