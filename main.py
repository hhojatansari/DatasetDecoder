import datetime as dt

t0 = "2010-11-04 00:03:01.509589 M003 ON Sleeping begin"
t1 = "2010-11-04 00:03:57.399391 M003 ON Sleeping end"

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

class State:

    def __init__(self):
        self.datetime = dt.datetime.now()
        self.readed = False
        self.data = {
            "date" : "00-00-00", "time" : "00:00:00", "M001" : 0, "M002" : 0, "M003" : 0,"M004": 0, "M005" : 0,
            "M006" : 0, "M007" : 0, "M008" : 0, "M009" : 0, "M010" : 0,"M011": 0, "M012": 0, "M013": 0, "M014": 0,
            "M015": 0, "M016": 0, "M017": 0, "M018": 0,"M019": 0, "M020": 0, "M021": 0, "M022": 0, "M023": 0, "M024": 0,
            "M025": 0,"M026": 0, "M027": 0, "M028": 0, "M029": 0, "M030": 0, "M031": 0,"T001" : 20.0, "T002" : 20.0,
            "T003" : 20.0, "T004" : 20.0, "T005" : 20.0, "D001" : 0, "D002" : 0, "D003" : 0, "D004" : 0, "Label" : "NoLabel"
        }

    def textParser(self, string):
        self.readed = True
        year, month, day = string.split(" ")[0].split("-")
        hour, minute, second = string.split(" ")[1].split(":")

        year = int(year)
        month = int(month)
        day = int(day)
        hour = int(hour)
        minute = int(minute)
        second = int(round(float(second), 0))
        self.datetime = dt.datetime(year, month, day, hour, minute, second)

        self.data["date"] = str(year) + "-" + "{0:0=2d}".format(month) + "-" + "{0:0=2d}".format(day)
        self.data["time"] = "{0:0=2d}".format(hour) + ":" + "{0:0=2d}".format(minute) + ":" + "{0:0=2d}".format(second)

        if len(string.split(" ")) == 6 or len(string.split(" ")) == 4:
            if string.split(" ")[3] == "ON" or string.split(" ")[3] == "OPEN":
                self.data[string.split(" ")[2]] = 1
            elif string.split(" ")[3] == "OFF" or string.split(" ")[3] == "CLOSE":
                self.data[string.split(" ")[2]] = 0
            else:
                self.data[string.split(" ")[2]] = string.split(" ")[3]

            if len(string.split(" ")) == 6:
                if string.split(" ")[5] == "begin":
                    self.data["Label"] = ClassLabel[string.split(" ")[4]]
                elif string.split(" ")[5] == "end":
                    self.data["Label"] = ClassLabel["NoLabel"]

        else:
            print("Error:", "len of line is " + str(len(string.split(" "))))

    def printState(self):
        print(self.data["date"], self.data["time"], self.data["M001"], self.data["M002"], self.data["M003"],
              self.data["M004"], self.data["M005"], self.data["M006"], self.data["M007"], self.data["M008"],
              self.data["M009"], self.data["M010"], self.data["M011"], self.data["M012"], self.data["M013"],
              self.data["M014"], self.data["M015"], self.data["M016"], self.data["M017"], self.data["M018"],
              self.data["M019"], self.data["M020"], self.data["M021"], self.data["M022"], self.data["M023"],
              self.data["M024"], self.data["M025"], self.data["M026"], self.data["M027"], self.data["M028"],
              self.data["M029"], self.data["M030"], self.data["M031"], self.data["T001"], self.data["T002"],
              self.data["T003"], self.data["T004"], self.data["T005"], self.data["D001"], self.data["D002"],
              self.data["D003"], self.data["D004"], self.data["Label"])


LastState = State()
NewState = State()

LastState.textParser(t0)
LastState.printState()

NewState.textParser(t1)

NewState.printState()