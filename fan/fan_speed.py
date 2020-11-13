


def fan_speed_control(compressor_status):

    if compressor_status:
        msg = 'Fan work 80 percentage power'

    else:
        msg = 'Fan work 20 percentage power'

    return msg