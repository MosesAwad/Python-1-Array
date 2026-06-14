from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def convert_to_grey(image: np.array) -> np.array:
    """
        Converts a color image to grayscale using the standard luminosity
        formula.

        Args:
            image (np.array): A color image array with shape
            (height, width, 3).

        Returns:
            np.array: A grayscale image array with shape (height, width, 1).

        Raises:
            AssertionError: If the input image is invalid or has incorrect
            dimensions.
            Exception: If an error occurs during conversion.
    """
    # return image[:, :, 0:1]
    grey_image = 0.2989 * image[:, :, 0:1] + 0.5870 * image[:, :, 1:2] \
        + 0.1140 * image[:, :, 2:]
    return grey_image


def zoom_slicer(image: np.array, x0: int, y0: int,
                x1: int, y1: int) -> np.array:
    """
        Extracts a rectangular region (zoom) from an image using coordinates.

        Args:
            image (np.array): The input image array.
            x0 (int): The starting x-coordinate (column).
            y0 (int): The starting y-coordinate (row).
            x1 (int): The ending x-coordinate (column).
            y1 (int): The ending y-coordinate (row).

        Returns:
            np.array: The sliced image region from (y0:y1, x0:x1).

        Raises:
            AssertionError: If the input image is invalid or coordinates are
            out of bounds.
            Exception: If an error occurs during slicing.
    """
    return image[y0:y1, x0:x1]


def transpose(image: np.array) -> np.array:
    """
        Transposes a 3D image array to a 2D array by extracting the first
        channel.

        Args:
            image (np.array): A 3D image array with shape
            (height, width, channels).

        Returns:
            np.array: A transposed 2D array with shape (width, height).

        Raises:
            AssertionError: If the input image has invalid dimensions.
            Exception: If an error occurs during transposition.
    """
    # num of channels in array = image height
    h = image.shape[0]
    # num of rows in array = image width
    w = image.shape[1]
    # 2D array to match subject PDF output
    transpose = np.zeros((w, h), dtype=image.dtype)

    for i in range(h):
        for j in range(w):
            transpose[j][i] = image[i][j][0]

    return transpose


def rotate():
    """
        Loads an image, extracts a region, converts to grayscale, transposes,
        and displays the result.

        This function performs the following steps:
        1. Loads an image from "../animal.jpeg"
        2. Zooms into a specified rectangular region
        3. Converts the zoomed region to grayscale
        4. Transposes the grayscale image
        5. Displays the transposed image using matplotlib

        Raises:
            AssertionError: If the image cannot be loaded or has invalid
            dimensions.
            Exception: If an error occurs during image processing.
    """
    try:
        image = ft_load("../animal.jpeg")

        zoomed_image = zoom_slicer(image, 450, 100, 850, 500)
        grey_zoomed_image = convert_to_grey(zoomed_image)
        print(grey_zoomed_image.shape)
        print(grey_zoomed_image)

        transpose_image = transpose(grey_zoomed_image)
        print("New shape after Transpose: ", transpose_image.shape)
        print(transpose_image)

        plt.imshow(transpose_image, cmap="grey")
        plt.axis("on")
        plt.show()
    except AssertionError as e:
        print("AssertionError: ", e)
    except Exception as e:
        print("Exception: ", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    rotate()
