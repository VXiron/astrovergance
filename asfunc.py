import random
import database as dbas
import os
import time


def tutorial():
    list_greetings = ['Great selction', 'Beautiful selection','Beautiful choice', 'Great choice']
    greetings = random.choice(list_greetings)
    print("Welcome to Astroverge, a place where you can own your own planet ")
    print("A place of Renosance and Harmony")
    print("Each planet has its own job you can choose one")
    # Chooses The planet
    while True:
        try:
            while True:
                print("Choose Your Starting Planet"); print("Enter the number corresponding to the starter planet")
                print(dbas.planet_dict)
                starter_planet = int(input(">>>"))

                if starter_planet == 1:
                    print(f"Livid is a {greetings} selection")
                    print("_______________________________")
                    print("Livid is the living planet and supports many kinds of life forms")
                    print("Livid is a non-static planet meaning it has variational gravity and variational conditions on; each part of the planet.")
                    print("Livid is great for collecting livestock back to homebase so great selection")
                    f = open("invfile.py", "w")
                    f.write(f"owned_planets = ['{starter_planet}']")
                    f.close()
                    return True

                if starter_planet == 2:
                    print(f"Cryonix is a {greetings}, as it is a very rich mine for exotic ores")
                    print("Cryonix is biocrystallic meaning it has various mass biological crystal formations")
                    print("Cryonix is home to almost no life but has a couple of dangerous entities from the crystal formations so watch out for them!")
                    f = open("invfile.py", "w")
                    f.write(f"owned_planets = ['{starter_planet}']")
                    f.close()
                    return True
                if starter_planet == 3:
                    print(f"Resonance is a {greetings}, it is a very good planet because it has intelligent life in current planetal amity")
                    print("this means that the planet is not in war and in civil disorder so they are perfectly lawful life forms")
                    print("this place is great for workforce so that you lessen your chances of death")
                    print("One downside to this intelligent life is that if you try to force this life form they can be extremly enraged towards you and may cause problems.")
                    print("the upside is that they will usully except to be part of your work force so dont be to worried of there anger.")
                    f = open("invfile.py", "w")
                    f.write(f"owned_planets = ['{starter_planet}']")
                    f.close()
                    return True
                if starter_planet == 4:
                    print(f"Cryptical is a {greetings}, This is because it is a more microbionical planet meaning it has microbes useful for finding, settling and harvesting on new planets.")
                    print("The microbionical creatures are extremely resilient to many kinds of enviornments in space and one planets.")
                    print("As much as the se microbial creatures are useful, they can also be dangerous if not kept in a safe place, as they can eat through many weak metals like aluminum and iron and can be carnivorous if left starving so feed them frequently and keep them in a safe spot to avoid danger.")
                    f = open("invfile.py", "w")
                    f.write(f"owned_planets = ['{starter_planet}']")
                    f.close()
                    return True
                if starter_planet == 5:
                    print(f"Zealous is an {greetings}, This planet is a very unstable but very rich planet full of Exotic ores")
                    print("The reason this is an unstable planet is because it is a rouge planet in dangerous territories with wormholes and this planet will sometimes go through wormholes and be temporarily unstable while the wormhole alter zealous's properties as it is going through.")
                    print("Zealous travel distance may alter depending on where its wormholes take it where as it could go from 3 hours to 10 days")
                    f = open("invfile.py", "w")
                    f.write(f"  owned_planets = ['{starter_planet}']")
                    f.close()
                    return True
                else:
                    print("This is not a valid response to the input please try again")
                    time.sleep(2)
        except Exception as a:
            print("Hey, No Letters Enter a number please")
            time.sleep(2)
            os.system('clear')
        time.sleep(5)
        print("we hope you enjoy the astroverge, and make sure, dont die, good night!")
        time.sleep(3)
        os.system('clear')

            
    
        

    

def gameplay():
    print("YOU FINISHED TUTORIAL")