import time

def pomodoro_timer():
    print("Focus timer started!")
    for i in range(4):
        time.sleep(1500) # 25 minutes
        print("Time to take a break! Five minutes starting now.")
        time.sleep(300) # 5 minutes
    print("Congratulations! You have completed a full cycle.")

pomodoro_timer()
