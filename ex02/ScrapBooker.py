import numpy
from PIL import Image


class ImageProcessor:

    def __init__(self):
        pass

    def load(self, path):
        try:
            img = numpy.array(Image.open(path))
            width = numpy.size(img, 1)
            height = numpy.size(img, 0)
            print("Loading image of dimensions {} x {}".format(width, height))
            return(img)
        except AttributeError:
            print("Error in loading file, wrong path")
            return(None)
        except FileNotFoundError:
            print("Error in loading file, wrong path")
            return(None)
        except:
            print("Something Wrong Happened")
            return(None)

    def display(self, array):
        try:
            to_disp = Image.fromarray(array, 'RGBA')
            to_disp.show()
        except:
            print("Can't display this")


class ScrapBooker:

    def __init__(self):
        pass

    def crop(self, array, dim, pos):
        if dim[0] > numpy.size(array, 0):
            print("Dim on axis[0] is too big")
            return(None)
        if dim[1] > numpy.size(array, 1):
            print("Dim on axis[1] is too big")
            return(None)
        return(array[pos[0]:pos[0] + dim[0], pos[1]:pos[1] + dim[1]])

    def thin(self, array, n, axis):
        return(numpy.delete(array, n, not axis))

    def juxtapose(self, array, n, axis):
        if axis == 0:
            return(numpy.tile(array, (n, 1)))
        elif axis == 1:
            return(numpy.tile(array, (1, n)))

    def mosaic(self, array, dim):
        return(numpy.tile(array, (dim[0], dim[1])))


imp = ImageProcessor()
arr = imp.load("rick.png")
scrap = ScrapBooker()

print("test for mosaic")
test = numpy.tile(numpy.array([0, 1, 2, 3, 4, 5, 6]), (2, 1))
print(test)
print("\nMosaic 3,3\n", scrap.mosaic(test, (3, 3)))


print("test for juxtapose")
test = numpy.tile(numpy.array([0, 1, 2, 3, 4, 5, 6]), (2, 1))
print(test)
print("\nAxis 0:\n", scrap.juxtapose(test, 2, 0))
print("\nAxis 1:\n", scrap.juxtapose(test, 2, 1))
i

print("test for thin axe 0")
test = numpy.tile(numpy.array([0, 1, 2, 3, 4, 5, 6]), (5, 1))
print(test)
print(scrap.thin(test, 2, 0))


print("Test fop crop method")
test = numpy.tile(numpy.array([0, 1, 2, 3, 4, 5, 6]), (5, 1))

imp.display(arr)
imp.display(scrap.crop(arr, (150, 100), (75, 0)))
