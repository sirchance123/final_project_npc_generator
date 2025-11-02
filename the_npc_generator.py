name = ["Kevan", "Kavan", "Kevin", "Kavin", "Smevin", "Roan", "Liam", "William", "Melissa", "Jake", "Shovel", "Leo", "Jack", "Caleb", "Grunkle Stan", "Jodie", "Jody", "gurt", "Jordan", "Bartholomuew XIV Jr. Sr."]
hair = ["bald", "Mohawk", "Strawberry Fade", "Low taper fade", "Bowl cut", "Receding Hairline"]
hair_color = ["Green", "Chromatic", "Rainbow", "Gold", "Yellow", "Hot bubble gum pink"]
skin_color = ["Geen", "Bink", "Puorple", "Pitch black", "Neon White", "Paper", "Bright hot bubblegum pink", "void."]
clothes = ["t-shirt pants", "t-shirt shorts", "long sleeves short", "long sleeves pants", "Winter coat","skimask"]
race = ["Elf", "omega alpha skibidi sigma", "dwarf", "ogre", "draconian", "human", "SUPER small dwarf"]
characteristics = ["nice", "not nice", "funny", "rude", "arrogant", "ignorant", "caring", "loving", "shy","extroverted"]
gender = ["male", "female", "Non-binary", "male", "female", "male", "female"]
age = [6.7, 41, 6.1, 1, 101, 54, 2]
#these imports are the most important thing.  without them, randomly selecting things from lists would be 10x longer
import random
import time
print("Welcome to the NPC generator!")
print("You choose a number...and I will make that many amount of NPCs.")
amount_random = int(input("Whats the amount of NPCs do you want? : "))
random_age = random.choice(age)
#the thing above me is responsible for determining the senile trait or not
#and everything below me is the actual part that functions
for i in range(amount_random) : 

    print("Name : ", random.choice(name))
    print("")
    time.sleep(0.75)
    print("Age : ", random_age)
    print("")
    time.sleep(0.75)
    print("Hair cut : ", random.choice(hair))
    print("")
    time.sleep(0.75)
    print("Hair color : ", random.choice(hair_color))
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
    time.sleep(0.75)
    if random_age >= 55 :
        print("This NPC has been given the Senile trait.")
    else : 
        print("This NPC has been given the Young trait.")
    print("")
    print("End of NPC")
    print("------------")
    random_age = random.choice(age)
#the thing above me is what resets the age for the next npc.  normally you wouldnt need to do this, but I needed to cram a boolean somewhere in the project so I did this.







