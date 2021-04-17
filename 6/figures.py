import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage.measure import label, regionprops

img = plt.imread("balls_and_rects.png")
img = color.rgb2hsv(img)[:, :, 0]
uq = np.unique(img) * 10
img = np.ceil(img * 10)
o = np.ceil(uq) 
color = np.unique(o)
circle = {}
rectangle = {}
i = 0

for c in color:
    circle["c" + str(i)] = 0
    rectangle["c" + str(i)] = 0
    image = img.copy()
    image[image != c] = 0
    lab = label(image)
    reg = regionprops(lab)
    for s in reg:
        if np.all(s.image):
            circle["c" + str(i)] += 1
        else:
            rectangle["c" + str(i)] += 1
    i += 1

print("РљСЂСѓРіРё = ", circle)
print("РџСЂСЏРјРѕСѓРіРѕР»СЊРЅРёРєРё = ", rectangle)
print("Р’СЃРµРіРѕ = ", np.sum(list(rectangle.values())) + np.sum(list(circle.values())))