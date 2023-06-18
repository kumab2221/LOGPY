import time

from Logger import Logger
import analyze

@Logger.timer
@Logger.log_calls
def slow_function():
    time.sleep(1)

@Logger.timer
@Logger.log_calls
def fast_function():
    pass

class MyClass:
    data = 2
    @Logger.timer
    @Logger.log_calls
    def my_method(self, arg1, arg2):
        time.sleep(1)
        return arg1 + arg2
    @classmethod
    @Logger.timer
    @Logger.log_calls
    def my_classmethod(cls, arg1, arg2):
        time.sleep(1)
        return cls.data * (arg1 + arg2)

Logger.enabled = True
Logger.mode = 'console'  # ログをコンソールに出力

slow_function()
fast_function()

Logger.mode = 'memory'  # ログをメモリに蓄積
slow_function()
fast_function()
slow_function()
fast_function()
slow_function()
fast_function()
slow_function()
fast_function()
slow_function()
fast_function()
slow_function()
fast_function()
slow_function()
fast_function()
slow_function()
fast_function()
slow_function()
fast_function()
slow_function()
fast_function()
slow_function()
fast_function()

mc = MyClass()
print(mc.my_method(3,4))
print(mc.my_classmethod(3,4))

filename = Logger.write_logs()  # ログをファイルに書き出す

analyze.analyze_logs(filename)


