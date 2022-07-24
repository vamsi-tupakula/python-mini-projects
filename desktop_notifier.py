# a simple project to understand how notifications work with python in windows.

from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = "Reminder!!!....",
        message = "Hey, there this how notification works..",
        timeout = 10 # notification will stay upto 10 seconds
    )