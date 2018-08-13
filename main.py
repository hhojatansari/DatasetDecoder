import os
import sys
from State import State

ClassLabel = {
    "NoLabel" : "0",
    "Meal_Preparation" : "1",
    "Relax" : "2",
    "Eating" : "3",
    "Work" : "4",
    "Sleeping" : "5",
    "Wash_Dishes" : "6",
    "Bed_to_Toilet" : "7",
    "Enter_Home" : "8",
    "Leave_Home" : "9",
    "Housekeeping" : "10",
    "Respirate" : "11"
}

LastState = State()
NewState = State()
directory = os.path.dirname(sys.modules['__main__'].__file__)
outputDataset = open(directory+"/Dataset/OutPut", "w")

with open(directory+"/Dataset/data", "r") as Dataset:

    LastState.textParser(Dataset.readline())

    for line in Dataset:

        NewState.textParser(line)

        if(NewState == LastState):
            LastState.textParser(line)
            continue

        for s in range(0, (NewState - LastState)):
            LastState.writeState(outputDataset)
            LastState.incrementTime()

        LastState.writeState(outputDataset)
        LastState.textParser(line)

    Dataset.close()

LastState.writeState(outputDataset)
outputDataset.close()

print("#outputDataSet's line: ", LastState.counter)
