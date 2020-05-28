import numpy
from PIL import Image


class ImageProcessor:

    def load(self, path):
        try:
            img = numpy.array(Image.open(path))
            width = numpy.size(img, 1)
            height = numpy.size(img, 0)
            print("Loading image of dimensions {} x {}".format(width, height))
            img = img[:,:,:3]
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
        blue = array
        blue[:,:,0] = numpy.zeros([array.shape[0],array.shape[1]])
        blue[:,:,1] = numpy.zeros([array.shape[0],array.shape[1]])
        ImageProcessor().display(blue)
        return(blue)
    
    def to_green(self, array):
        green = array
        green[:,:,0] * 0
        green[:,:,2] * 0
        ImageProcessor().display(green[:,:,0] + green[:,:,1] + green[:,:,2])
        return(green)

    def to_red(self, array):
        print("shape de red = ",numpy.shape(red))
        #red[:,:,1] = numpy.zeros([array.shape[0],array.shape[1]])
        #red[:,:,2] = numpy.zeros([array.shape[0],array.shape[1]])
        #ImageProcessor().display(red)
        return(red)


imp = ImageProcessor()
arr = imp.load("rick.png")
cf = ColorFilter()


#imp.display(arr)

#inverted = cf.invert(arr)
#imp.display(inverted)

#to_green = cf.to_green(arr)
#imp.display(to_red)

to_blue = cf.to_blue(arr)
#imp.display(to_blue)


#to_green = cf.to_green(arr)
#imp.display(to_green)

