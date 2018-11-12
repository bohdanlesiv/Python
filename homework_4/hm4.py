class Context():
    def _validator(self,val):
        pass
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self._validator(v)
        self._args = kwargs

    def __getattr__(self, item):
        return self._args[item]

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key not in ['_args', 'index']:
            self._validator(value)
            self._args[key] = value

    def __len__(self):
        return len(self._args)

    def __str__(self):
        class_name = str(self.__class__.__name__)
        args = ','.join(list(map(lambda kv: str(kv[0]) + '=' + str(kv[1]), self._args.items())))
        return '{} ({})'.format(class_name, args)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            key = list(self._args.keys())[self.index]
            val = self._args.get(key)
        except IndexError:
            raise StopIteration
        self.index += 1
        return tuple((key, val))



class RealContext(Context):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def _validator(self,val):
        print('Real_val')
        is_valitd = isinstance(val,(int,float))
        if not is_valitd:
            raise TypeError



class ComplexContext(Context):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def _validator(self,val):
        print('Complex_val')
        is_valitd = isinstance(val,(complex))
        if not is_valitd:
            raise TypeError


class ValidationError(Exception):
    pass

class NumberContext(RealContext,ComplexContext):
     def __init__(self,**kwargs):
         super().__init__(**kwargs)

     def _validator(self,val):
         is_RealContext = True
         is_ComplexContext = True
         is_NumberContext = True

         try:
          super()._validator(val)
         except TypeError:
             is_RealContext =False

         try:
          super(RealContext,self)._validator(val)
         except TypeError:
             is_ComplexContext =False

         is_NumberContext  =  is_ComplexContext or is_RealContext

         if not  is_NumberContext:
             raise ValidationError


