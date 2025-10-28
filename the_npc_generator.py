name = ["Kevan", "Kavan", "Kevin", "Kavin", "Smevin", "Smevan", "Liam", "William", "Lliam", "Willliam", "Shovel", "Leo", "Leoo", "Leooo", "Leoooo", "Leeo", "Leeeo", "leeeeo", "Leeeeooooo", "Bartholomuew XIV Jr. Sr."]
hair = ["bald", "Mohawk", "Strawberry Fade", "Low taper fade", "Bowl cut", "Receding Hairline"]
hair_color = ["Green", "Chromatic", "Rainbow", "Gold", "Yellow", "Hot bubble gum pink"]
height = ["1'1","4,5", "6'7", "100'1", "0'11" ]
skin_color = ["Geen", "Bink", "Puorple," "Pitch black", "Neon White", "Paper", "Bright hot bubblegum pink", "void."]
clothes = ["t-shirt pants", "t-shirt shorts", "long sleeves short", "long sleeves pants", "Winter coat","skimask"]
race = ["Elf", "omega alpha skibidi sigma", "dwarf", "ogre", "draconian", "human", "SUPER small dwarf"]
characteristics = ["nice", "not nice", "funny", "rude", "arrogant", "ignorant", "caring", "loving", "shy","extroverted"]
gender = ["male", "female", "Non-binary", "Trans man", "trans woman"]
import random
import time
confirm = input("Do you want to generate an npc? : ")
confirm_real = confirm.capitalize()
if confirm_real == "Yes" :
    print(random.choice(name))
    print("")
    print(random.choice(hair))
    print("")
    print(random.choice(hair_color))
    print("")
    print(random.choice(height))
    print("")
    print(random.choice(skin_color))
    print("")
    print(random.choice(clothes))
    print("")
    print(random.choice(race))
    print("")
    print(random.choice(characteristics))
    print("")
    print(random.choice(gender))
else : 
    print("aw man okay...")








