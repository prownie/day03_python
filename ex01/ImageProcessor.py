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


imp = ImageProcessor()
arr = imp.load("rickd.png")
imp.display(arr)
