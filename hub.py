from hub import BT_VCP
import hub
a = 0
motor = hub.port.B.motor
com = BT_VCP(0)
def carubaku(cb):
    global a
    if cb == 0:
        pass
    if cb==1:
        a= 1
com.callback(carubaku)
while True:
    if a == 1:
        if com.any():
            hub.led(6)
            message = com.readline()
            message = message.decode('UTF-8')
            if message == 'a':
                motor.run_for_time(500)
        else:
            hub.led(0)
    else:
        pass
