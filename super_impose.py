# To overlay two images in python

from PIL import Image
import numpy as np

background_img_path = ("background.jpeg")
logo_path = ("logo.png")
background_size = 244  # px
logo_size = 50  # px


def superimpose_two_images(background_img_path, logo_path, background_size, logo_size):
    above_img = Image.open(logo_path)
    background = Image.open(background_img_path)

    print(above_img.size)
    print(background.size)

    # resize the background image
    size = (background_size, background_size)
    background = background.resize(size, Image.ANTIALIAS)

    # resize the logo image
    size = (logo_size, logo_size)
    above_img = above_img.resize(size, Image.ANTIALIAS)

    # paste to overlay two images
    background.paste(above_img, (160, 160), above_img)
    background.save('superimpose_two_images.png', "PNG")


superimpose_two_images(background_img_path, logo_path,
                       background_size, logo_size)
