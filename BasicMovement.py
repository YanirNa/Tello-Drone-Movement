from djitellopy import tello
from time import  sleep


me=tello.Tello()
me.connect()
print(me.get_battery())
me.takeoff()
me.send_rc_control(0,0,50,0)
sleep(2)#the height
#             left_right_velocity: -100~100 (left/right)
#             forward_backward_velocity: -100~100 (forward/backward)
#             up_down_velocity: -100~100 (up/down)
#             yaw_velocity: -100~100 (yaw)

me.send_rc_control(0,45,0,0)
sleep(6)#walk to door
me.send_rc_control(0,0,0,0)
sleep(4)#holdstill
me.send_rc_control(0,0,0,50)
sleep(3)#turn right

me.send_rc_control(0,30,0,0)
sleep(6)#walk right

me.send_rc_control(0,0,0,0)


# me.send_rc_control(0,0,0,40)
# sleep(4)#turn right
#
# me.send_rc_control(0,40,0,0)
# sleep(3)#walk to table to land


me.send_rc_control(0,0,0,0)
sleep(2)
me.land()
