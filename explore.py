import numpy as np

def ft_explore():
    arr = np.array([
            [[5, 3, 2], [8, 2, 9], [12, 12, 21]],
            [[52, 122, 133], [21, 3232, 3123], [323, 32131, 543]],
            [[3213, 8748, 5656], [655, 6453, 987], [432, 75474, 6554]]
        ])
    
    print(arr[:2, 2:, 0:1]) # shape is now (2, 1, 1) -> 2 blocks extracted, 1 row selected, 1 column selected

if __name__ == "__main__":
    ft_explore()

"""
    Output is:

        [[[12]]
        
        [[323]]]

    What this actually is:
    [
        [[12]]
        [[323]]
    ]

    This is still a 3D array but with shape (2,1,1)
"""
