# Meera's task: Print a valid binary text file and convert it
# into IMAGE1.PNG, preserving the order of rows and columns.
#
# IDE: PyCharm
# Development date: 10/9/26, 10/13/26, 10/14/26, 10/15/26, 10/16/26
#
# Data structures:
# rows is a list of strings containing the binary text lines.
# pixel_values is a list containing brightness values:
# 0 for black and 255 for white.
# image1 holds the resulting Pillow image.
#
# External files:
# Input: A previously validated binary text file.
# Output: IMAGE1.PNG in the current working directory.
# An existing IMAGE1.PNG is overwritten.


from PIL import Image


class Image1Converter:
    # Stores the name of the validated input file.
    # Parameters: filename is the binary text file's name.
    # Global variables used: None.
    # Returns: None.
    def __init__(self, filename):
        self.filename = filename
        self.image1 = None

    # Prints the text, converts it to pixels, saves and displays IMAGE1.
    # Parameters: None other than self, the current object.
    # Global variables used: None.
    # Returns: The Pillow image stored in self.image1.
    # The input file must already have passed binary file validation.
    # File errors are passed to the calling program.
    def ConvertImage1(self):
        # Reopen the file so reading begins at the first line.
        # Remove only newline characters, preserving the binary data.
        with open(self.filename, "r") as file:
            rows = [line.rstrip("\r\n") for line in file]

        # Print each text row in its original order.
        for row in rows:
            print(row)

        width = len(rows[0])
        height = len(rows)

        # Build the pixel list from left to right, then top to bottom.
        pixel_values = []
        for row in rows:
            for character in row:
                if character == "0":
                    pixel_values.append(0)
                else:
                    pixel_values.append(255)

        # L mode stores one grayscale brightness value per pixel.
        # Only 0 and 255 are used, making the image black and white.
        self.image1 = Image.new("L", (width, height))
        self.image1.putdata(pixel_values)

        # Saving with the same filename overwrites an existing image.
        self.image1.save("IMAGE1.PNG")
        self.image1.show()

        return self.image1