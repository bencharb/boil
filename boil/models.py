from __future__ import absolute_import, unicode_literals 
from boil import util

class Function(object):

    def __init__(self, name=None, args=None, kwargs=None, code_block=None):
        super(Function, self).__init__()
        self.name = name
        self.args = args
        self.kwargs = kwargs
        self.code_block = code_block
    
    def iter_render_arguments(self):
        if self.args:
            for a in self.args:
                yield a
        if self.kwargs:
            for k,v in self.kwargs.iteritems():
                yield '%s=%s' % (k,v,)
    
    @property
    def argskwargs_block(self):
        result = [r.strip() for r in self.iter_render_arguments()]
        if result:
            result = ',\n'.join(result)
        else:
            result = ''
        return result
    
    @property
    def def_string(self):
        argskwargs = self.argskwargs_block
        def_text = 'def %s():' % (self.name,)
        result = util.insert_indented(def_text,argskwargs,def_text.index('(')+1)
        return result
    
    def render(self):
        parts = self.def_string, util.indent(self.code_block)
        txt = '\n'.join(parts)
        return txt


class Class(object):
    def __init__(self, name=None, types=('object',), methods=None):
        super(Class, self).__init__()
        self.name = name
        self.types = types
        self.methods = methods

    @staticmethod
    def render_init_block(classname, args=None, kwargs=None):
        lines = ['super(%s, self).__init__()' % classname]
        if not args:
            args = ['self']
        if args[0] == 'self':
            args = args[1:]
        lines.extend(['self.%s = %s' % (a,a,) for a in args])
        if kwargs:
            lines.extend(['self.%s = %s' % (k,k,) for k in kwargs])
        return '\n'.join(lines)
    
    @property
    def code_block(self):
        if not self.methods:
            return 'pass'
        return '\n\n\n'.join([m.render() for m in self.methods])
        
    def render(self):
        types_string = ', '.join(self.types) if self.types else ''
        defstring = 'class %s(%s):' % (self.name, types_string,)
        return '\n'.join((defstring, util.indent(self.code_block),))

    def __unicode__(self):
        return unicode(self.render())
    
    def __str__(self):
        return str(self.render())
