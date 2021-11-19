import os
import time

import numpy as np
import random
import cv2
from dipy.sims import phantom


saveMode = True
numImages = 10
imageNoiseProbability = 0.25
theSNR = 3.54

numMRI_list = [5, 15, 25, 35]
resolution = 0.0294 #cm

buffer = 15
fatThickness = int(0.5/resolution)
fatCenter = int(8/resolution)
imageWidth = fatCenter + 2 * buffer +int(fatThickness *2)
print("fatCenter", fatCenter)

#nerve info
nerveLocation = (int(imageWidth/3), int(imageWidth/2))
nerveRadius = int(0.5/resolution)

#tumor info
tumorRadius = int(1/resolution)

#white color
# The value of Fat: 0.7747169032417183  Muscle:  0.46249658372820346  Tumor  0.5652088003382723  and Nerve  0.6783725593150846
fat_color = 0.7747169032417183
muscle_color = 0.46249658372820346
nerve_color = 0.6783725593150846
tumor_color = 0.5652088003382723

fat_color = int(fat_color * 255)
muscle_color = int(muscle_color * 255)
nerve_color = int(nerve_color * 255)
tumor_color = int(tumor_color * 255)


def displayImage(multipleImage, noMultiple, origImage):
    global cntImages

    if not saveMode:
        cv2.imshow('Single Channel Window', multipleImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Done with image " + str(cntImages))
        cv2.imwrite(multipleSavePath + str(cntImages) + ".png", multipleImage)
        cv2.imwrite(originalSavePath + str(cntImages) + ".png", origImage)
        cv2.imwrite(noMultipleSavePath + str(cntImages) + ".png", noMultiple)
        cntImages += 1

def createImage(img =None):
    width = imageWidth
    height = width
    if img is None:
        img = np.zeros((width, height, 1), dtype = "uint8")

    #draw the fat
    fatRadius = int(fatCenter/2) + int(fatThickness/2)
    img = cv2.circle(img, center = (int(width/2), int(height/2)), radius=fatRadius, color=fat_color, thickness=fatThickness)

    #draw the muscle
    img = cv2.circle(img, center=(int(width / 2), int(height / 2)),
                     radius=fatRadius, color=muscle_color,
                     thickness=-1)

    #draw the nerve
    img = cv2.circle(img, center = nerveLocation, radius=nerveRadius, color=nerve_color, thickness=-1)

    return img

lastTumor1 = None
lastTumor2 = None
def drawTumor(img, numberIter):
    global lastTumor1, lastTumor2
    #need to be between 1.33 and 5

    if numberIter == 0:
        firstNumber = 0.0
        secondNumber = 0.0
        while firstNumber < 1.33 or firstNumber > 4.5:
            firstNumber = random.random() * 5
        while secondNumber < 1.33 or secondNumber > 4.5:
            secondNumber = random.random() * 5
        lastTumor1 = firstNumber
        lastTumor2 = secondNumber

    tumorLocation = (int(imageWidth/lastTumor1), int(imageWidth/lastTumor2)) #TODO randomize location of tumor
    #draw the nerve
    img = cv2.circle(img, center = tumorLocation, radius=tumorRadius, color=tumor_color, thickness=-1)
    return img

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def drawSpeckle(img):
    print("before draw")
    img = phantom.add_noise(img, snr=theSNR, S0=None, noise_type='gaussian')
    print("after draw")
    # img = sp_noise(img, imageNoiseProbability)

    #draw mask
    # fatRadius = int(fatCenter / 2) + int(fatThickness / 2)
    # mask = np.zeros((imageWidth, imageWidth, 1), dtype="uint8")
    # mask = cv2.circle(mask, center=(int(imageWidth / 2), int(imageWidth / 2)), radius=fatRadius + int(fatThickness/2), color=1,
    #                  thickness=-1)
    # img = cv2.bitwise_and(img, img, mask= mask)

    return img

if __name__ == "__main__":

    for numMRI in numMRI_list:
        cntImages = 0
        if not saveMode:
            numImages = 1

        if saveMode:
            thisTime = time.time()
            savePath = "./savedImages/numMRI_" + str(numMRI) + "_snr_" + str(theSNR) + "_" + str(thisTime) + "/"
            os.mkdir(savePath)
            originalSavePath = savePath + "original" + "/"
            noMultipleSavePath = savePath + "noMultiple" + "/"
            multipleSavePath = savePath + "multiple" + "/"
            os.mkdir(originalSavePath)
            os.mkdir(multipleSavePath)
            os.mkdir(noMultipleSavePath)

        for y in range(0, numImages):
            image = None
            avg_image = None
            for x in range(0, numMRI):
                image = createImage(image)
                image = drawTumor(image, x)
                speckle = drawSpeckle(image)

                if avg_image is None:
                    avg_image = image
                else:
                    alpha = 1.0 / (x)
                    beta = 1.0 - alpha
                    avg_image = cv2.addWeighted(speckle, alpha, avg_image, beta, 0.0)

            displayImage(avg_image, speckle, image)
            #NOTE::I AM ASSUMING THE 3CM THICKNESS OF THE MUCLE IS ACTUALLY THE RADIUS