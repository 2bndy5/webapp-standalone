class Drivetrain(object):
    # using BCM pins = [18, 17, 13, 22]
    def __init__(self, pins, phased = False):
        if phased:  
            from gpiozero import PhaseEnableMotor as biMotor
        else: 
            from gpiozero import Motor as biMotor
        self.motor1 = biMotor(pins[0], pins[1])
        self.motor2 = biMotor(pins[2], pins[3])

    
    def stop(self):
        self.motor1.stop()
        self.motor2.stop()
        
    def __del__(self):
        del self.motor1
        del self.motor2
# end Drivetrain class

class BiPed(Drivetrain):
    def __init__(self, pins, phased = False):
        super(BiPed, self).__init__(pins, phased)
        self.right = 0
        self.left = 0

    # pass backwards/forward (-100 to 100) as variable x
    # pass left/right (-100 to 100) as variable y
    def go(self, x, y):
        # make sure arguments are in their proper range
        x = max(-100, min(100, x))
        y = max(-100, min(100, y))
        # assuming left/right axis is null (just going forward or backward)
        self.left = y
        self.right = y
        if y == 0: 
            # if forward/backward axis is null ("turning on a dime" functionality)
            self.right = -1 * x
            self.left = x
        else: 
            # if forward/backward axis is not null and left/right axis is not null
            offset = (100 - abs(x)) / 100.0
            if x > 0:
                self.right = y * offset
            elif x < 0:
                self.left = y * offset
        
        # make sure speeds are an integer (not decimal/float) and send to motors
        if self.right > 0:
            self.motor1.backward(self.right / 100.0)
        elif self.right < 0:
            self.motor1.forward(self.right / -100.0)
        else:
            self.motor1.stop()
        
        if self.left > 0:
            self.motor2.backward(self.left / 100.0)
        elif self.left < 0:
            self.motor2.forward(self.left / -100.0)
        else:
            self.motor2.stop()
        
    # for debugging purposes
    def print(self):
        print("left =", self.left)
        print("right =", self.right)
# end BiPed class

class QuadPed(Drivetrain):
    def __init__(self, pins, phased = False):
        super(QuadPed, self).__init__(pins, phased)
        self.fr = 0 # forward/reverse direction
        self.lr = 0 # left/right direction

    # pass backwards/forward (-100 to 100) as variable x
    # pass left/right (-100 to 100) as variable y
    def go(self, x, y):
        # make sure arguments are in their proper range
        # make sure speeds are an integer (not decimal/float)
        x = int(round(max(-100, min(100, x))))
        y = int(round(max(-100, min(100, y))))
        # set the axis directly to their corresponding motors
        self.fr = y
        self.lr = x
        
        if self.fr > 0:
            self.motor1.forward(self.fr / 100.0)
        elif self.fr < 0:
            self.motor1.backward(self.fr * -0.01)
        else:
            self.motor1.stop()

        if self.lr > 0:
            self.motor2.forward(self.lr / 100.0)
        elif self.lr < 0:
            self.motor2.backward(self.lr * -0.01)
        else:
            self.motor2.stop()
    
    # for debugging purposes
    def print(self):
        print("forward/reverse =", self.fr)
        print("left/right =", self.lr)
# end QuadPed class




if __name__ == "__main__":
    import time
    # handle cmd line args
    import os
    import argparse
    # add description to program's help screen
    parser = argparse.ArgumentParser(description='testing purposes. Please try using quotes to encompass values. ie "0" or "1"')
    gps_defaults = '0'
    parser.add_argument('--d', default=gps_defaults, help='Select drivetrain type. "1" = bi-ped (R2D2 - like); "0" = quad-Ped (race car setup).')
    class args():
        def __init__(self):
            parser.parse_args(namespace=self)
            self.d = int(self.d)
    cmd = args()
    # finish get cmd line args
    
    if(cmd.d == 1):
        d = BiPed(17, 27, 22, 23)
    else: d = QuadPed(17, 27, 22, 23)
    d.go(100, 0)
    time.sleep(2)
    d.go(0, 100)
    time.sleep(2)
    d.go(100, 100)
    time.sleep(2)
    d.go(-100, 0)
    time.sleep(2)
    d.go(0, -100)
    time.sleep(2)
    d.go(-100, -100)
    time.sleep(2)
    d.stop()

    del d