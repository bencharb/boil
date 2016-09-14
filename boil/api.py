from __future__ import absolute_import, unicode_literals 
from boil import transform 

__all__ = ('boil', 'boil_print',)

def boil_class(s):
    data = transform.parse_string(s)
    oldkwargs = data['kwargs']
    data['kwargs'] = {k:None for k in oldkwargs}
    return transform.create_class(**data)


def boil(s):
    obj = boil_class(s)
    return obj.render()


def boil_print(s):
    print boil(s)

#exmaple: boil_print('MyClass arg1 arg2 arg3, kwarg1 kwarg2 kwarg3')

