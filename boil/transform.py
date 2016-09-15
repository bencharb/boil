# coding: utf-8
from __future__ import absolute_import, unicode_literals 
import re

from boil import util
from boil import models
from boil import exc

__all__ = ('create_class','parse_string',)

def create_init_method(classname, args=None, kwargs=None):
    args = util.insert_arg('self', args or ())
    func = models.Function(name='__init__', args=args, kwargs=kwargs)
    func.code_block = models.Class.render_init_block(classname, args=args, kwargs=kwargs)
    return func

def create_class(name=None, types=('object',), args=None, kwargs=None):
    init_method = create_init_method(name, args=args, kwargs=kwargs)
    return models.Class(name=name, types=types, methods=(init_method,))

rx_classname = '(?P<name>\w+)' # 'MyClass(object, MyMixin)'
rx_types = '\((?P<types>[\w,\s]*)\)?'
rx_args = '(?P<args>[\w\s\-]*)?'
rx_kwargs = ',?\s?(?P<kwargs>[\w\s\-]*)'

rx_basic = rx_classname + rx_args + rx_kwargs
rx_types = rx_classname + rx_types + rx_args + rx_kwargs


def parse_string(s):
    dct = None
    s = s.strip('"')
    s = s.strip("'")
    match = re.match(rx_types, s)
    if match:
        dct = match.groupdict()
    if not dct:
        match = re.match(rx_basic, s)
        if match:
            dct = match.groupdict()
    if not dct:
        raise exc.NoMatchException('No match found for %s' % s)
    if dct.get('types') is not None:
        dct['types'] = [d.strip() for d in dct.get('types').strip().split(',')]

    dct['args'] = dct.get('args').strip().split() if dct.get('args') else []
    dct['kwargs'] = dct.get('kwargs').strip().split() if dct.get('kwargs') else []
    return dct

