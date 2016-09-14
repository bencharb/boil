from __future__ import absolute_import, unicode_literals 
def indent(lines, exact=None, times=1, delim='    '):
    if exact is None:
        exact = times*delim
    else:
        exact = ' ' * exact
    if isinstance(lines, basestring):
        if '\n' in lines:
            lines = lines.split('\n')
        else:
            lines = [lines]
    return '\n'.join([exact + l for l in lines])


def insert_arg(arg, seq, index=0):
    if not seq:
        seq = [arg]
        return seq
    if arg != seq[index]:
        if not hasattr(seq, 'insert'):
            seq = list(seq)
        seq.insert(index,arg)
    return seq


def insert_indented(src, block, index):
    parts = block.split('\n')
    if len(parts) > 1:
        line1, otherlines = parts[0], parts[1:]
        otherlines = indent(otherlines, index)
        newblock = '\n'.join((line1,otherlines,))
    else:
        newblock = block
    src_left, src_right = src[:index], src[index:]
    return ''.join((src_left, newblock, src_right,))
