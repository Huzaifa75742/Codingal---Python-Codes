import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    randomGen = random.Random()
    dateFormat = "%d-%m-%Y"

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = randomGen.uniform(startTime, endTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print(getRandomDate("01-01-2020", "31-12-2020"))
