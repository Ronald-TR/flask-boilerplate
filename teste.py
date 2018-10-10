class Teste:
    def bla(self):
        return 'bla bla'

# def pai(f):
#     def funcaoDoFilho(*a, **k):
#         print(a, k)
#         setattr(f, 'bla', bla)
#         return f(*a, **k)
#     return funcaoDoFilho    
    
def herde(f):
    def argfun(*args, **kwargs):
        result = type(f.__class__.__name__, (Teste, ), {})
        return result(*args, **kwargs)
    return argfun 

@herde
class Filho:
    def own_hello(self):
        return 'hello from Filho'

# print(Filho().own_hello())
# print(Filho().bla())

print(Filho().bla())