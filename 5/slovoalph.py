import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

def has_bay(img):
    b = ~img
    bb = np.zeros((b.shape[0] + 1, b.shape[1])).astype("uint8")
    bb[:-1, :] = b
    return lakes(~bb) -1

def count_bays(img):
    holes = ~img.copy()
    return np.max(label(holes))

def lakes(img):
    B = ~img
    BB = np.ones((B.shape[0] + 2, B.shape[1] + 2))
    BB[1:-1, 1:-1] = B
    return np.max(label(BB)) - 1

def has_hline(img):
    lines = np.sum(img, 1) // img.shape[1]
    return 1 in lines

def has_vline(img):
    lines = np.sum(img, 0) // img.shape[0]
    return 1 in lines

def recognize(reg):
    lc = lakes(reg.image)
    if lc == 0:
        if has_vline(reg.image):
            if count_bays(reg.image) == 5:
                return '*'
            if np.all(reg.image == 1):
                return '-'
            return '1'
        if count_bays(reg.image) == 2:
            return '/'    
        if count_bays(reg.image) == 5:
            if has_hline(reg.image):
                return '*'
            return 'W'
        if count_bays == 4 and (reg.perimeter**2)/reg.area > 40:
            return '*'
        else:
            return 'X'
    if lc == 1:
        if has_vline(reg.image):
            if count_bays(reg.image) > 3:
                return '0'
            else:
                if (reg.perimeter**2)/reg.area < 59:
                    return 'P'
                else:
                    return 'D'
        else:
            if has_bay(region.image) > 0:
                return 'A'
            else:
                return '0'
    if lc == 2:
        if count_bays(reg.image) > 4:
            return '8'
        else:
            return 'B'
    return None


image = plt.imread("symbols.png")
image = np.sum(image,2)
image[image > 0] = 1

lab = label(image)

r = regionprops(lab)

a = {}
for region in r:
    symbol = recognize(region)
    if symbol not in a:
        a[symbol] = 1
    else:
        a[symbol] += 1

sum = 0
for key in a.keys():
    a[key] = a[key]/np.max(lab) * 100
    sum += a[key]
    print(a[key], "%")

print("РџСЂРѕС†РµРЅС‚С‹ : ")
print(a)


plt.figure()
plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(lab)
plt.show()