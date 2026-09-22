import time
import cv2
from serial_motor import MotorController
from lane_detection import detect_lane
from obstacle_detection import Ultrasonic
from traffic_signal import detect_traffic_signal
from sign_detection import detect_sign

SIMULATION_MODE=True
SERIAL_PORT="/dev/ttyACM0"
BASE_SPEED=125
STOP_DISTANCE_CM=25

def autonomous_step(frame,motors,ultrasonic):
    error,_=detect_lane(frame)
    signal=detect_traffic_signal(frame)
    sign=detect_sign(frame)
    distance=ultrasonic.distance_cm()

    if distance < STOP_DISTANCE_CM or signal=="RED":
        motors.stop()
        return {"action":"STOP","distance":distance,"signal":signal,"sign":sign}

    correction=int(error*90)
    left=BASE_SPEED+correction
    right=BASE_SPEED-correction
    if signal=="YELLOW":
        left=int(left*.55); right=int(right*.55)
    motors.drive(left,right)
    return {"action":"DRIVE","distance":distance,"lane_error":round(error,3),
            "signal":signal,"sign":sign}

def main():
    motors=MotorController(SERIAL_PORT,115200,SIMULATION_MODE)
    ultrasonic=Ultrasonic(simulation=SIMULATION_MODE)
    cap=cv2.VideoCapture(0)
    try:
        while True:
            ok,frame=cap.read()
            if not ok: break
            print(autonomous_step(frame,motors,ultrasonic))
            if cv2.waitKey(1)&0xFF==ord("q"): break
    except KeyboardInterrupt:
        pass
    finally:
        motors.stop(); motors.close()
        cap.release(); cv2.destroyAllWindows()

if __name__=="__main__":
    main()
