import time
import os
import threading
from functools import wraps

class ThreadSafeLogger:
    enabled = True
    logs = []
    mode = 'console'  # or 'memory'
    lock = threading.RLock()

    @staticmethod
    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if ThreadSafeLogger.enabled:
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                log = f"{func.__name__} took {(end - start) * 1000} milliseconds to run."
                with ThreadSafeLogger.lock:
                    if ThreadSafeLogger.mode == 'console':
                        print(log)
                    elif ThreadSafeLogger.mode == 'memory':
                        ThreadSafeLogger.logs.append(log)
                return result
            else:
                return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def log_calls(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if ThreadSafeLogger.enabled:
                log = f"{func.__name__} was called."
                with ThreadSafeLogger.lock:
                    if ThreadSafeLogger.mode == 'console':
                        print(log)
                    elif ThreadSafeLogger.mode == 'memory':
                        ThreadSafeLogger.logs.append(log)
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def write_logs():
        logs_dir = 'logs'
        if not os.path.exists(logs_dir):
            os.mkdir(logs_dir)
        filename = os.path.join(logs_dir, time.strftime('%Y%m%d%H%M%S.txt', time.gmtime()))
        with open(filename, 'w') as f:
            with ThreadSafeLogger.lock:
                for log in ThreadSafeLogger.logs:
                    f.write(log + '\n')
        return filename
