class Vehicle :
    def __init__(self,color,body_material, capacity, fuel_type, max_speed):

        self.color=color
        self.body_material = body_material
        self.capacity = capacity
        self.fuel_type = fuel_type
        self.total_distance = 0 
        self.speed_ = 0       
        self.distance_ = 0       
        self.max_speed = max_speed

    def speed (self,n_speed) :
        if 0 <= n_speed <= self.max_speed :
            self.speed_ = n_speed
            print(f"Speed is : {self.speed_} ")

    def increase_speed (self, amount) :
        self.speed_ += amount
        if self.speed_ > self.max_speed :
            self.speed_ = self.max_speed 
        print(f"Speed increaseed to : {self.speed_ }")

    def decreased_speed(self, amount2):
        self.speed_ -= amount2
        if self.speed_ < 0:
            self.speed_ = 0
        print(f"Speed decreased to : {self.speed_}")


    def distance (self,hour) :
        distance_moved = self.speed_ * hour
        self.total_distance += distance_moved
        print(f"moved now {distance_moved} m >> Toyaly you moved {self.total_distance} m")

class Car (Vehicle) :
    def __init__(self, color, body_material, capacity, fuel_type, max_speed ,doors):
        super().__init__(color, body_material, capacity, fuel_type, max_speed)
        self.doors = doors

class Bike (Vehicle) :
    def __init__(self, color, body_material, capacity, fuel_type, max_speed, pedal):
        super().__init__(color, body_material, capacity, fuel_type, max_speed)
        self.pedal = pedal

c1 = Car("white", "iron", 5, "gas", 200, 4)
c1.speed(150)
c1.increase_speed(20)
c1.decreased_speed(40)
c1.distance(20)