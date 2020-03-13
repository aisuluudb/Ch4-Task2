
class Airplane():

    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying  = False

    def take_off(self):
        if self.make == samolet.make:
            self.is_flying = True
            print(samolet.is_flying)
       

    def fly(self):
        distance = 15000
        if distance >= 14000:
           self.odometer += 1000
           print(samolet.odometer)
    
    def land(self):
        if self.year == 2010:
            self.is_flying = False
        print(samolet.is_flying)

samolet = Airplane('airbus', 'A330', 2010, 840)
samolet.take_off()
samolet.fly()
samolet.land()
