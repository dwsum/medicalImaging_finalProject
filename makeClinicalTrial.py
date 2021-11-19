import os
import random

import cv2
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

allMRI = os.listdir(Path("./savedImages/"))
removeDS_store = []
for mri in allMRI:
    if "numMRI" in mri:
        removeDS_store.append(mri)
allMRI = removeDS_store
print(allMRI)

for x in range(0, len(allMRI)):
    whichMRI = allMRI[x]#"numMRI_5_1637200322.6270678"
    multiple = "./savedImages/" + whichMRI + "/multiple/"
    noMultiple = "./savedImages/" + whichMRI + "/noMultiple/"
    original = "./savedImages/" + whichMRI + "/original/"
    randomSelection = random.sample(range(0, 10), 10)

    images_multiple = []
    images_multiple_original = []
    for rand in randomSelection:
        images_multiple.append(cv2.imread(multiple + str(rand) + ".png"))
        images_multiple_original.append(cv2.imread(original + str(rand) + ".png"))

    images_noMultiple = []
    images_noMultiple_original = []
    for rand in randomSelection:
        images_noMultiple.append(cv2.imread(noMultiple + str(rand) + ".png"))
        images_noMultiple_original.append(cv2.imread(original + str(rand) + ".png"))


    def saveImages(theImages, savePath):
        # concatanate image Horizontally
        col1 = np.concatenate((theImages[0], theImages[1], theImages[2], theImages[3], theImages[4]), axis=0)
        col2 = np.concatenate((theImages[5], theImages[6], theImages[7], theImages[8], theImages[9]), axis=0)
        combine = np.concatenate((col1, col2), axis=1)

        cv2.imwrite(savePath + "allDisplay.png", combine)

    saveImages(images_multiple, multiple)
    saveImages(images_multiple_original, original + "multiple_")
    saveImages(images_noMultiple, noMultiple)
    saveImages(images_noMultiple_original, original + "noMultiple_")

