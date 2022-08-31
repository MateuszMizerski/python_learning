from datetime import datetime, timedelta


def func_name_logger(func):

    def f1(*args, **kwargs):
        print('[INFO] Name of function: {}'.format(func.__name__))
        func(*args, **kwargs)
    return f1


def time_checker(timeout: int):

    def decor(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            print('Start time: {}'.format(start.strftime("%H:%M:%S")))
            func(*args, **kwargs)
            end = datetime.now()
            print('End time: {}'.format(end.strftime("%H:%M:%S")))
            max_time = start + timedelta(seconds=timeout)
            print('Exceeded') if max_time < end else print('Pass')
        return wrapper
    return decor


class Dox:

    def __init__(self, func):
        self.f = func
        print('[INFO] Documentation:\n {}\n###END OF DOX###'.format(func.__doc__))

    def __call__(self, *args, **kwargs):
        self.f(*args, **kwargs)


class WrapperArgs:

    def __init__(self, *args, **kwargs):
        print(args, str(kwargs.items()))

    def __call__(self, func):
        print('[INFO] Name of function: {}'.format(func.__name__))

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

        return wrapper
