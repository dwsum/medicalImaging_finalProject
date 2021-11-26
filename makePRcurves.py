import numpy as np
from matplotlib import pyplot
from sklearn.metrics import precision_recall_curve


#NOTE: 1 means it is touching
actual_1 = [0, 0, 0, 1, 0, 1, 1, 1, 0, 0]
actual_5 = [0, 0, 0, 1, 0, 1, 1, 1, 0, 0]
actual_15 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
actual_25 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
actual_35 = [0, 0, 0, 0, 1, 0, 0, 1, 0, 1]

#initiate to save all the data.
allSubjects_1 = []
allSubjects_5 = []
allSubjects_15 = []
allSubjects_25 = []
allSubjects_35 = []

def combineSubjects(test1, test5, test15, test25, test35):
    global allSubjects_1, allSubjects_5, allSubjects_15, allSubjects_25, allSubjects_35
    allSubjects_1 = allSubjects_1 + test1
    allSubjects_5 = allSubjects_5 + test5
    allSubjects_15 = allSubjects_15 + test15
    allSubjects_25 = allSubjects_25 + test25
    allSubjects_35 = allSubjects_35 + test35

#Dad
subject_1 = [0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
subject_5 = [0, 0, 0, 1, 0, 1, 1, 1, 1, 0]
subject_15 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
subject_25 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
subject_35 = [0, 0, 0, 0, 1, 0, 0, 1, 0, 1]
combineSubjects(subject_1, subject_5, subject_15, subject_25, subject_35)


#Jeff
subject_1 = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
subject_5 = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
subject_15 = [0, 0, 0, 0, 1, 1, 0, 0, 1, 1]
subject_25 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
subject_35 = [0, 0, 0, 0, 1, 0, 0, 1, 0, 1]
combineSubjects(subject_1, subject_5, subject_15, subject_25, subject_35)

#Mom
subject_1 = [0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
subject_5 = [0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
subject_15 = [1, 0, 0, 0, 0, 1, 0, 0, 1, 1]
subject_25 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
subject_35 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
combineSubjects(subject_1, subject_5, subject_15, subject_25, subject_35)

#Dan
subject_1 = [0, 0, 0, 1, 0, 1, 0, 1, 1, 0]
subject_5 = [0, 0, 1, 1, 0, 1, 1, 1, 0, 0]
subject_15 = [0, 0, 0, 0, 0, 1, 0, 0, 1, 1]
subject_25 = [0, 0, 0, 0, 1, 0, 1, 0, 0, 1]
subject_35 = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
combineSubjects(subject_1, subject_5, subject_15, subject_25, subject_35)

#Rachel
subject_1 = [0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
subject_5 = [0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
subject_15 = [0, 0, 0, 0, 0, 1, 0, 0, 1, 1]
subject_25 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
subject_35 = [0, 0, 0, 0, 1, 0, 0, 1, 0, 1]
combineSubjects(subject_1, subject_5, subject_15, subject_25, subject_35)


def make_PR_curve(this_allSubjects, this_actual, numMRI):
    theActual = []
    label = str(numMRI) + " scans"
    print(len(this_allSubjects))
    for x in range(0, int(len(this_allSubjects) / 10)):
        theActual = theActual + this_actual
    # pyplot.figure(figureNum)
    precision, recall, thresholds = precision_recall_curve(np.array(theActual), np.array(this_allSubjects))
    pyplot.plot(recall, precision, marker='.' , label=label)

    # pyplot.ylim(0.995, 1.01)  # have it go down to 0.85



#for the 1 MRI
make_PR_curve(allSubjects_1, actual_1, 1)
make_PR_curve(allSubjects_5, actual_5, 5)
make_PR_curve(allSubjects_15, actual_15, 15)
make_PR_curve(allSubjects_25, actual_25, 25)
make_PR_curve(allSubjects_35, actual_35, 35)

pyplot.xlabel('Recall')
pyplot.ylabel('Precision')
pyplot.title("MRI Scans (Sample Size: " + str(int(len(allSubjects_1) / 10)) + str(")"))
pyplot.legend()
pyplot.show()


