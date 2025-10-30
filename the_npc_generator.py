name = ["Kevan", "Kavan", "Kevin", "Kavin", "Smevin", "Roan", "Liam", "William", "Melissa", "Jake", "Shovel", "Leo", "Jack", "Caleb", "Grunkle Stan", "Jodie", "Jody", "gurt", "Jordan", "Bartholomuew XIV Jr. Sr."]
hair = ["bald", "Mohawk", "Strawberry Fade", "Low taper fade", "Bowl cut", "Receding Hairline"]
hair_color = ["Green", "Chromatic", "Rainbow", "Gold", "Yellow", "Hot bubble gum pink"]
height = ["1'1","4,5", "6'7", "100'1", "0'11" ]
skin_color = ["Geen", "Bink", "Puorple," "Pitch black", "Neon White", "Paper", "Bright hot bubblegum pink", "void."]
clothes = ["t-shirt pants", "t-shirt shorts", "long sleeves short", "long sleeves pants", "Winter coat","skimask"]
race = ["Elf", "omega alpha skibidi sigma", "dwarf", "ogre", "draconian", "human", "SUPER small dwarf"]
characteristics = ["nice", "not nice", "funny", "rude", "arrogant", "ignorant", "caring", "loving", "shy","extroverted"]
gender = ["male", "female", "Non-binary", "male", "female", "male", "female"]
import random
import time
print("Welcome to the NPC generator!")
print("You choose a number...and I will make that many amount of NPCs.")
amount_random = int(input("Whats the amount of NPCs do you want? : "))



for i in range(amount_random) : 

    print("Name : ", random.choice(name))
    print("")
    time.sleep(0.75)
    print("Hair cut : ", random.choice(hair))
    print("")
    time.sleep(0.75)
    print("Hair color : ", random.choice(hair_color))
    print("")
    time.sleep(0.75)
    print("Height : ", random.choice(height))
    print("")
    time.sleep(0.75)
    print("Skin color : ", random.choice(skin_color))
    print("")
    time.sleep(0.75)
    print("Clothing : ", random.choice(clothes))
    print("")
    time.sleep(0.75)
    print("Race : ", random.choice(race))
    print("")
    time.sleep(0.75)
    print("Characteristics : ", random.choice(characteristics))
    print("")
    time.sleep(0.75)
    print("Gender : ", random.choice(gender))
    print("")








