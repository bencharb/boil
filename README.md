# boil

~~~~
In [1]: from boil import boil
In [2]: boil(MyClass arg1 arg2 arg3, kwarg1 kwarg2 kwarg3)
Out[2]: 
class MyClass(object):
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
        self.kwarg3 = kwarg3
~~~~

Then copy/paste the output into your editor. 

WHY?
--------
Saves 1-5 minutes of time. (2m of typing, 30s of fixing typos, 
and possibly 2.5m fixing hidden mistakes like ```def __init__(arg1,arg2...)```


TODO
--------

1. Magics
~~~~
In [1]: % boil MyClass arg1 arg2 arg3, kwarg1 kwarg2 kwarg3
In [ ]: class MyClass(object):
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
		        self.kwarg3 = kwarg3
~~~~