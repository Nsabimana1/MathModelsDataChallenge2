
import random
import math

#getting a list of random flip coins in one trial
def getRandomResult():
    i = 0;
    data = []
    stop = False
    t = 0
    while(not stop):
        t += 1
        if(random.randint(0,1) == 0):
            data.append("H")
        else:
            data.append("T")
        if len(data) > 1 and (data[i - 1] == "T" and data[i] == "T"):
            stop = True
            break
        i += 1
    return data, t

# Generating more data by creating different n trails
def getMoreDataTrials(n):
    allData = list()
    table = {}
    for i in range(n):
        date, var = getRandomResult()
        allData.append(var)
    for i in allData:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1
    return table, allData

#Calculating Probabilities of outcomes
def calculateProbFromTrialsAndResutTable(table):
    t, d = table
    ptable = {}
    sum = 0
    for i in t:
        ptable[i] = t[i]/len(d)
        sum += ptable[i]
    return ptable, sum

#Calculating Expected Value
def getExpectedValue(table):
    Ex = 0
    for i in table:
        Ex += i*table[i]
    return Ex

#Calculating Standard Deviation
def getStandardDeviation(table, m, n):
    st = 0
    for i in table:
        st += ((i - m) ** 2)*table[i]
    return math.sqrt(st)

def main():
    # simple case for 10 trails
    l = getRandomResult()
    print("Random Trial: " + str(l))
    t, d = getMoreDataTrials(10)
    print("Lit of Results With Duplicated Occurrences:" + str(d))
    print("Table of Results With Counts of Occurrence Per OutCome: "+ str(t))

    print()
    #Bigger case for n trials
    print("Result for any Number of Trails")
    tableDataFortrials, dat = getMoreDataTrials(1000)
    tableForProbabilities, sumOfProbabilities = calculateProbFromTrialsAndResutTable((tableDataFortrials, dat))
    ExpectedValue = getExpectedValue(tableForProbabilities)
    StandardDeviation = getStandardDeviation(tableForProbabilities, ExpectedValue, 1000)

    print(tableForProbabilities, sumOfProbabilities)
    print( "Expected value is: " + str(ExpectedValue))
    print("Standard Deviation is : " + str(StandardDeviation))
    print("Data Trials in Table Format")
    print("______________")
    stringResult = "{"
    for i in sorted(tableDataFortrials.keys()):
        stringResult += "{" + str(i) + "," + str(tableForProbabilities[i]) + "},"
        print("| " + str(i) + " |  " + str(tableForProbabilities[i]) + " |")
        print("______________")
    stringResult += "}"
    print("Data Trials in Point List Format")
    print(stringResult)
main()
