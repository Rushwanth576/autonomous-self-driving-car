import serial, time
class MotorLink:
    def __init__(self, port, baud):
        self.ser=serial.Serial(port, baud, timeout=0.2); time.sleep(2)
    @staticmethod
    def clamp(v): return max(-255,min(255,int(v)))
    def drive(self,left,right): self.ser.write(f"L{self.clamp(left)},R{self.clamp(right)}\n".encode())
    def stop(self): self.drive(0,0)
    def close(self):
        try: self.stop()
        finally: self.ser.close()
