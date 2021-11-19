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
short_TE = 25 #* (10 ** -3)# A short TE is usually lower than 30 ms
long_TE = 90 #* (10 ** -3)# A long TE = 3 times the short TE, usually greater than 90 ms
TE_list = [short_TE, long_TE]
# print(TE_list)
titles_longTR = ["Short TE, Long TR", "Long TE, Long TR"]
titles_shortTR = ["Short TE, Short TR", "Long TE, Short TR"]

# In clinical practice:
#
# TE is always shorter than TR
# A short TR = value approximately equal to the average T1 value, usually lower than 500 ms
# A long TR = 3 times the short TR, usually greater than 1500 ms
# A short TE is usually lower than 30 ms
# A long TE = 3 times the short TE, usually greater than 90 ms
# https://www.imaios.com/en/e-Courses/e-MRI/MRI-signal-contrast/Signal-weighting#:~:text=TE%20is%20always%20shorter%20than,usually%20lower%20than%2030%20ms

#short/long TE, varying TR
def varyTR(TR_max, titles):
    for y in range(0, len(TE_list)):
        TE = TE_list[y]#1 / 10000000
        #normal TR value: between 500ms and 1500ms....1000ms.
        TR_list = list(range(0, TR_max, int(TR_max/100)))
        # TR_list = [x / 10000000 for x in TR_list]
        for x in range(0, len(t1)):
            shortTE_shortTR = []
            for TR in TR_list:
                # TR = TR * (10 ** -3)
                shortTE_shortTR_tmp = initial * math.exp(-TE/t2[x]) * (1 - math.exp(-TR/t1[x]))
                shortTE_shortTR.append(shortTE_shortTR_tmp)
            plt.plot(np.array(TR_list), np.array(shortTE_shortTR))
        plt.legend(names)
        plt.title(titles[y])
        plt.xlabel("TR (ms)")
        plt.ylabel("Magnitude (*Mo)")
        plt.show()

# varyTR(500, titles_shortTR) # A short TR = value approximately equal to the average T1 value, usually lower than 500 ms
# varyTR(2000, titles_longTR) # A long TR = 3 times the short TR, usually greater than 1500 ms

#varying TE, Long/short TR
short_TR = 450 # A short TR = value approximately equal to the average T1 value, usually lower than 500 ms
long_TR = 1550 # A long TR = 3 times the short TR, usually greater than 1500 ms
titles_shortTE = ["Short TR, Short TE", "Long TR, Short TE"]
titles_longTE = ["Long TE, Short TR", "Long TE, Long TR"]
TR_list = [short_TR, long_TR]

def varyTE(TE_max, titles):
    for y in range(0, len(TR_list)):
        TR = TR_list[y]
        TE_list = list(range(0, TE_max, int(TE_max/25)))
        # TR_list = [x / 10000000 for x in TR_list]
        for x in range(0, len(t1)):
            shortTE_shortTR = []
            for TE in TE_list:
                shortTE_shortTR_tmp = initial * math.exp(-TE/t2[x]) * (1 - math.exp(-TR/t1[x]))
                shortTE_shortTR.append(shortTE_shortTR_tmp)
            plt.plot(np.array(TE_list), np.array(shortTE_shortTR))
        plt.legend(names)
        plt.title(titles[y])
        plt.xlabel("TE (ms)")
        plt.ylabel("Magnitude (*Mo)")
        plt.show()

# varyTE(25, titles_shortTE)  #* (10 ** -3)# A short TE is usually lower than 30 ms
# varyTE(120, titles_longTE)  #* (10 ** -3)# A long TE = 3 times the short TE, usually greater than 90 ms


def together(TR_max, TE_max, titles):
    # for y in range(0, len())
    TE = short_TE
    # normal TR value: between 500ms and 1500ms....1000ms.
    TR_list = list(range(0, TR_max, int(TR_max / 100)))
    TE_list = list(range(0, TE_max, int(TE_max / 25)))
    # print(TE_list)

    for x in range(0, len(t1)):
        xAxis = []
        theResult = []
        for TR in TR_list:
            # TR = TR * (10 ** -3)
            shortTE_shortTR_tmp = initial * math.exp(-TE / t2[x]) * (1 - math.exp(-TR / t1[x]))
            theResult.append(shortTE_shortTR_tmp)
            xAxis.append(TR)
        finalIndex = len(theResult) - 1
        TR_final = theResult[finalIndex]
        # print(TR_final)
        for TE in TE_list:
            shortTE_shortTR_tmp = TR_final * math.exp(-TE / t2[x]) * (1 - math.exp(-TR / t1[x]))
            theResult.append(shortTE_shortTR_tmp)
            xAxis.append(TE + TR_max)
        # print(theResult[finalIndex + 1])
        plt.plot(np.array(xAxis), np.array(theResult))


    plt.legend(names)
    plt.title(titles[0])
    plt.xlabel("TR (ms)")
    plt.ylabel("Magnitude (*Mo)")
    plt.show()


together_titles = ["test"]
together(TR_max=450, TE_max=25, titles=["Short TR, Short TE (T1 Weighted)"])
together(TR_max=450, TE_max=95, titles=["Short TR, Long TE (No Signal)"])
together(TR_max=1550, TE_max=25, titles=["Long TR, Short TE (Proton Density Weighted)"])
together(TR_max=1550, TE_max=95, titles=["Long TR, Long TE (T2 Weighted)"])


# In clinical practice:
#
# TE is always shorter than TR
# A short TR = value approximately equal to the average T1 value, usually lower than 500 ms
# A long TR = 3 times the short TR, usually greater than 1500 ms
# A short TE is usually lower than 30 ms
# A long TE = 3 times the short TE, usually greater than 90 ms
# https://www.imaios.com/en/e-Courses/e-MRI/MRI-signal-contrast/Signal-weighting#:~:text=TE%20is%20always%20shorter%20than,usually%20lower%20than%2030%20ms
