import inspect

class WrrongAtrrs (Exception):
    pass
class_na = input("Plese enter class name: ")

class_attrs = {}

def get_class_attrs(self):
    txt = 'Class <' + self.__class__.__name__ + '>\n'
    for i in inspect.getmembers(self):
        # Ignores anything starting with underscore
        # (that is, private and protected attributes)
        if not i[0].startswith('_'):
            # Ignores methods
            if not inspect.ismethod(i[1]):
                txt = txt + str(i[0]) + '=' + str(i[1]) + '\n'
    return txt

def validate_params(attr_name_value):
    attr_nm_split = attr_name_value.lstrip().split('=')
    attr_name = attr_nm_split[0]
    attr_value = attr_nm_split[1]
    try:
       exec(attr_name + '=' + attr_value)

    except:
        raise WrrongAtrrs

    return attr_name, attr_value

while True:
    attr_name_value = input("Please add attr name and value")
    if not attr_name_value:
        break

    try:
        attr_name, attr_value =validate_params(attr_name_value)
        class_attrs.update({attr_name:attr_value})
    except:
        print('Wrong attrs , please try again')
        continue




def create_object(class_name):
    def create_class_attr(attr_name):
        return  type(class_name,(),attr_name)
    return create_class_attr



ClassName = create_object(class_na)

My_Class = ClassName(class_attrs)

My_Class.__str__ = get_class_attrs

x=My_Class()

print(x)

