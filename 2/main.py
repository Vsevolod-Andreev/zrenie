import numpy as np 
import matplotlib.pyplot as plt 

def negate(Img):
    arr = Img.copy()
    arr[np.where(arr == 1)] = -1
    return arr

def neighbours2(Img, y, x):
    left = y, x-1
    top = y - 1, x
    if not check(Img, *left):
        left = None
    if not check(Img, *top):
        top = None
    return left, top

def check(Img, y, x):
    if not 0 <= y < Img.shape[0]:
        return False
    if not 0 <= x < Img.shape[1]:
        return False
    if Img[y, x] != 0:
        return True
    return False

def exists(neighbours):
    return not all([n is None for n in neighbours])

def find(label, links):
    j = label
    while links[j] != 0:
        j = links[j]
    return j

def union(label1, label2, links):
    r1 = find(label1, links)
    r2 = find(label2, links)
    if r1 != r2:
        links[r2] = r1

def two_pass_labeling(Img):
    links = np.zeros(len(Img)).astype("uint32")
    labels = np.zeros_like(Img).astype("uint32")
    label = 1
    for y in range(Img.shape[0]):
        for x in range(Img.shape[1]):
            if Img[y, x] != 0:
                n = neighbours2(Img, y, x)
                if not exists(n):
                    m = label
                    label += 1
                else:
                    lbs = [labels[i] for i in n if i is not None]
                    m = min(lbs)
                labels[y, x] = m
                for i in n:
                    if i is not None:
                        lb = labels[i]
                        if lb != m:
                            union(m, lb, links)
    for y in range(Img.shape[0]):
        for x in range(Img.shape[1]):
            if labels[y, x] != 0:
                new_label = find(labels[y, x], links)
                if new_label!= labels[y, x]:
                    labels[y, x] = new_label
    quantity = 0
    lb_unique = np.unique(labels)
    for i in lb_unique:
        labels[labels==i] = quantity
        quantity += 1
    return labels

image = np.zeros((20, 20), dtype = 'int32')
#figure 1
image[1 : -1, -2] = 1
#figure 2
image[1, 1 : 5] = 1
image[1, 7 : 12] = 1
image[2, 1 : 3] = 1
image[2, 6 : 8] = 1
image[3 : 4, 1 : 7] = 1
#figure 3
image[7 : 11, 11] = 1
image[7 : 11, 14] = 1
image[10 : 15, 10 : 15] = 1
#figure 4
image[5 : 10, 5] = 1
image[5 : 10, 6] = 1

labeled_image = two_pass_labeling(image)

plt.figure(figsize=(12, 5))
plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(labeled_image)
plt.show()