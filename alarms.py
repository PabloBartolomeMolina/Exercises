import webbrowser
import time


def alarm():

    # Get user input
    val = input("Enter time of alarm for today: ")

    # Check time is not already gone today and its format.
    if val[:2].isnumeric() and val[4:].isnumeric() and val[2] == ':':
        print("True")
        if int(val[:2]) < 24 and int(val[:2]) > 0 and int(val[3:]) < 61 and int(val[3:]) > 0:

            # Check if hour is already passed or not
            now = time.ctime()
            now = now[11:16]

            if int(val[:2]) > int(now[:2]) or (int(val[:2]) == int(now[:2]) and int(val[3:]) > int(now[3:])):
                print("True")       # Debugging purpose
                # Form string with valid format and user input
                alarmTime = time.ctime()
                alarmTime = alarmTime[:11] + val + ":00" + alarmTime[19:]
                print(alarmTime)

                while (1):
                    targetTime = time.ctime()
                    if (targetTime == alarmTime):
                        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                        break
                    else:
                        time.sleep(1)
                        print('Not yet')
        else:
            print("False 1")      # Debugging purpose
    else:
        print("False 0")          # Debugging purpose