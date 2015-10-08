# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:  John Kautzner
# Collaborators:  None
# Time:  0:00
#

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    Dict = {}

    inputFile = open(filename)
    for line in inputFile:
        words = []
        word = ''
        for l in line:
            if l == ',' or l == '\n':
                words.append(word)
                word = ''
            else:
                word += l

        words.append(word)
        Dict[words[0]] = (int(words[1]), int(words[2]))

    return Dict

    # Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).


def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

subjects = loadSubjects(SUBJECT_FILENAME)
# printSubjects(subjects)


#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    #print "sub1 = ", subInfo1[0], "  sub2 = ", subInfo2[0]
    return subInfo1[0] > subInfo2[0]


def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """

    return subInfo1[1] < subInfo2[1]

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """

    return (subInfo1[0]+0.0)/subInfo1[1] > (subInfo2[0]+0.0)/subInfo2[1]


def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """

    work = 0
    subs = subjects.copy()
    greeDict = {}

    while work < maxWork and len(subs) > 0:
        badList = []
        for s in subs:

            if work + subs[s][1] > maxWork:
                badList += [s]

        for b in badList:
                del subs[b]

        if len(subs) != 0:
            best = subs.keys()[0]  #best starts as first element in the dict.

            for s in subs:
                if comparator(subs[s], subs[best]):
                    best = s

            # print "best = ", best, "   work = ", subs[best][1]
            # print "badList = ", badList
            # print "work = ", work
            work += subs[best][1]
            greeDict[best] = subs[best]
            del subs[best]


    return greeDict


smallCatalog = \
{'6.00': (16, 8),
'1.00': (7, 7),
'6.01': (5, 3),
'15.01': (9, 6)}


#greedyAdvisor(smallCatalog, 15, cmpWork)

#greedyAdvisor(subjects, 15, cmpWork)

#
# Problem 3: Subject Selection By Brute Force
#
# def recursDictBuilder(subjects, maxWork, dict):

def weightOfList(subjects, solutionList):
    """
    :param subjects: dictionary mapping subject name to (value, work)
    :param solutionDict: List of classes (potential solution)
    :return:  total work of solutionList
    """

    weight = 0

    for d in solutionList:
        weight += subjects[d][1]

    return weight

#weightOfList(subjects, ['6.00', '3.01', '2.03'])

def findBestList(subjects, listOfSolutions):
    """

    :param subjects: dictionary mapping subject name to (value, work)
    :param listOfSolutions: a list of lists (list of potential solutions)
    :return: the list with the highest total value
    """

    best = listOfSolutions.keys()[0]

    for l in listOfSolutions:
        for m in listOfSolutions:
            if weightOfList(subjects, m) > weightOfList(subjects, l):
                best = m

    print m
    return m




def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """


# Make this a method called def getListOfDicts(subjects) and put it above the current method.  May need to put maxWork within.


    #  Write a method that goes through remaining dicts and finds the one with the highest value.

    dicts = {'0':[0]}
    fullDicts = {}

    for x in subjects:
        newElements = {}  # A list containing the previous lists with x appended to each

        for d in dicts:
            print "d = ", d
            e = dict(d)     #This isn't working because d isn't a dict right now. It's just an element of a dict.  Must convert first?
            print "e = ", e
            print "x = ", x
            e.update(x)
            print "e = ", e
            newElements.update(e)

        #for n in newElements:       # If the new dicts are full, don't add them to list that grows
        #    if weightOfList(subjects, n) == maxWork:
         #       fullDicts += n

          #  elif weightOfList(subjects, n) < maxWork:
           #     dicts += newElements

    dicts += fullDicts
    return dicts


# bruteForceAdvisor([0,1,2,3], 15)
bruteForceAdvisor(smallCatalog,15)
#findBestList(subjects, bruteForceAdvisor(subjects, 15))

#dictDict = {str(smallCatalog):(7, 3)}
#dicTac = {'apple':(1,4)}
#dictDict.update(dicTac)
#print dictDict