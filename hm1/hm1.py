class LimitExceedError(Exception):
    """Raised when the limit is over or not defined"""
    pass


class EmptyStackError(Exception):
    """Raised when the array of objects defined in Stack is empty """
    pass


class Stack(object):
    """The class  Stack"""

    def __init__(self, data_type=object, limit=None):
        """ use for create class Stack parameters data_type (define type of object def. is object)
            limit define amount of elements
        """
        self._data_type = data_type
        self._limit = limit
        self._data = []

    def _push(self, item):
        """ private method , used for data type validation of adding elements and checks amount of elements
           by limit attribute . Generates two exceptions   LimitExceedError and EmptyStackError in case when conditions
           are not met
         """
        if self._limit <= len(self._data):
            raise LimitExceedError

        if type(item) != self._data_type:
            raise TypeError

    def push(self, item):
        "Add element in the beginning of queue"
        self._push(item)
        self._data.append(item)

    def pull(self):
        """Remove and return the last element of queue , in case if list of erlemnts is empty EmptyStackError
        will be generated
        """
        if len(self._data) == 0:
            raise EmptyStackError

        del_item_lats = self._data[-1]
        del self._data[-1]

        return del_item_lats

    def count(self):
        "Return amount of element in queue"
        return len(self._data)

    def clear(self):
        """remove all elements from items list"""
        del self._data[:]

    def type(self):
        "Return type of Stack "
        return self._data_type

    def __str__(self):
        return 'Stack<' + str(self._data_type) + '>'

