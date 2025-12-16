from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(image: np.array) -> np.array:
    """
        Inverts the colors of the input image.
    """
    try:
        inverted_img = 255 - image

        plt.imshow(inverted_img)
        plt.title('Inverted Image')
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')
    except KeyboardInterrupt:
        pass

    return inverted_img


def ft_grey(image: np.array) -> np.array:
    """
        Converts the input image to grayscale.
    """
    try:
        grey_img = image.copy()
        grey_img = (
            image[:, :, 0:1] / (1 / 0.2989) +
            image[:, :, 1:2] / (1 / 0.5870) +
            image[:, :, 2:] / (1 / 0.1140)
        )

        plt.imshow(grey_img, cmap="grey")
        plt.title('Grey Image')
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')
    except KeyboardInterrupt:
        pass

    return grey_img


def ft_green(image: np.array) -> np.array:
    """
        Extracts the green channel of the input image.
    """
    try:
        green_img = image.copy()
        green_img[:, :, 0] = 0
        green_img[:, :, 2] = 0

        plt.imshow(green_img)
        plt.title('Green Image')
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')
    except KeyboardInterrupt:
        pass

    return green_img


def ft_red(image: np.array) -> np.array:
    """
        Extracts the red channel of the input image.
    """
    try:
        red_img = image.copy()
        red_img[:, :, 1] = 0
        red_img[:, :, 2] = 0

        plt.imshow(red_img)
        plt.title('Red Image')
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')
    except KeyboardInterrupt:
        pass

    return red_img


def ft_blue(image: np.array) -> np.array:
    """
        Extracts the blue channel of the input image.
    """
    try:
        blue_img = image.copy()
        blue_img[:, :, 0] = 0
        blue_img[:, :, 1] = 0

        plt.imshow(blue_img)
        plt.title('Blue Image')
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')
    except KeyboardInterrupt:
        pass

    return blue_img


if __name__ == "__main__":
    try:
        image = ft_load("../landscape.jpg")
        ft_blue(image)
    except AssertionError as e:
        print("AssertionError: ", e)
    except Exception as e:
        print("Exception: ", e)
    except KeyboardInterrupt:
        pass
