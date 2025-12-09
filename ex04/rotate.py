from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def convert_to_grey(image: np.array) -> np.array:
    return image[:, :, 0:1]


def zoom_slicer(image: np.array, x0: int, y0: int,
                x1: int, y1: int) -> np.array:
    return image[y0:y1, x0:x1]


def transpose(image: np.array) -> np.array:
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
