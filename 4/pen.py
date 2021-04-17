import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import morphology
from skimage.filters import threshold_triangle
from skimage.measure import label, regionprops

def binarisation(image, limit_min, limit_max):
    B = image.copy()
    B[B <= limit_min] = 0
    B[B >= limit_max] = 0
    B[B > 0] = 1
    return B

def circularity(region, label = 1):
    return (region.perimeter ** 2) / region.area

def toGray(image):
    return (0.2989 * image[:,:,0] + 0.587 * image[:,:,1] + 0.114 * image[:,:,2]).astype("uint8")

sc = 0
pencils = 0

for sc in range(1, 13):
    image = plt.imread("images/img ("+str(sc)+").jpg")
    gr = toGray(image)
    thr = threshold_triangle(gr)
    br = binarisation(gr, 0, thr)
    br = morphology.binary_dilation(br, iterations = 1)
    lab = label(br)
    areas = []
   
    for r in regionprops(lab):
        areas.append(r.area)
    
    for r in regionprops(lab):
        if r.area < np.mean(areas):
            lab[lab == r.label] = 0
        bbox = r.bbox
        if bbox[0] == 0 or bbox[1] == 0:
            lab[lab == r.label] = 0
        
    lab[lab > 0] = 1
    lab = label(lab)
  
    c = 0 
    ov = 0 

    for reg in regionprops(lab):
        c = c + 1
        if (((circularity(reg, c) > 100) and (300000 < reg.area < 450000))):
            ov = ov + 1

    pencils = pencils + ov

print("РљР°СЂР°РЅРґР°С€РµР№ = ", pencils)
plt.show()