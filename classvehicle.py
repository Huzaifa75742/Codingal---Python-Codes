class vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = vehicle(240, 18)

print("The maximum speed of the vehicle is:", modelX.max_speed)
print("The mileage of the vehicle is:", modelX.mileage)