from threading import Thread
import time

def car(speed, pilot):
    route = 0
    while route <= 100:
        route += speed
        time.sleep(0.5)
        print(f'Pilot: {pilot}, Km {route}')


t_car1 = Thread(target = car, args = [20, 'Paul'])
t_car2 = Thread(target = car, args = [10, 'Del'])

t_car1.start()
t_car2.start()