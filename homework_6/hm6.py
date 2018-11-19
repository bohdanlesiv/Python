class Context():
    def _validator(self,val):
        pass
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self._validator(v)
        self._args = kwargs

    def __enter__(self, **kwargs):
            globals().update(self._args)

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

    def __exit__(self, exc_type, exc_val, exc_tb):
        for i in self._args:
            globals().pop(i)
    def __next__(self):
        try:
            key = list(self._args.keys())[self.index]
            val = self._args.get(key)
        except IndexError:
            raise StopIteration
        self.index += 1
        return tuple((key, val))

## Test1
try:
   with Context (x1=3,x3=4,x5=6) as c:
        print(x1,x3,x5)
   print('Passed')
except:
    print('Failed')

## Test2
try:
    with Context (x1=3,x3=4,x5=6) as c:
         pass
    print(x1,x3,x5)
    print('Failed')
except:
    print('Passes')
