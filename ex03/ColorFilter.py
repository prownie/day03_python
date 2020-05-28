import numpy
from PIL import Image


class ImageProcessor:

    def load(self, path):
        try:
            img = numpy.array(Image.open(path))
            width = numpy.size(img, 1)
            height = numpy.size(img, 0)
            print("Loading image of dimensions {} x {}".format(width, height))
            img = img[:, :, :3]
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
            to_disp = Image.fromarray(array, 'RGB')
            to_disp.show()
        except:
            print("Can't display this")


class ColorFilter:

    def invert(self, array):
        return(255 - array)

    def to_blue(self, array):
        blue = numpy.zeros(array.shape, dtype=numpy.uint8)
        blue[:, :, 2] = array[:, :, 2]
        return(blue)

    def to_green(self, array):
        return(array * numpy.uint8([0, 1, 0]))

    def to_red(self, array):
        return(array - self.to_green(array) - self.to_blue(array))

    def celluloid(self, array, num=5):
        if num < 2:
            num = 2
        linspace = (numpy.linspace(0, 255, num))
        return array - array % int(linspace[1])

    def to_grayscale(array, filter):
        pass


imp = ImageProcessor()
arr = imp.load("elonmusk.jpg")
cf = ColorFilter()


imp.display(arr)

inverted = cf.invert(arr)
imp.display(inverted)

to_green = cf.to_green(arr)
imp.display(to_green)

to_blue = cf.to_blue(arr)
imp.display(to_blue)


to_red = cf.to_red(arr)
imp.display(to_red)

celluloid = cf.celluloid(arr, 3)
imp.display(celluloid)
