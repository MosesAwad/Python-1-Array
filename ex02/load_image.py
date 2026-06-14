from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
        Loads an image from the specified path and converts it into a NumPy
        array.

        Args:
            path (str): The file path to the image.

        Returns:
            np.array: The image as a NumPy array.

        Raises:
            AssertionError: If the path is not a valid string or the image
            format is not supported.

            Exception: If an error occurs during image loading.
    """
    try:
        assert isinstance(path, str) and len(path) > 0, \
            "The path must be a string."

        im = Image.open(path)
        assert im.format in ["JPG", "JPEG"], \
            "Only .jpg or .jpeg file extensions are allowed"
        assert im is not None, \
            "Unable to load image."

        data_array = np.array(im)
        print("The shape of the image is: ", data_array.shape)

        return data_array
    except AssertionError as e:
        print("Assertion error: ", e)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    print(ft_load("../landscape.jpg"))

"""

def ft_load(path: str):
    try:
        im = Image.open(path)

        data_list = list(im.getdata())
        data_array = np.array(data_list)
        data_array = data_array.reshape(
            (im.size[1], im.size[0], 3)
        ) # num of cols = 3 for (h,w,channels)

        print("The shape of the image is: ", data_array.shape)

        row = data_array[0].copy()          # first row
        row[-3:] = data_array[-1, -3:]      # last 3 pixels from last row
        print(row[None, :, :])

    except Exception as e:
        print("Error: ", e)

"""
