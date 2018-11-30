import datetime
import abc


class Product():
    def __init__(self):
        self.vendod ='Compus'
        self.release_date =datetime.datetime.now()


class Monitor(Product):
    def __init__(self):
        super().__init__()
        self.model = None
        self.diagonal =None

class Keyboard(Product):
    def __init__(self,type):
        super().__init__()
        self.type =type


class Keyboard_PC(Product):
    def __init__(self):
        super().__init__('PC')


class Keyboard_Bluetooth(Product):
    def __init__(self):
        super().__init__('Bluetooth')


class Computer_Case(Product):
    def __init__(self,type):
        super().__init__()
        self.type =type

class Computer_Case_Mini_tower(Computer_Case):
    def __init__(self):
        super().__init__('Mini tower')


class Computer_Case_Tower(Computer_Case):
    def __init__(self):
        super().__init__('Tower')


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ExceptioProductNotSupportted(Exception):
    pass
class Factory (metaclass=Singleton):
    product =None
    def __init__(self,name):
        self.name = name
    def create(self,_product_type):
        if  _product_type == 'Monitor':
            product = Monitor()
        elif _product_type == 'Keyboard_PC':
            product = Keyboard_PC()
        elif _product_type == 'Keyboard_Bluetooth':
            product = Keyboard_Bluetooth()
        elif _product_type == 'Computer_Case_Mini_tower':
            product = Computer_Case_Mini_tower()
        elif _product_type == 'Computer_Case_Mini_tower':
            product = Computer_Case_Mini_tower()
        elif _product_type == 'Computer_Case_Tower':
            product = Computer_Case_Tower()
        else:
            raise ExceptioProductNotSupportted

        product.vendod =self.name
        return product


fc =Factory('My')

