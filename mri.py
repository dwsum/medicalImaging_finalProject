import math
import matplotlib.pyplot as plt
import numpy as np

initial = 1
#equation is: Mxy = k* M0 * e ^ (-TE/T2) * (1 - e ^ (-TR/T1))

fat_t1 = 337
fat_t2 = 98
muscle_t1 = 1233
muscle_t2 = 37
tumor_t1 = 1100
tumor_t2 = 50
nerve_t1 = 1083
nerve_t2 = 78
t1 = [fat_t1, muscle_t1, tumor_t1, nerve_t1]
t2 = [fat_t2, muscle_t2, tumor_t2, nerve_t2]
names = ["Fat", "Muscle", "Tumor", "Nerve"]

def findMax(item1, item2, scale):
    maxDiff = 0
    maxLocation = None
    maxX = None
    for x in range(0, len(item1)):
        thisDiff = abs(item1[x] - item2[x])
        if thisDiff > maxDiff:
            maxDiff = thisDiff
            maxLocation = scale[x]
            maxX = x

    return maxLocation, maxDiff, maxX

def together(TR_max, TE_max, titles, firstItem = "Muscle", secondItem = "Tumor"):
    # for y in range(0, len())
    # TE = short_TE
    # normal TR value: between 500ms and 1500ms....1000ms.
    TR_list = list(range(0, TR_max, 1))
    TE_list = list(range(0, TE_max, int(TE_max / 25)))
    # print(TE_list)

    firstItem_TR = None
    firstItem_TE = None
    secondItem_TR = None
    secondItem_TE = None
    fat_TR = []
    muscle_TR = []
    tumor_TR = []
    nerve_TR = []

    location1 = None
    location2 = None
    for x in range(0, len(t1)):
        xAxis = []
        theResult = []
        for TR in TR_list:
            # TR = TR * (10 ** -3)
            shortTE_shortTR_tmp = initial * math.exp(-TE_max / t2[x]) * (1 - math.exp(-TR / t1[x]))
            theResult.append(shortTE_shortTR_tmp)
            xAxis.append(TR)
            if names[x] == "Fat":
                fat_TR.append(shortTE_shortTR_tmp)
            elif names[x] == "Muscle":
                muscle_TR.append(shortTE_shortTR_tmp)
            elif names[x] == "Tumor":
                tumor_TR.append(shortTE_shortTR_tmp)
            elif names[x] == "Nerve":
                nerve_TR.append(shortTE_shortTR_tmp)
        finalIndex = len(theResult) - 1
        TR_final = theResult[finalIndex]

        # print(TR_final)
        for TE in TE_list:
            shortTE_shortTR_tmp = TR_final * math.exp(-TE / t2[x]) * (1 - math.exp(-TR_max / t1[x]))
            theResult.append(shortTE_shortTR_tmp)
            xAxis.append(TE + TR_max)
        # print(theResult[finalIndex + 1])


        # save the items to compare against.
        if firstItem == names[x]:
            firstItem_TR = theResult[0:finalIndex]
            firstItem_TE = theResult[finalIndex + 1:len(theResult)-1]
        elif secondItem == names[x]:
            secondItem_TR = theResult[0:finalIndex]
            secondItem_TE = theResult[finalIndex + 1:len(theResult)-1]

        # names = ["Fat", "Muscle", "Tumor", "Nerve"]


        # if firstItem_TR is not None and firstItem_TE is not None and secondItem_TR is not None and secondItem_TE is not None:
        if len(fat_TR) != 0 and len(muscle_TR) == len(tumor_TR) == len(nerve_TR) == len(fat_TR):
            location1, diff1, index1 = findMax(firstItem_TR, secondItem_TR, xAxis[0:finalIndex])
            location2 , diff2, index2 = findMax(firstItem_TE, secondItem_TE, xAxis[finalIndex + 1:len(theResult)-1])
            print(titles[0], "on", firstItem, "and", secondItem, "TR's max location and diff:", location1, diff1, "TE's max location and diff:", location2, diff2)
            print(len(muscle_TR), len(tumor_TR), len(nerve_TR), len(fat_TR))
            print("The value of Fat:",fat_TR[index1]," Muscle: ",muscle_TR[index1]," Tumor ", tumor_TR[index1]," and Nerve ",   nerve_TR[index1])
            firstItem_TR = None
            firstItem_TE = None
            secondItem_TR = None
            secondItem_TE = None

        plt.plot(np.array(xAxis), np.array(theResult))

    plt.axvline(location1)
    # plt.axvline(location2)
    plt.legend(names)
    plt.title(titles[0])
    plt.xlabel("TR (ms)")
    plt.ylabel("Magnitude (*Mo)")
    plt.show()


together_titles = ["test"]
together(TR_max=10000, TE_max=25, titles=["Infinitely Long TR and Instantaneously Short Echo Time"])
# together(TR_max=450, TE_max=25, titles=["Short TR, Short TE (T1 Weighted)"])
# together(TR_max=450, TE_max=95, titles=["Short TR, Long TE (No Signal)"])
# together(TR_max=1550, TE_max=25, titles=["Long TR, Short TE (Proton Density Weighted)"])
# together(TR_max=1550, TE_max=95, titles=["Long TR, Long TE (T2 Weighted)"])


# In clinical practice:
#
# TE is always shorter than TR
# A short TR = value approximately equal to the average T1 value, usually lower than 500 ms
# A long TR = 3 times the short TR, usually greater than 1500 ms
# A short TE is usually lower than 30 ms
# A long TE = 3 times the short TE, usually greater than 90 ms
# https://www.imaios.com/en/e-Courses/e-MRI/MRI-signal-contrast/Signal-weighting#:~:text=TE%20is%20always%20shorter%20than,usually%20lower%20than%2030%20ms
