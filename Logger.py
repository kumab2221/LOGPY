import time
from functools import wraps
import os

class Logger:
    enabled = True
    logs = []
    mode = 'console'  # or 'memory'

    @staticmethod
    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if Logger.enabled:
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                log = f"{func.__name__} took {(end - start) * 1000} milliseconds to run."
                if Logger.mode == 'console':
                    print(log)
                elif Logger.mode == 'memory':
                    Logger.logs.append(log)
                return result
            else:
                return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def log_calls(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if Logger.enabled:
                log = f"{func.__name__} was called."
                if Logger.mode == 'console':
                    print(log)
                elif Logger.mode == 'memory':
                    Logger.logs.append(log)
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def write_logs():
        logs_dir = 'logs'
        if not os.path.exists(logs_dir):
            os.mkdir(logs_dir)
        filename = os.path.join(logs_dir, time.strftime('%Y%m%d%H%M%S.txt', time.gmtime()))
        with open(filename, 'w') as f:
            for log in Logger.logs:
                f.write(log + '\n')
        return filename
