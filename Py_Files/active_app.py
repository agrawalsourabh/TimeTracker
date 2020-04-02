import json
from datetime import date
import os

class ActivityData:
    __key = ['name', 'duration']
    __activity_list = []
    __json_data = None
    __filename = None
    __filedir = None

    def __init__(self):
        print('Inside active-app cons')
        self.__filedir = '../user_activity_data/' + str(date.today().year) + '/' + str(date.today().month)
        if not os.path.exists(self.__filedir):
            os.makedirs(self.__filedir)
        self.__filename = self.__filedir + '/' + str(date.today().day) + '.json'

    def save_activity_data(self, act_name, act_duration):
        value = [act_name, round(act_duration, 2)]
        index = self.__getIndex(act_name)

        if index != -1 and len(act_name) > 0:  # activity already present
            self.__activity_list[index]['duration'] = round(self.__activity_list[index]['duration'] + act_duration, 2)

        elif len(act_name) > 0:  # First Activity or Unique Activity
            self.__activity_list.append(dict(zip(self.__key, value)))

    # This is a private function, returns the index of act_name if present, otherwise returns -1
    def __getIndex(self, act_name):
        index = -1
        flag = False

        # if first activity is being add - function will returns -1
        if len(self.__activity_list) == 0:
            return index

        # if activity_list contains some activities, for loop will search each activity for act_name
        else:
            for activity in self.__activity_list:
                index = index + 1

                # if act_name is present in the activity_list - set flag = true
                if activity['name'] == act_name:
                    flag = True
                    break

        # check the flag
        # if flag = False, that means act_name is not present, it will return -1
        if not flag:
            return -1
        # else it will return the index
        else:
            return index

    def printActivityData(self):
        print(self.__activity_list)

    def dumpListToJson(self):
        self.__json_data = json.dumps(self.__activity_list)
        # json.du

    def saveDataToFile(self):
        print(self.__filename)
        file = open(self.__filename, "w+")
        file.write(self.__json_data)
        file.close()
        print("File saved.")
