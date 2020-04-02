from Py_Files.active_windows import UserActiveWindow
from win10toast import ToastNotifier

def main():
    toaster = ToastNotifier()
    toaster.show_toast("Time Tracking", "Task is Running")

    userActiveWindows = UserActiveWindow()
    userActiveWindows.current_active_window()
    userActiveWindows.print_data()
    userActiveWindows.save_to_file()

    toaster.show_toast("Time Tracking", "User Activity file created")


if __name__ == "__main__":
    main()
