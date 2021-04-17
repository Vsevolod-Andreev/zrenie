from task1 import read_data
from typing import List

IMG_1 = 'C:/Users/User/Downloads/img1.txt'
IMG_2 = 'C:/Users/User/Downloads/img2.txt'


def calculate(result1: List[List[int]], result2: List[List[int]]) -> List[int]:
    x1, y1 = -1, -1
    x2, y2 = -1, -1
    for i in range(len(result1)):
        if x1 != -1 and y1 != -1:
            break
        for j in range(len(result1[i])):
            if result1[i][j]:
                x1, y1 = i, j

    for i in range(len(result2)):
        if x2 != -1 and y2 != -1:
            break
        for j in range(len(result2[i])):
            if result2[i][j]:
                x2, y2 = i, j
    return [abs(x1 - x2), abs(y1 - y2)]


if __name__ == '__main__':
    figure1 = read_data(IMG_1)
    figure2 = read_data(IMG_2)
    result = calculate(figure1['array'], figure2['array'])
    print(f"x: {result[0]} y: {result[1]}")
