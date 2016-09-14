from __future__ import absolute_import, unicode_literals 

import unittest

from boil import api
from boil import util


class TestInsertIndented(unittest.TestCase):

    def test_online(self):
        src = 'def somefunc()'
        index = src.index('(')+1

        blockoneline = 'asdfasdf, asdfas'

        blockmultiline = 'a,\nb,\nc'

        result = util.insert_indented(src,blockoneline,index)
        expected = 'def somefunc(asdfasdf, asdfas)'
        self.assertEqual(result, expected)
        

    def test_multiline(self):
        src = 'def somefunc()'
        index = src.index('(')+1

        blockmultiline = 'a,\nb,\nc'

        result = util.insert_indented(src,blockmultiline,index)
        expected = 'def somefunc(a,\n             b,\n             c)'
        self.assertEqual(result, expected)
    
class Stub(object):
    pass

class TestBasicBoil(unittest.TestCase):
    tests = Stub()
    expectations = Stub()
    tests.noargs = 'MyClass'
    expectations.noargs = '''class MyClass(object):
    def __init__(self):
        super(MyClass, self).__init__()'''

    tests.onlyargs = 'MyClass arg1 arg2 arg3'
    expectations.onlyargs = '''class MyClass(object):
    def __init__(self,
                 arg1,
                 arg2,
                 arg3):
        super(MyClass, self).__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3'''
    
    tests.onlykwargs = 'MyClass, kwarg1 kwarg2 kwarg3'
    expectations.onlykwargs = '''class MyClass(object):
    def __init__(self,
                 kwarg1=None,
                 kwarg2=None,
                 kwarg3=None):
        super(MyClass, self).__init__()
        self.kwarg1 = kwarg1
        self.kwarg2 = kwarg2
        self.kwarg3 = kwarg3'''
    
    tests.argsandkwargs = 'MyClass arg1 arg2 arg3, kwarg1 kwarg2 kwarg3'
    expectations.argsandkwargs = '''class MyClass(object):
    def __init__(self,
                 arg1,
                 arg2,
                 arg3,
                 kwarg1=None,
                 kwarg2=None,
                 kwarg3=None):
        super(MyClass, self).__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.kwarg1 = kwarg1
        self.kwarg2 = kwarg2
        self.kwarg3 = kwarg3'''

    def _test_and_assert(self, attr):
        test = api.boil(getattr(self.tests, attr))
        expected = getattr(self.expectations, attr)
        self.assertEqual(test,expected)

    def test_noargs(self):
        attr = 'noargs'
        self._test_and_assert(attr)

    def test_onlyargs(self):
        attr = 'onlyargs'
        self._test_and_assert(attr)

    def test_onlykwargs(self):
        attr = 'onlykwargs'
        self._test_and_assert(attr)

    def test_argsandkwargs(self):
        attr = 'argsandkwargs'
        self._test_and_assert(attr)


class TestTypesBoil(unittest.TestCase):
    tests = Stub()
    expectations = Stub()

    tests.noargs = 'MyClass(object, MyMixin)'
    expectations.noargs = '''class MyClass(object, MyMixin):
    def __init__(self):
        super(MyClass, self).__init__()'''

    tests.onlyargs = 'MyClass(object, MyMixin) arg1 arg2 arg3'
    expectations.onlyargs = '''class MyClass(object, MyMixin):
    def __init__(self,
                 arg1,
                 arg2,
                 arg3):
        super(MyClass, self).__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3'''
    
    tests.onlykwargs = 'MyClass(object, MyMixin), kwarg1 kwarg2 kwarg3'
    expectations.onlykwargs = '''class MyClass(object, MyMixin):
    def __init__(self,
                 kwarg1=None,
                 kwarg2=None,
                 kwarg3=None):
        super(MyClass, self).__init__()
        self.kwarg1 = kwarg1
        self.kwarg2 = kwarg2
        self.kwarg3 = kwarg3'''
    
    tests.argsandkwargs = 'MyClass(object, MyMixin) arg1 arg2 arg3, kwarg1 kwarg2 kwarg3'
    expectations.argsandkwargs = '''class MyClass(object, MyMixin):
    def __init__(self,
                 arg1,
                 arg2,
                 arg3,
                 kwarg1=None,
                 kwarg2=None,
                 kwarg3=None):
        super(MyClass, self).__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.kwarg1 = kwarg1
        self.kwarg2 = kwarg2
        self.kwarg3 = kwarg3'''
    
    def _test_and_assert(self, attr):
        test = api.boil(getattr(self.tests, attr))
        expected = getattr(self.expectations, attr)
        self.assertEqual(test,expected)

    def test_noargs(self):
        attr = 'noargs'
        self._test_and_assert(attr)

    def test_onlyargs(self):
        attr = 'onlyargs'
        self._test_and_assert(attr)

    def test_onlykwargs(self):
        attr = 'onlykwargs'
        self._test_and_assert(attr)

    def test_argsandkwargs(self):
        attr = 'argsandkwargs'
        self._test_and_assert(attr)


if __name__ == '__main__':
    unittest.main()
