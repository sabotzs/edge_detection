import numpy as np
from options import EdgeDetectDirection

def prewitt(image: np.ndarray[np.uint8], direction: EdgeDetectDirection) -> np.ndarray:
    rows = image.shape[0]
    cols = image.shape[1]
    res = np.zeros((rows, cols), dtype=np.float32)

    if direction == EdgeDetectDirection.DIRECTION_X:
        mask = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
    else:
        mask = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)
    mask = (1/6) * mask

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            region = image[row-1:row+2, col-1:col+2]
            res[row, col] = (mask * region).sum()

    return res

