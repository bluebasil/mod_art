import math

def ibase(n, radix=2, maxlen=None):
    r = []
    while n:
        n,p = divmod(n, radix)
        r.append('%d' % p)
        if maxlen and len(r) > maxlen:
            break
    r.reverse()
    return ''.join(r)

def fbase(n, radix=2, maxlen=8):
    r = []
    f = math.modf(n)[0]
    while f:
        f, p = math.modf(f*radix)
        r.append('%.0f' % p)
        if maxlen and len(r) > maxlen:
            break
    return ''.join(r)

def base(n, radix, maxfloat=8):
    if isinstance(n, float):
        return ibase(n, radix)+'.'+fbase(n, radix, maxfloat)
    elif isinstance(n, str):
        n,f = n.split('.')
        n = int(n, radix)
        f = int(f, radix)/float(radix**len(f))
        return n + f
    else:
        return ibase(n, radix)