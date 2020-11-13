from fan import fan_speed_control
from termcolor import colored
import pygame


def on_off_compressor(user_temp, sensor_temp):

    msg = ''
    compressor = False
    pygame.init()
    s = pygame.mixer.Sound("./compressor/beep-07.wav")

    if user_temp <= sensor_temp:
        msg = colored('compressor is on', 'green')
        compressor = True
        fan_order = fan_speed_control(compressor)
        s.play()
    else:
        msg = colored('compressor is off', 'red')
        compressor = False
        fan_order = fan_speed_control(compressor)

    # return msg, fan_order
    print(msg)
    print(colored(fan_order, 'blue'))