# Meera's task: Load and display IMAGE2.png and convert its
# pixels into an array containing 0 for black and 1 for nonzero.
#
# IDE: PyCharm
# Dates: 10/9/26, 10/13/26, 10/14/26, 10/15/26, 10/16/26
#
# Data structures:
# image2 holds the grayscale image.
# ZerosAndOnes is a two dimensional NumPy array of integers.
# Each entry corresponds to one image pixel at [row, column].
#
# External file: IMAGE2.png in the current working directory.

from PIL import Image
import numpy as np


class Image2Converter:
    # Sets the filename and prepares the image and array attributes.
    # Parameters: filename is the input image filename.
    # Global variables used: None.
    # Returns: None.
    def __init__(self, filename="IMAGE2.png"):
        self.filename = filename
        self.image2 = None
        self.ZerosAndOnes = None

    # Loads and displays IMAGE2 and converts its pixels to binary values.
    # Parameters: None other than self, the current object.
    # Global variables used: None.
    # Returns: The two dimensional ZerosAndOnes array.
    # File errors are passed to the calling program.
    def ConvertImage2(self):
        # Grayscale uses one brightness value for each pixel.
        with Image.open(self.filename) as image:
            self.image2 = image.convert("L")

        self.image2.show()

        # Preserves the original order of the rows and columns.
        pixels = np.array(self.image2)

        # Zero becomes 0. Every nonzero brightness becomes 1.
        self.ZerosAndOnes = (pixels != 0).astype(int)

        return self.ZerosAndOnes


if __name__ == "__main__":
    try:
        converter = Image2Converter()
        ZerosAndOnes = converter.ConvertImage2()

        print("IMAGE2 has been displayed and converted.")
        print("Rows:", ZerosAndOnes.shape[0])
        print("Columns:", ZerosAndOnes.shape[1])

    except FileNotFoundError:
        print("Error: IMAGE2.png was not found in the current directory.")

    except PermissionError:
        print("Error: Permission denied when opening IMAGE2.png.")

    except OSError as error:
        print("Error: Could not read IMAGE2.png:", error)

    input("Press ENTER to end the program.")