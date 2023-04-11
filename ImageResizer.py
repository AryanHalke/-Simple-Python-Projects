# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB modeg
im = Image.open("photo.png")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size


# Cropped image of above dimension
# (It will not change original image)

newsize = (250, 200)
im1 = im.resize(newsize)
# Shows the image in image viewer
im1.show()
im1.save("Resized.png")
