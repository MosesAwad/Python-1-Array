import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
        Calculates the BMI (Body Mass Index) for a list of heights and weights.

        Args:
            height (list[int | float]): A list of heights in meters.
            weight (list[int | float]): A list of weights in kilograms.

        Returns:
            list[int | float]: A list of BMI values corresponding to the input
            heights and weights.

        Raises:
            AssertionError: If the input lists are not of equal length, contain
            invalid types, or have non-positive values.
            Exception: If an error occurs during BMI calculation.
    """
    try:
        assert len(height) == len(weight), \
            "height and weight lists not of equal length"

        assert isinstance(height, list) and isinstance(weight, list), \
            "height and weight must be of type list"

        for h, w in zip(height, weight):
            assert isinstance(h, (int, float)) and \
                isinstance(w, (int, float)), \
                "height and weight must only contain either \
                    float or int values"
            assert h > 0 and w > 0, \
                "height and weight must have only positive values"

        h = np.array(height)
        w = np.array(weight)

        return (w / (h ** 2)).tolist()
    except AssertionError as e:
        print("AssertionError: ", e)
    except Exception as e:
        print("Exception: ", e)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Compares each BMI value in the list to a specified limit and returns a
        list of booleans.

        Args:
            bmi (list[int | float]): A list of BMI values.
            limit (int): The BMI limit to compare against.

        Returns:
            list[bool]: A list of booleans indicating whether each BMI exceeds
            the limit.

        Raises:
            AssertionError: If the input BMI list or limit is invalid, or if
            the BMI list contains non-positive values.
            Exception: If an error occurs during the comparison.
    """
    try:
        assert isinstance(bmi, list), "bmi must be of type list"
        assert isinstance(limit, int), "limit must be an integer value"
        for b in bmi:
            assert isinstance(b, (float, int)), \
                "bmi must only contain either float or int values"
            assert b > 0, "cannot have negative or zero bmi values"
        
        return (np.array(bmi) > limit).tolist()
    except AssertionError as e:
        print("AssertionError: ", e)
    except Exception as e:
        print("Exception: ", e)
        return []


if __name__ == "__main__":
    # height = [189, 178, 163, 190, 172]
    # weight = [92, 81, 72, 98, 93]

    # print(give_bmi(height, weight))
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

"""
    def give_bmi(height: list[int | float], weight: list[int | float])
        -> list[int | float]:
        bmi = []

        for i in range(len(height)):
            bmi.append(weight[i] / (height[i] * height[i]))

        return bmi
"""
