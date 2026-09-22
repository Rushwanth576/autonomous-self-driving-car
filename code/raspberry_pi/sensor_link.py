class SensorLink:
    def __init__(self, ser): self.serial=ser
    def request_sensors(self):
        self.serial.write(b"S\n"); line=self.serial.readline().decode('ascii','ignore').strip(); v={}
        for p in line.split(','):
            if p.startswith('I0'): v['ir_left']=int(p[2:])
            elif p.startswith('I1'): v['ir_right']=int(p[2:])
            elif p.startswith('D'):
                try:v['distance']=float(p[1:])
                except ValueError:v['distance']=999
        v.setdefault('ir_left',1);v.setdefault('ir_right',1);v.setdefault('distance',999);return v
