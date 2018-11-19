class ConstAttributeError (Exception):
    pass
class Const(type):
    def __setattr__(self, name, value):
        raise ConstAttributeError


class MyClass(metaclass=Const):
    x1 =2
    x3 =4



## test1

try:
    MyClass.x1=5
    print('Failed')
except ConstAttributeError:
    print('Passed')


try:
    MyClass().x1=5
    print('Passed')
except :
    print('Failed')
