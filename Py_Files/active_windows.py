import win32gui as win
import time
from .active_app import ActivityData


def isWindowChanged(current_window):
    if current_window != win.GetForegroundWindow():
        return True
    else:
        return False


class UserActiveWindow:
    current_window = None
    counter = 1
    save_data = None

    def __init__(self):
        self.save_data = ActivityData()

    def current_active_window(self):
        while self.current_window != win.GetForegroundWindow() and self.counter < 20:
            # store the current active window in current_window
            # and take the start time in variable tic
            tic = time.perf_counter()
            self.current_window = win.GetForegroundWindow()

            # get the name of the current active window
            current_window_name = str(win.GetWindowText(self.current_window))

            # if self.current_window != " ":
            # print("Current Active window")
            # print(str(self.counter) + " " + current_window_name)

            while True:
                # time.sleep(0.05)
                if isWindowChanged(self.current_window):
                    toc = time.perf_counter()
                    dur = toc - tic
                    self.save_data.save_activity_data(current_window_name, dur)
                    self.counter = self.counter + 1
                    # print("========================================")
                    break

    def print_data(self):
        self.save_data.printActivityData()

    def save_to_file(self):
        self.save_data.dumpListToJson()
        self.save_data.saveDataToFile()