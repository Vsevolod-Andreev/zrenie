import numpy
import matplotlib.pyplot as plt
from typing import Dict


FIGURE =['C:/Users/User/Downloads/figure1.txt',
        'C:/Users/User/Downloads/figure2.txt',
        'C:/Users/User/Downloads/figure3.txt',
        'C:/Users/User/Downloads/figure4.txt',
        'C:/Users/User/Downloads/figure5.txt',
        'C:/Users/User/Downloads/figure6.txt',]


def read_data(file_name: str) -> Dict:
    array = []
    with open(file_name, 'r') as f:
        data = f.read()
    data = data.split('\n')
    resolution = float(data[0])
    for row in data[2:-1]:

        row = row.split(' ')
        array.append(list(map(int, row[:-1])))
    return {"resolution": resolution, "array": array}


def get_resolution(data: numpy.array):
    max_size = 0
    for row in data:
        if sum(row) > max_size:
            max_size = sum(row)
    return max_size


if __name__ == '__main__':
    for file_path in FIGURE:
        info = read_data(file_path)
        try:
            print(info['resolution'] / get_resolution(info['array']))
        except ZeroDivisionError:
            print('resolution 0')

