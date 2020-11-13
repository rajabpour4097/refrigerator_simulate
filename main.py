from compressor import on_off_compressor
from random import randint
from time import sleep




if __name__ == "__main__":

    print('Welcome to program')
    user_temp = int(input('Enter your temp: '))

    while True:
        # user_temp = randint(0, 10)
        sensor_temp = randint(0, 10)
        print('User:', user_temp, 'Sensor:', sensor_temp)
        on_off_compressor(user_temp, sensor_temp)
        sleep(3)
        print('#' * 30)

    # print(on_off_compressor(6, 1))
