import time
from plyer import notification


if __name__ == '__main__':
    while True:
        notification.notify(
            title="Please Drink Water",
            app_name="Drink Water Desktop App",
            message="Water keeps us hydrated",
            app_icon="D:\Programs\Python Programs\Drink water reminder\icon.ico",
            timeout=10,
            ticker="Deepak"
        )
        time.sleep(5)