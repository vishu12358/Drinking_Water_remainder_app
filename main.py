import time
from plyer import notification

while True:
    print("Please drink water now!")
    notification.notify(title="Drink Some Water Reminder",
                        message="you need to drink some water!")
    time.sleep(60*60) 