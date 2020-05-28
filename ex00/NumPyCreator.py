import numpy
import random


class NumPyCreator:

    def __init__(self, *args):
        pass

    def from_list(self, lst, dtype=""):
        if not dtype:
            return(numpy.array(lst))
        else:
            return(numpy.array(lst, dtype="{}".format(dtype)))

    def from_tuple(self, tpl, dtype=""):
        if not dtype:
            return(numpy.array(tpl))
        else:
            return(numpy.array(tpl, dtype="{}".format(dtype)))

    def from_iterable(self, itr, dtype=""):
        if not dtype:
            return(numpy.array(itr))
        else:
            return(numpy.array(itr, dtype="{}".format(dtype)))

    def from_shape(self, shape, value=0, dtype=""):
        if value == 0:
            if dtype:
                return(numpy.zeros(shape, dtype="{}".format(dtype)))
            else:
                return(numpy.zeros(shape))
        else:
            if dtype:
                return(numpy.full(shape, value, dtype="{}".format(dtype)))
            else:
                return(numpy.full(shape, value))

    def random(self, shape):
        return(numpy.random.random_sample(shape))

    def identity(self, n, dtype=""):
        if dtype:
            return(numpy.eye(n, dtype="{}".format(dtype)))
        else:
            return(numpy.eye(n))


npc = NumPyCreator()
print("1")
print(npc.from_list([[1, 2, 3], [6, 3, 4]], "float"))
print("2")
print(npc.from_tuple(("a", "b", "c")))
print("3")
print(npc.from_iterable(range(5), "float"))
shape = (3, 5)
print("4")
print(npc.from_shape(shape, 0, 'str'))

print("5")
print(npc.random(shape))

print("6")
print(npc.identity(4, "str"))
