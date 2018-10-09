from hm1 import Stack
from hm1 import LimitExceedError, EmptyStackError

import unittest


class TestStackMethods(unittest.TestCase):
    def test_init_default(self):
        """testcase1: Crete object with default attrs."""
        Stack_default = Stack()
        self.assertEqual(Stack_default.type(), object)
        self.assertEqual(Stack_default._limit, None)

    def test_init_param(self):
        """testcase2: Crete object data_type=int, limit=11"""
        Stack_default = Stack(data_type=int, limit=11)
        self.assertEqual(Stack_default.type(), int)
        self.assertEqual(Stack_default._limit, 11)

    def test_init_add(self):
        """testcase3: Add two elements into stack and validate amount"""
        Stack_default = Stack(data_type=int, limit=11)
        Stack_default.push(1)
        Stack_default.push(2)
        self.assertEqual(Stack_default.count(), 2)

    def test_pull(self):
        """testcase4: Add two elements into stack and delete one , expected result
           deleteted element is correct and amount is equal 2
        """
        Stack_default = Stack(data_type=int, limit=11)
        Stack_default.push(1)
        Stack_default.push(2)
        Stack_default.push(3)
        self.assertEqual(Stack_default.pull(), 3)
        self.assertEqual(Stack_default.count(), 2)

    def test_type_exception(self):
        """testcase5:Raise TypeError exception"""
        Stack_default = Stack(data_type=int, limit=1)
        with self.assertRaises(TypeError):
            Stack_default.push('x')

    def test_limit_exception(self):
        """testcase6:Raise LimitExceedError exception"""
        Stack_default = Stack(data_type=str, limit=1)
        Stack_default.push('A')
        with self.assertRaises(LimitExceedError):
            Stack_default.push('x')

    def test_empty_stack_exception(self):
        """testcase7:Raise EmptyStackError exception"""
        Stack_default = Stack(data_type=str, limit=1)
        Stack_default.push('A')
        Stack_default.pull()
        with self.assertRaises(EmptyStackError):
            Stack_default.pull()


    def test_clear(self):
        """testcase8:Clear method test"""
        Stack_default = Stack(data_type=int, limit=11)
        Stack_default.push(1)
        Stack_default.push(2)
        Stack_default.push(3)
        Stack_default.clear()
        self.assertEqual(Stack_default.count(), 0)

    def test_type(self):
        """testcase8:Clear method test"""
        Stack_default = Stack(data_type=bool, limit=11)
        Stack_default.push(True)
        Stack_default.push(True)
        Stack_default.push(False)
        self.assertEqual(Stack_default.type(),bool )

if __name__ == '__main__':
    unittest.main()
