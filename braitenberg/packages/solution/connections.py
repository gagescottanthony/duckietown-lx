from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    segwidth = shape[1] // 6
    # these are random values
    # ---
    res[:,0:segwidth*1] = 0.1
    res[:,segwidth*1:segwidth*2] = 0.4
    res[:,segwidth*2:segwidth*3] = 0.9
    res[:,segwidth*3:segwidth*4] = -0.6
    res[:,segwidth*4:segwidth*5] = -0.3
    res[:,segwidth*5:shape[1]] = -0.1
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    segwidth = shape[1] // 6
    # these are random values
    res[:,0:segwidth*1] = -0.1
    res[:,segwidth*1:segwidth*2] = -0.3
    res[:,segwidth*2:segwidth*3] = -0.6
    res[:,segwidth*3:segwidth*4] = 0.9
    res[:,segwidth*4:segwidth*5] = 0.4
    res[:,segwidth*5:shape[1]] = 0.1
    return res
