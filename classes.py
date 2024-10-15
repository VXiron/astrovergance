class Planet:
    def __init__(self,name,radiation_level, gravity_strength,rocky,gas_giant,
                 goldzone,habitable,mass,atmosphere,special_affects):
        self.name = name
        self.radiation_level = radiation_level
        self.gravity_strength = gravity_strength
        self.rocky = rocky
        self.gas_giant = gas_giant
        self.goldzone = goldzone
        self.habitable = habitable
        self.mass = mass
        self.atmosphere = atmosphere
        self.special_affects = special_affects
class Rocket: 
   def __init__(self,speed,amount_of_fuel,size,mass,material, fuel_type,cost):
       self.speed = speed
       self.amount_of_fuel = amount_of_fuel
       self.size = size
       self.mass = mass
       self.material = material
       self.fuel_type = fuel_type
       self.cost = cost
    
class Minerals:
    def __init__(self, name,radiation,ore_type,rarity, sell_price, ore_id):
        self.name = name
        self.radiation = radiation
        self.ore_type = ore_type
        self.rarity = rarity
        self.sell_price = sell_price
        self.ore_id = ore_id
class Suits:
    def __init__(self,name, radition_resist, weight, special_affects, 
                 debris_resistance):
        self.name = name
        self.radiation_resist = radition_resist
        self.weight = weight
        self.special_affects = special_affects
        self.debris_resistance = debris_resistance
