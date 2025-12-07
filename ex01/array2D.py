import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert isinstance(family, list), \
            "must pass in a 2D list as an argument"
        assert all(isinstance(row, list) for row in family), \
            "list inner arguments are not of type list"
        assert all(len(row) == len(family[0]) for row in family), \
            "array cannot be jagged"

        array = np.array(family)
        assert len(array.shape) == 2, "list passed in was not 2D"
        print("My shape is :", array.shape)

        assert isinstance(start, int) and isinstance(end, int), \
            "start and end must be integers"
        sliced_array = array[start:end]
        print("My new shape is :", sliced_array.shape)

        return sliced_array
    except AssertionError as e:
        print("AssertionError: ", e)
    except Exception as e:
        print("Exception: ", e)


if __name__ == "__main__":
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    # family = [[],
    #             [],
    #             [],
    #             []]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
