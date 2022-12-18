# source from https://www.youtube.com/watch?v=KshTf2A5aUk and
# https://www.devdungeon.com/content/windows-desktop-notifications-python

# python -m pip install win10toast
from win10toast import ToastNotifier
import time

# One-time initialization
toaster = ToastNotifier()

# Show notification whenever needed
toaster.show_toast("Notification!", "Alert!", threaded=True,
                   icon_path=None, duration=3)  # 3 seconds

# To check if any notifications are active,
# use `toaster.notification_active()`
while toaster.notification_active():
    time.sleep(0.1)
