from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def convert_to_grey(image: np.array) -> np.array:
    # return image[:, :, 0:1]
    grey_image = 0.2989 * image[:, :, 0:1] + 0.5870 * image[:, :, 1:2] + 0.1140 * image[:, :, 2:]
    return grey_image


def zoom_slicer(image: np.array, x0: int, y0: int, x1: int, y1: int) -> np.array:
    """
        This function doesn't really "zoom", it slices the image into the two 
        extreme corners: top left [x0,y0]) and bot right [x1, y1]
    """
    return image[y0:y1, x0:x1]


def zoom():
    try:
        image = ft_load("../animal.jpeg")
        print(image)

        zoomed_image = zoom_slicer(image, 450, 100, 850, 500)
        grey_zoomed_image = convert_to_grey(zoomed_image)

        print("New shape after slicing: ", grey_zoomed_image.shape)
        print(grey_zoomed_image)

        plt.imshow(grey_zoomed_image, cmap="grey")
        plt.axis("on")
        plt.show()
    except AssertionError as e:
        print("AssertionError: ", e)
    except Exception as e:
        print("Exception: ", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    zoom()

"""
    NOTES

    You can also use PIL functions to achieve the same effect:

        image_array = ft_load("../animal.jpeg")
        image = Image.fromarray(image_array)
        zoomed_image = image.transform((400,400),
            Image.Transform.EXTENT, (450,100,850,500))
        grey_zoomed_image = zoomed_image.convert("L")

"""
