import time# time.time() method of Time module is used to get the time in seconds
import sys#The sys module provides access to system-specific parameters and functions in Python. 
#It allows you to interact with the Python interpreter and access command-line arguments
from collections import Counter #counter is the number counter and collections
import random #this is for random number generator
def print1(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print()
def printtext(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.045)
    print()
def printmorning(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
def printbus(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.3)
    print()
inventory = Counter()

def add_items(current_inventory, items_to_add):
    # If items_to_add is a dictionary
    if isinstance(items_to_add, dict):
        current_inventory.update(items_to_add)
    # If items_to_add is a list
    elif isinstance(items_to_add, list):
        current_inventory.update(Counter(items_to_add))
    return current_inventory
def lose_items(current_inventory, items_to_lose):
    # If items_to_lose is a dictionary
    if isinstance(items_to_lose, dict):
        for item, count in items_to_lose.items():
            current_inventory[item] -= count
            if current_inventory[item] < 0:
                current_inventory[item] = 0
    # If items_to_lose is a list
    elif isinstance(items_to_lose, list):
        for item in items_to_lose:
            current_inventory[item] -= 1
            if current_inventory[item] < 0:
                current_inventory[item] = 0
    return current_inventory
def remove_item(current_inventory, item_to_remove):
    if item_to_remove in current_inventory:
        del current_inventory[item_to_remove]
    return current_inventory
game_state = {
    "yarn_picked_up": False,
    "morning_getting_ready": False,
    "throw_toothpaste":False,
    "paint_and_brushes":False,
    "symbol":False,
    "salt":False,
    "placed_salt":False,
    "pc":False,
    "scissors":False,
    "number":False,
    "deathmark":False,
    "cafevisit":False,
    "tied_yarn":False,
    "mirror_check":False,
    "3_am_sleep":False,
    "tied_phone":False,
    "deathmark2":False,
    "coin":False,
    "coin 1":False,
    "coin 1 buy":False,
    "note 1":False,
    "note 2":False,
    "note 3":False,
    "vending_machine":False,
    "correct_bus":False,
    "spook":False,
    "walked":False,
    "fish_dead":False,
    "water":False,
    "Blessing_Book":False,
    "offerings":False,
    "burned":False,
    "second_visit":False,
    "key_1":False,
    "key_2":False,
    "key_3":False,
    "bucket":False,
    "how_boat":False,
    "water_bucket":False,
    "fight_win":False,
    "more keys":False,
    "third_visit":False,
    "getmeout keys":False,
    "ending_1":False,
    "ending_2":False,
    "ending_3":False,
    "ending_4":False,
    "ending_5":False,
    "ending_6":False,
    "ending_7":False,
    "ending_8":False,
    "ending_9":False,
    "ending_10":False,
    "true_ending":False,
    "trueanswer":False,

}#game States are the things you have already done and it will be marked true if you have done it

def get_input(prompt=""):
    choice = input(prompt).strip().lower()
    
    # Check if player wants to access inventory
    if choice in ["i", "inventory"]:
        print(inventory)  # Open the inventory
    elif choice in ["notes"]:
        if game_state["note 1"]:
            print("'Train 1 is going to be delayed by approximately 3 minutes, due to boarding errors at the previous stop.' 'Make sure to update the schedule accordingly'")
            print()
        if game_state["note 2"]:
            print(r"'DO NOT REMOVE LABEL: This seat is made with 2% real leather and the rest are probably some toxic chemicals from the power plants in America, or something.'")
            print("Actually, they don't tell us what these are made of, there's probably only 3 people who read labels like this anyway")
            print()
        if game_state["note 3"]:
            print("'Honestly, people can't even use public restrooms nowadays, everything is always so crowded.'")
            print("'I mean, I'm stuck here with 3 people and only 2 urinals, and one of them is broken! When are the maintenance people going to fix this...'")
    elif choice in ["book"]:
        if game_state["Blessing_Book"]:
            print("*Tsukuyomi...*")
            print("*Once every blue moon you get a chance to get a blessing from the God named 'Tsukuyomi'")
            print("To get this blessing you much give it food or sake")

        return None  # Return None to re-prompt the current context
    return choice  # Return the actual input otherwise

#game_state Creates a Dictionary this makes it good to track of whether the player has picked up the yarn ball.
#notes dict is a dictionary is a data type that represents a collection of key-value pairs and a way to store data
#isinstance is to check if an object (or instance) is of a specific class or a tuple of classes.

def morning_routine():#def definitions are the equivalent of folders that contain code and when I open it or use it I will run all this code
    while True:#while true is basically the looping system of the game to break it you put break
        if not game_state["morning_getting_ready"]:
            printmorning("*Task: Get ready to go out*")
        
        if not game_state["pc"]:#as long as this is not true then this will print
            printmorning("*Task: Get on the pc to do some research*")

        printmorning("What would you like to do?\n1. Check the PC\n2. Check the desk\n3. Check the closet\n4. Leave")
        choice = get_input("")  # Use centralized input 

        if choice is None:
            continue  # If inventory was opened, re-prompt
        
        if choice in ["1", "pc", "check pc"]:
            interact_pc()
        elif choice in ["2", "desk"]:
            if not game_state["yarn_picked_up"]:
                printmorning("*You find a yarn ball on the desk.*")
                pick_up = input("Do you want to pick up the yarn ball? (yes/no): ").strip().lower()
                if pick_up == "yes":
                    game_state["yarn_picked_up"] = True #basically verifies if I have done it
                    add_items(inventory, ["yarn"]) #adding items to inventory
                    printmorning("*You pick up the yarn ball and add it to your inventory.*")
                    printmorning("*type in 'i' to see inventory*")
                else:
                    print1("*You decide to leave the yarn ball where it is.*")
            else:
                printmorning("*You don't find anything of note on the desk*")
        elif choice in ["3", "check closet"]:
            printmorning("*You find your pajamas and outdoors clothing*")
            if game_state.get("morning_getting_ready", False):
                print1("Yunli: I have already gotten changed.")
            else:
                ready_choice = input("Do you want to get ready? (yes/no): ").strip().lower()
                if ready_choice == "yes":
                    printmorning("*You get changed.*")
                    game_state["morning_getting_ready"] = True
                elif ready_choice == "no":
                    print1("*You close the closet.*")
        elif choice in ["4", "leave"]:
            if not game_state["pc"]:
                printmorning("Yunli: I should do some research first")            
            else:
                upstairs_hallway()  
                break  
        elif choice in ["true"]:
            game_state["ending_1"] = True
            game_state["ending_2"] = True
            game_state["ending_3"] = True
            game_state["ending_4"] = True
            game_state["ending_5"] = True
            game_state["ending_6"] = True
            game_state["ending_7"] = True
            game_state["ending_8"] = True
            game_state["ending_9"] = True
            game_state["key_1"] = True
            game_state["key_2"] = True
            game_state["key_3"] = True
            printmorning("*You suddenly appear in a strange forest*")
            printmorning("Yunli: Wha- How did I get here!?")
            unknown_forest()
            break


def night_time_routine():
    total_deaths = 0
    while True:
        printmorning("What would you like to do?\n1. Check the PC\n2. Check the desk\n3. Check the closet\n4. Sleep\n5. Leave")
        choice = get_input("")  # Use centralized input 

        if choice is None:
            continue  # If inventory was opened, re-prompt
        
        if choice in ["1", "pc", "check pc"]:
            interact_pc()
        elif choice in ["2", "desk"]:
            if not game_state["yarn_picked_up"]:
                printmorning("*You find a yarn ball on the desk.*")
                pick_up = input("Do you want to pick up the yarn ball? (yes/no): ").strip().lower()
                if pick_up == "yes":
                    game_state["yarn_picked_up"] = True
                    add_items(inventory, ["yarn"])
                    printmorning("*You pick up the yarn ball and add it to your inventory.*")
                    printmorning("*type in 'i' to see inventory*")
                else:
                    print1("*You decide to leave the yarn ball where it is.*")
            else:
                printmorning("*You don't find anything of note on the desk*")
        elif choice in ["3", "check closet"]:
            printmorning("*You you find your pajamas and outdoors clothing*")
            print1("*You close the closet*")

        elif choice in ["4", "sleep"]:
            if game_state["symbol"]: # Can remove if you think this is too railroad-ish (I think so too)
                if not game_state["3_am_sleep"]:
                    if game_state["deathmark"]:
                        total_deaths += 1
                        print1("*You slowly close your eyes.*")
                        print1("*An hour passes by... You wake up to a loud noise.*")
                        print1("Yunli: What the...?")
                        print1("*You see a tall, slim entity with a mysterious dark substance flowing from its mouth.*")
                        print1(". . .")
                        print1("*You feel a sharp pain within your body...*")
                        print1("*As you slowly close your eyes, your blood slowly leaves your body...*")
                        print1("*You bleed out.*")
                        game_state["ending_1"] = True
                        print1("Ending 1 - False Ritualist")
                        if total_deaths == 2:
                            print1("It happened again...")
                            print1("How about we tone down the rituals, especially if you're going to screw it up")
                        elif total_deaths > 2:
                            print1("You really should read the instructions again...")
                        else:
                            print1("Well that was... something.")
                            print1("Let's go back to before you went to sleep...")


                    elif game_state["deathmark2"]:
                        total_deaths += 1
                        print1("*You slowly close your eyes.*")
                        print1("*An hour passes by... You wake up to a loud noise.*")
                        print1("Yunli: What the...?")
                        print1("*You see a tall, slim entity with a mysterious dark substance flowing from its mouth.*")
                        print1(". . .")
                        print1("*You feel a sharp pain within your body...*")
                        print1("*As you slowly close your eyes, your blood slowly leaves your body...*")
                        print1("*You bleed out.*")
                        print1("Ending 1 - False Ritualist")
                        game_state["ending_1"] = True
                        if total_deaths == 2:
                            print1("It happened again...")
                            print1("How about we tone down the rituals, especially if you're going to screw it up")
                            print1("Let's go back to before you went to sleep...")
                        elif total_deaths > 2:
                            print1("You really should read the instructions again...")
                            print1("Let's go back to before you went to sleep...")
                        else:
                            print1("Well that was... something.")
                            print1("Let's go back to before you went to sleep...")
                

                    else:
                        print1("*A couple hours pass by...")
                        printmorning("*beep* " * 3)
                        printmorning("*yawns*")
                        printmorning("*You look at the alarm*")
                        printmorning("*3 am...*")
                        game_state["3_am_sleep"] = True
                else:
                    printmorning("Yunli: I'm not tired right now...")
            else:
                printmorning("Yunli: I should at least start the ritual")
                
        elif choice in ["5", "leave"]:
            upstairs_hallway()  
            break  

def interact_pc():
    printmorning("*You boot up the PC...*")
    while True:
        printmorning("What would you like to do?\n1. Go on Chrome\n2. Play music\n3. Power off")
        choice = input().strip().lower()

        if choice in ["1", "chrome"]:
            printmorning("*You open a tab on 'Akumu no Tabi' and read about a ritual...*")
            print1("*You see a list to perform a ritual.*")
            print1("*Unknown user:*")
            print1("- Pour salt near the front door.")
            print1("- Enter the garage, and paint a pentagon with red paint on the floor.")
            print1("- Then, put a ribbon on each side of the pentagon.")
            print1("- Wait until 3 AM.")
            print1("- Get a home phone and tie a ribbon onto it.")
            print1("- Call the number 670 999 663.")
            print1("- Say 'Hello', you will get a response, then ask 'Are you here?'")
            print1("Do NOT mess up.")
            print1("*Demon Hunter:*")
            print1("Is this the real deal?")
            print1("*Unknown user:*")
            print1("Don't know, but whoever did it never came back.")
            print1("Yunli: Looks interesting!")
            game_state["pc"] = True
        elif choice in ["2", "music"]:
            number = random.randrange(1, 4) # i think this needs to be 1,4 since wildfire never plays
            if number == 1:
                printmorning("*You play 'Salty Moon Â· HOYO-MiX' softly in the background.*")
            elif number == 2:
                printmorning("*You play 'Hartmann's Youkai Girl - Team Shanghai Alice' softly in the background.*")
            elif number == 3:
                printmorning("*You play 'Wildfire - HOYO-MIX' very loudly in the background.*")
        elif choice in ["3", "off", "leave"]:
            printmorning("*You turn off the PC...*")
            break

def interact_bathroom():
    check_counter = 0
    while True:
        if not game_state["morning_getting_ready"]:
            printmorning("*Task: Get ready to go out*")
        if not game_state["pc"]:
            printmorning("*Task: Get on the pc*")
        printmorning("What would you like to do?\n1. Check cabinets\n2. Check shelf\n3. Look at the mirror\n4. Leave")
        choice = get_input("")  # Use centralized input 
        
        if choice is None:
            continue  # If inventory was opened, re-prompt

        if choice in ["1", "cabinets"]:
            if check_counter == 3:
                printmorning("Yunli: There's nothing in here, go away Michael") # Michael Chleros, when playtesting the game, opened this cabinet like 20 times, so I added this as a reference and joke
                check_counter += 1
            elif check_counter == 5:
                printmorning("*You find a statue of... wait who is this?*")
                printmorning("Yunli: How did this even get here?")
                check_counter += 1
            else: 
                printmorning("*You open the cabinets and find nothing unusual.*")
                check_counter += 1

        elif choice in ["2", "shelf"]:
            if not game_state["throw_toothpaste"]:
                print1("*You check the shelf and find old toothpaste, but nothing unusual.*")
                print1("Yunli: I should throw that out . . .")
                print1("*You throw out the toothpaste")
                game_state["throw_toothpaste"] = True
            else:
                print1("*You check the shelf and find some toothpaste and toothbrushes*")
        elif choice in ["3", "mirror"]:
            if not game_state["mirror_check"]:
                if not game_state["number"]:
                    print1("*You look at the mirror.*")
                    print1("*You see yourself*")
                    print1("Yunli: I don't know what I expected")
                    print1("*You step away from the mirror*")
                else:
                    printmorning("*You see yourself in the mirror*")
                    printmorning("*You also see a figure behind you*")
                    printmorning ("*You quickly turn around*")
                    printmorning ("*Nothing's there*")
                    printmorning ("Yunli: What the...")
                    game_state["mirror_check"]=True
            else:
                print1("*You look at the mirror.*")
                print1("*You see yourself*")
                print1("Yunli: I don't know what I expected")
                print1("*You step away from the mirror*")

        elif choice in ["4", "leave"]:
            printmorning("*You leave the bathroom...*")
            break

def upstairs_hallway():
    printmorning("*You enter the upstairs hallway...*")
    while True:
        if not game_state["morning_getting_ready"]:
            printmorning("*Task: Get ready to go out*")
        if not game_state["pc"]:
            printmorning("*Task: Get on the pc*")
        printmorning("Where would you like to go?\n1. Bathroom\n2. Your bedroom\n3. Downstairs")
        choice = get_input("")  # Use centralized input 
        
        if choice is None:
            continue  # If inventory was opened, re-prompt

        if choice in ["1", "bathroom"]:
            printmorning("*You enter your bathroom...*")
            interact_bathroom()
        elif choice in ["2", "your bedroom"]:
            printmorning("*You enter your bedroom...*")
            if not game_state["cafevisit"]:
                morning_routine()
                break
            else:
                night_time_routine()
                break
            
        elif choice in ["3", "downstairs"]:
                downstairs_hallway()
            
def downstairs_hallway():
    printmorning("*You enter the downstairs hallway...*")
    while True:
        if not game_state["morning_getting_ready"]:
            printmorning("*Task: Get ready to go out*")
        if not game_state["pc"]:
            printmorning("*Task: Get on the pc*")
        printmorning("Where would you like to go?\n1. Living room\n2. Kitchen\n3. Front yard\n4. Go upstairs")
        choice = get_input("")  # Use centralized input 
        
        if choice is None:
            continue  # If inventory was opened, re-prompt

        if choice in ["1", "living room"]:
            printmorning("*You enter the living room... *")
            Living_room()

        elif choice in ["2", "kitchen"]:
            if not game_state["true_ending"]:
                printmorning("*You enter the kitchen...*")
                kitchen_room()
                break
            else:
                printmorning("Yunli: I can't go through here")

        elif choice in ["3", "front yard"]:
            if not game_state["true_ending"]:
                printmorning("*You go through the front door*")
                front_yard() 
            else:
                printmorning("Yunli: There's no point in going out there") 
        elif choice in ["4", "upstairs"]:
            if not game_state["true_ending"]:
                upstairs_hallway()
            else:
                printmorning("Yunli: I don't think there's a reason to go upstairs")

        elif choice in ["salt"]:
            if not game_state ["salt"]:
                printmorning("Yunli: I don't have any salt, maybe I should check the kitchen..")
            elif game_state["placed_salt"]:
                printmorning("Yunli: I already placed the salt")
            elif not game_state["placed_salt"]:
                game_state["placed_salt"] = True
                print1("*Would you like to place salt down at the front door?* (yes/no)")
                choice = get_input("")
                if choice in ("yes", "Yes"):
                    printmorning("You place the salt down in front of the door")
                    remove_item(inventory, "salt")
                if choice in ("no", "No"):
                    printmorning("Yunli: Maybe this isn't the best idea...")
            
def Living_room():
    while True:
        
        if not game_state["morning_getting_ready"]:
            printmorning("*Task: Get ready to go out*")
        if not game_state["pc"]:
            printmorning("*Task: Get on the pc*")
        print1("What would you like to do? \n1. Check cabinets\n2. Backyard\n3. Check the phone\n4. Leave")
        choice = get_input("")  # Use centralized input 
        
        if choice is None:
            continue  # If inventory was opened, re-prompt

        if choice in ["1", "cabinets"]:
            if not game_state["scissors"]: 
                printmorning("*You open the cabinets and find a pair of unused scissors. Strange..*")
                print1("*Would you like to take the scissors?* (yes/no)")
                choice = get_input("")
                if choice in ["Yes", "yes"]:
                    printmorning("*You take the scissors*")
                    game_state["scissors"] = True
                    add_items(inventory, ["scissors"])
                else:
                    printmorning("*You leave the strange scissors where you found them*")
            else:
                printmorning("*You open the cabinets and find nothing unusual*")

        elif choice in ["2", "backyard"]:
            if not game_state["true_ending"]:
                printtext("*You leave the living room . . .")
                backyard_interact()
            else:
                printmorning("Yunli: I feel like I'm in the right area...")

        elif choice in ["4", "leave"]: # They are out of order because I had to rearrange them. They will be in order in the game
            if not game_state["true_ending"]:
                downstairs_hallway
                break
            else:
                printmorning("Yunli: I feel like I'm in the right area...")

        elif choice in ["3", "check the phone"]:
            phone()
            break

        elif choice in ["scissors"]:
            if game_state["scissors"]:
                if game_state["trueanswer"]:
                    print1("Would you like to stab yourself? (yes/no)")
                    choice = get_input("")
                    if choice in ["yes"]:
                        print1("Are you sure? (yes/no)")
                        choice = get_input("")
                        if choice in ["yes"]:
                            printmorning("*You promptly aim the scissors at your neck, before stabbing yourself*")
                            printmorning("*You feel the blood draining down your throat and into your lungs*")
                            printmorning("*Honestly, you can't tell if you died from blood loss or drowning first*")
                            printmorning("*There is one thing for certain though, you did die*")
                            true_ending()
                            break

                        elif choice in ["no"]:
                            printmorning("Yunli: I need to mentally prepare myself for this...") 
                    elif choice in ["no"]:
                        printmorning("Yunli: I need to mentally prepare myself for this...")



def phone(): # definetely not a koishi reference
    printmorning("*You check out the phone*")
    while True:
        if not game_state["morning_getting_ready"]:
            printmorning("*Task: Get ready to go out*")
        if not game_state["pc"]:
            printmorning("*Task: Get on the pc*")
        if not game_state["true_ending"]:
            print1("What would you like to do? \n1. Call someone\n2. Inspect\n3. Leave the phone alone")
            choice = get_input("")  # Use centralized input 
            
            if choice is None:
                continue  # If inventory was opened, re-prompt

            elif choice in ["1", "call someone"]:
                print1("Input a number")
                choice = get_input("")

                if choice in ["911"]:
                    printmorning("Yunli: I'm not calling 911")

                elif choice in ["670 999 663", "670999663"]:
                    print1("What will you say?")
                    choice = get_input("")

                    if choice in ["Hello", "hello", "hello?", "Hello?"]:
                        print1("Yunli: Hello?~")
                        print1("...")
                        print1("What would you like to say? \n1. Where is my bus?\n2. Where are you?\n3. Are you here?") # personally I would remove the options and have this be a puzzle where you had to memorize the correct responses
                        choice = get_input("")
                        if choice in ["1","Where is my bus?", "where is my bus?"]:
                            if not game_state["number"]:
                                printmorning ("You hear nothing...")
                                if not game_state["number"]:
                                    game_state["deathmark"] = True
                            else:
                                printmorning ("Take.. the third.. bus")
                                printmorning ("*beep* " * 3)
                                printmorning("*They hung up*")
                                printmorning("Yunli: ...Well that was certainly helpful") # add tone indicator lmao
                                game_state["correct_bus"] = True
                        elif choice in ["2","where are you?", "Where are you?"]:
                            printmorning("You hear nothing...")
                            if not game_state["number"]:
                                game_state["deathmark"] = True
                        elif choice in ["3","are you here?", "Are you here?"]:
                            printmorning ("Yunli: Are you here?")
                            printmorning ("'I'm at the train station...'")
                            printmorning ("*beep* " * 3)
                            printmorning("*They hung up*")
                            game_state["number"] = True
                            game_state["deathmark"] = False
                            printmorning("Yunli: ...")
                            printmorning("Yunli: What was that supposed to mean?")
                            printmorning("Yunli: I should go check out the train station")
                        else:
                            printmorning("*No response*")
                            game_state["deathmark"] = True

                    elif choice in ["pleasure to meet you invisible friend", "pleasure to meet you, invisible friend"]:
                        printmorning("Yunli: Pleasure to meet you, invisible friend!")
                        printbus("...")
                        printmorning("???: You think you can see me? It's only pretend!")
                        printmorning("Yunli: What is happening right now...")

                    else:
                        printmorning("*No response...*")
                        game_state["deathmark"] = True


                else:
                    printmorning("Yunli: I don't want to call a number I don't know...")

            elif choice in ["2", "inspect"]:
                if not game_state["3_am_sleep"]:
                    printmorning("*It's your standard house phone*")
                    printmorning("Yunli: I don't know what else I expected")
                else:
                    printmorning("Yunli: What the-")
                    printmorning("*You notice the numbers on the phone are distorted*")
                    printmorning("Yunli: Maybe I need glasses...")

            elif choice in ["3", "leave the phone alone"]:
                printmorning("*You leave the phone alone*")
                Living_room()
                break 
            elif choice in ["scissors", "Scissors"]:
                if not game_state["scissors"]:
                    printmorning("Yunli: I don't have any scissors")

                else:
                    printmorning("Yunli: I am NOT cutting the phone line!")
            elif choice in ["ribbon"]:
                if game_state["yarn_picked_up"]:
                    printmorning("Yunli: I don't have any ribbon, but maybe something similar would suffice?")
            elif choice in ["yarn"]:
                if not game_state["tied_phone"]:
                    if not game_state["yarn_picked_up"]:
                        printmorning("Yunli I don't have any yarn right now, I think I left some upstairs..")
                    else:
                        print1("Would you like to tie the yarn to the phone line? (yes/no)")
                        choice = get_input("")

                        if choice in ("yes", "Yes"):
                            printmorning("*You tie the yarn to the phone line*")
                            game_state["tied_phone"] = True
                        else:
                            printmorning("Yunli: Maybe this isn't the best idea...")
                else:
                    printmorning("Yunli: I already tied the yarn to the phone line")

            else:
                printmorning("Yunli: ...")
        else:
            print1("What would you like to do? \n1. Call someone\n2. Leave the phone alone")
            choice = get_input("")
            if choice is None:
                continue  # If inventory was opened, re-prompt

            elif choice in ["1", "call someone"]:
                print1("Input a number")
                choice = get_input("")

                if choice in ["911"]:
                    printmorning("Yunli: This is no time for jokes...")

                elif choice in ["670 999 663", "670999663"]:
                    print1("What will you say?")
                    choice = get_input("")

                    if choice in ["Hello", "hello", "hello?", "Hello?"]:
                        print1("Yunli: Hello?~")
                        printbus("...")
                        print1("What would you like to say? \n1. What should I do right now?")
                        choice = get_input("")
                        if choice in ["1", "what should i do right now"]:
                            printmorning("Yunli: What should I do right now?")
                            printbus("...")
                            printmorning("Yunli: Come on! I need your help!")
                            printbus("...")
                            printbus("...")
                            printmorning("T-Take... the scissors....///.. yourself...")
                            printmorning("Yunli: What? What does that even mean?")
                            printmorning ("*beep* " * 3)
                            printmorning("*They hung up*")
                            printmorning("Yunli: Damn it...")
                            game_state["trueanswer"] = True
                        else:
                            printmorning("Yunli: This is no time for jokes...")

            elif choice in ["2", "leave the phone alone"]:
                if not game_state["trueanswer"]:
                    printmorning("Yunli: I need to call him...")
                else:
                    printmorning("Yunli: I can only hope this is what it meant...")
                    printmorning("*You back away from the phone in preparation*")
                    Living_room()
                    break
                

            else: 
                printmorning("Yunli: I already know who to call")

def backyard_interact():
    if not game_state["3_am_sleep"]: # Day time
        printmorning("*You enter the backyard...*")
        printtext("*You see 2 cats:")
        print(r"          へ   ♡   ╱|、")
        print(r"       ૮ - ՛)     ( - 7")
        print(r"       / ⁻ ៸|     |、⁻〵")
        print(r"    乀(ˍ,ل ل      じしˍ,)ノ")
        while True:
            if not game_state["morning_getting_ready"]:
                printmorning("*Task: Get ready to go out*")
            if not game_state["pc"]:
                printmorning("*Task: Get on the pc*")

            print1 ("Where would you like to go?\n1. Go to the front yard\n2. Pet the cats \n3. Go back inside")
            choice = get_input("")  # Use centralized input 
            
            if choice is None:
                continue  # If inventory was opened, re-prompt

            if choice in ["1", "front yard"]:
                printmorning("*You enter the front yard...*")
                front_yard()
                break
            elif choice in ["2", "Pet the cats"]:
                print1("*You pet the cats. They seem happy!*")
            elif choice in ["3", "leave"]:
                Living_room()
                break
            elif choice in ["scissors"]:
                if game_state["scissors"]:
                    printmorning("Yunli: ...")
                    printmorning("Yunli: I'm not going to kill the cats...")
            elif choice in ["yarn"]:
                if game_state["yarn_picked_up"]:
                    printmorning("*You give the cats some yarn to play with*")
                    printmorning("*They seem happy!*")

    else:#Night time
        printtext("*You leave the living room . . .")
        printtext("*As you look up, you see a beautiful, bright moon. Gentle wind blows through your hair.*")
        printtext('Yunli: "What a pretty moon," she says softly.')
        # Easter egg - Random event with cat
        import random
        number = random.randint(1, 15)
        if 13 <= number <= 15:
            print(r"      |\      _,,,---,,_")
            print(r"ZZZzz /,`.-'`'    -.  ;-;;,_")
            print(r"     |,4-  ) )-,_. ,\ (  `'-'")
            print(r"    '---''(_/--'  `-'\_)")
            printtext("Yunli: Aww, the cat is sleeping.")
        elif 8 <= number <= 12:
            print(r"          へ   ♡   ╱|、")
            print(r"       ૮ - ՛)     (` -7")
            print(r"       / ⁻ ៸|     |、⁻〵")
            print(r"    乀(ˍ,ل ل      じしˍ,)ノ")
        else:
            print(r"   ╱|、")
            print(r"  (˚ˎ 。7 ")
            print(r"   |、˜〵 ")
            print(r"   じしˍ,)ノ")
        while True:
            if not game_state["morning_getting_ready"]:
                printmorning("*Task: Get ready to go out*")
            if not game_state["pc"]:
                printmorning("*Task: Get on the pc*")

            print1 ("Where would you like to go?\n1. Go to the front yard\n2. Pet the cats \n3. Go back inside")
            choice = get_input("")  # Use centralized input 
            
            if choice is None:
                continue  # If inventory was opened, re-prompt

            if choice in ["1", "front yard"]:
                printmorning("*You enter the front yard...*")
                front_yard()
                break
            elif choice in ["2", "Pet the cats"]:
                print1("*You pet the cats. They seem happy!*")
            elif choice in ["3", "leave"]:
                Living_room()
                break
            elif choice in ["scissors"]:
                printmorning("Yunli: ...")
                printmorning("Yunli: I'm not going to kill the cats...")
            elif choice in ["yarn"]:
                printmorning("*You give the cats some yarn to play with*")
                printmorning("*They seem happy!*")

def front_yard():
    if game_state["3_am_sleep"]:
            printmorning("*You see a few strange buses outside your house*") # BRO WHY ARE THERE 2 PLURAL FORMS FOR BUS AND WHY DO BOTH OF THEM HAVE PROBLEMS
            printmorning("Yunli: When did those get there...")
            printmorning("Yunli: I must've slept through it")
    while True:
        if not game_state["3_am_sleep"]: # This is for the morning
            print1 ("Where would you like to go?\n1. Backyard \n2. Front door \n3. Go to the cafe")
            choice = get_input("")  # Use centralized input 
            
            if choice is None:
                continue  # If inventory was opened, re-prompt

            if choice in ["1", "backyard"]:
                backyard_interact()  # Fixed: Add parentheses to call the function
                break

            elif choice in ["2", "front door"]:
                print1("*You go through the front door...*")
                downstairs_hallway()  # Fixed: Add parentheses to call the function
                break

            elif choice in ["3", "go to the cafe"]:
                if not game_state["morning_getting_ready"]:
                        print1("*You need to get ready before going out.*")
                elif cafe_room():
                    break

        else: 
            print1 ("Where would you like to go?\n1. Backyard \n2. Front door \n3. Take a bus")
            choice = get_input("")  # Use centralized input 
            
            if choice is None:
                continue  # If inventory was opened, re-prompt

            if choice in ["1", "backyard"]:
                backyard_interact()  # Fixed: Add parentheses to call the function
                break

            elif choice in ["2", "front door"]:
                print1("*You go through the front door...*")
                downstairs_hallway()  # Fixed: Add parentheses to call the function
                break

            elif choice in ["3", "take a bus"]: # whos this paper lily fella you speak of
                if not game_state["correct_bus"]:
                    printmorning("*You see 2 buses near your house*")
                    print1("Which bus will you take?\n1. Take the first bus\n2. Take the second bus\n3. Leave")
                    choice = get_input("")
                    if choice in ["1", "take the first bus"]:
                        printmorning("Yunli: I think I'll take the bus on the left...")
                        printmorning("*You step onto the bus, and it drives off*")
                        printbus("...") # It's just a slower typing speed
                        printbus("...")
                        printbus("...")
                        printmorning("Yunli: Mhm!") # oneshot reference you can remove that if you want
                        printbus("...")
                        printbus("...")
                        printbus("...")
                        printmorning("*After a silent ride, the bus rolls to a stop*")
                        printmorning("Yunli: Where are we?")
                        printbus("...")
                        printmorning("Yunli: No response, huh...")
                        wrong_bus()
                        break
                    elif choice in ["2", "take the second bus"]:
                        printmorning("Yunli: I think I'll take the bus on the right...")
                        printmorning("*You step onto the bus, and it drives off*")
                        printbus("...") # It's just a slower typing speed
                        printbus("...")
                        printbus("...")
                        printmorning("Yunli: Mhm!") # oneshot reference you can remove that if you want
                        printbus("...")
                        printbus("...")
                        printbus("...")
                        printmorning("*After a silent ride, the bus rolls to a stop*")
                        printmorning("Yunli: Where are we?")
                        printbus("...")
                        printmorning("Yunli: No response, huh...")
                        wrong_bus()
                        break 
                    elif choice in ["3", "leave"]:
                        printmorning("Yunli: I'm not going on one of those creepy busses..")

                        
                else:
                    printmorning("There see 2 buses near your house")
                    printmorning("*Just then, another bus rolls up, directly infront of your house*")
                    print1("Which bus will you take?\n1. Take the first bus\n2. Take the second bus\n3. Take the new third bus\n4. Leave")
                    choice = get_input("")
                    if choice in ["1", "take the first bus"]:
                        printmorning("Yunli: I think I'll take the bus on the left...")
                        printmorning("*You step onto the bus, and it drives off*")
                        printbus("...") # It's just a slower typing speed
                        printbus("...")
                        printbus("...")
                        printmorning("Yunli: Mhm!") # oneshot reference you can remove that if you want
                        printbus("...")
                        printbus("...")
                        printbus("...")
                        printmorning("*After a silent ride, the bus rolls to a stop*")
                        printmorning("Yunli: Where are we?")
                        printbus("...")
                        printmorning("Yunli: No response, huh...")
                        wrong_bus()
                        break
                    elif choice in ["2", "take the second bus"]:
                        printmorning("Yunli: I think I'll take the bus on the right...")
                        printmorning("*You step onto the bus, and it drives off*")
                        printbus("...") # It's just a slower typing speed
                        printbus("...")
                        printbus("...")
                        printmorning("Yunli: Mhm!") # oneshot reference you can remove that if you want
                        printbus("...")
                        printbus("...")
                        printbus("...")
                        printmorning("*After a silent ride, the bus rolls to a stop*")
                        printmorning("Yunli: Where are we?")
                        printbus("...")
                        printmorning("Yunli: No response, huh...")
                        wrong_bus()
                        break
                    elif choice in ["3", "take the third bus"]:
                        printmorning("Yunli: The person on the phone told me to take this bus...")
                        printmorning("*You walk over to the bus that just rolled up, and step on*")
                        printbus("...") # It's just a slower typing speed
                        printbus("...")
                        printbus("...")
                        printbus("...")
                        printbus("...")
                        printbus("...")
                        printmorning("*After a silent ride, it drops you off near an abandoned train station*")
                        printmorning("*The bus drives off*")
                        printmorning("Yunli: Well I guess I can't turn back now...")
                        train_station()
                        break
                    elif choice in ["4", "leave"]:
                        printmorning("Yunli: I'm not going on one of those creepy buses..")

def wrong_bus():
    print1("Would you like to get off the bus? (yes/no)")
    choice = get_input("")  # Use centralized input
    if choice in ["yes"]:
        printmorning("*After some consideration, you decide to get off*")
        printmorning("*As you step off, the bus drives off*")
        printmorning("*You find yourself in pitch black darkness*")
        walk_counter = 0
        look_counter = 0
        if game_state["correct_bus"]:
            printmorning("Yunli: Maybe I got on the wrong bus...")
        else:
            printmorning("Yunli: What do I do from here?")
        while True:
            printmorning("*You see a... well actually, you dont see anything*")
            print1("What would you like to do?\n1. Start walking in a direction \n2. Sit down where you are \n3. Investigate")
            choice = get_input("")  # Use centralized input 
            if choice is None:
                continue  # If inventory was opened, re-prompt
            if choice in ["1", "start walking", "start walking in a direction"]:
                if walk_counter == 0:
                    printmorning("*You start walking forwards... or whatever seems like forwards*")
                    printmorning("*Considerable time passes...*")
                    printmorning("Yunli: I've been walking for a while")
                    printmorning("Yunli: How come I haven't found anything?")
                    walk_counter += 1
                elif walk_counter == 1:
                    printmorning("*You keep walking forwards... or whatever seems like forwards*")
                    printmorning("*More time passes...*")
                    printmorning("Yunli: How much time has passed since I started...")
                    walk_counter += 1
                elif walk_counter == 2:
                    printmorning("*You continue walking forwards... or whatever seems like forwards*")
                    printmorning("*Considerable time passes...*")
                    printmorning("Yunli: I think it's been a few hours, why hasn't the sun come up?")
                    walk_counter += 1
                elif walk_counter == 3:
                    printmorning("*You keep walking forwards... or whatever seems like forwards*")
                    printmorning("*More time passes...*")
                    printmorning("*Your legs start to hurt*")
                    printmorning("Yunli: Is there no end to this? How long has it been?")
                    walk_counter += 1
                elif walk_counter == 4:
                    printmorning("*You manage to keep walking forwards*")
                    printmorning("*You can no longer tell how much time has passed*")
                    printmorning("*Your legs give out, and you collapse to the floor*")
                    printmorning("Yunli: I think I'm going to go insane...")
                    walk_counter += 1
                elif walk_counter == 5:
                    printmorning("*You can't move*")
                    printmorning("Yunli: Please.... let me out...")
                    walk_counter += 1
                elif walk_counter == 6:
                    printmorning("*You can't move*")
                    printmorning("Yunli: Let me out. Let me out. Let me out. Let me out. Let me out. Let me out. ")
                    printmorning("Let me out. Let me out. Let me out. Let me out. Let me out. Let me out. Let me out.")
                    printmorning("Let me out. Let me out. Let me out. Let me out. Let me out. Let me out. Let me out.")
                    printbus("...")
                    printbus("...")
                    printmorning("Yunli: Please....")
                    printbus("...")
                    printmorning("*Eventually, Yunli was engulfed by the darkness*") # I have no idea how to end this sequence so i just put this
                    printbus("...")
                    printmorning("Ending 2 - Engulfed by the void")
                    printmorning("That one hurt to watch...")
                    printmorning("Lets go back to the front yard, maybe don't take this bus")
                    game_state["walked"] = True
                    game_state["ending_2"] = True
                    walk_counter = 0
                    front_yard()
                    break
                
            
            elif choice in ["2", "sit", "sit down where you are"]:
                if walk_counter >= 5:
                    printmorning("*You are already lying on the ground*")
                else:
                    printmorning("*You sit down where you are and collect your thoughts*")
                    printmorning("Yunli: Wait... do I even think in the first place?")
                    printmorning("*You promptly stand back up*")
            
            elif choice in ["3", "investigate"]:
                printmorning("*You attempt to investigate the surrounding area*")
                if look_counter == 0:
                    printmorning("Yunli: I can't see anything...")
                    look_counter += 1
                elif look_counter == 1:
                    printmorning("Yunli: I still can't see anything")
                    look_counter += 1
                elif look_counter == 2:
                    printmorning("Yunli: I'm not going to keep straining my eyes like this")
            elif choice in ["scissors"]:
                if walk_counter >= 5:
                    printmorning("Yunli: ...")
                    printmorning("Yunli: Maybe I should...")
                    printmorning("Yunli: No... let's keep going")
                else:
                    printmorning("Yunli: ...I'm not that desperate")

    elif choice in ["no"]:
        printmorning("*After some consideration, you decide not to get off*")
        printmorning("*The bus starts up again*")
        printbus("...")
        printbus("..!")
        printmorning("*You notice the bus start to gradually speed up*")
        printbus("!!!")
        printmorning("Yunli: H-Hey! Slow down a bit!")
        printmorning("*The bus seems to be going at alarming speeds*")
        printmorning("Yunli: Woah! What if you cra-")
        printmorning("*Before you can finish your sentence, the bus collides with something*")
        printmorning("*Oh... and you also weren't wearing a seatbelt*")
        printmorning("*I think you can guess what happened*")
        printmorning("Ending 3 - Bus Crash")
        printmorning("I mean, there's a speed limit for a reason")
        printmorning("You might not like it, but lets go back to before the bus crashed")
        game_state["ending_3"] = True
        wrong_bus()
    else:
        wrong_bus()


def cafe_room():
    total_coffee = 0  # Total amount of coffee consumed
    game_state["cafevisit"] = True
    printmorning("*You walk into the cafe and are greeted by the overwhelming smell of coffee.*")
    printmorning("*You hear many people talking about rumors and other superstitions.*")

    while True:
        print1("What would you like to do?\n1. Sit at a table \n2. Order coffee \n3. Go home")
        choice = get_input("")  # Use centralized input 
        if choice is None:
            continue  # If inventory was opened, re-prompt

        if choice in ["1", "sit at a table"]:# word Filler
            printmorning("*You find a table and take a seat*")
            printmorning("*The entire Cafe goes silent...*")
            printmorning("Do you want of order coffee? (yes/no)")
            choice = get_input("")
            if choice in ["yes", "order coffee"]:
                printmorning("Yunli: I'd like to order a cup of coffee, please.")
                printmorning("*You start to hear Whispers of people talking about you*")
                printmorning("After a few minutes, you receive your order.")
                printmorning("*You drink the coffee*")
                printmorning("*You've had enough*")
                printmorning("*You leave the cafe*")
                front_yard()
                break 
            if choice in ["no"]:
                printmorning("You start to hear Whispers of people talking about you")
                printmorning("*You've had enough")
                printmorning("*You leave the cafe*")
                front_yard()
                break

        elif choice in ["2", "order coffee"]:
            printmorning("Yunli: I'd like to order a cup of coffee, please.")
            printmorning("After a few minutes, you receive your order.")
            printmorning("*You drink the coffee*")
            total_coffee += 1  # Increment the total coffee consumed

            if total_coffee == 3:
                printmorning("Yunli: Mr. Stark, I don't feel so good...")
                printmorning("*You collapse from caffeine overdose. Maybe don't drink so much coffee.*")
                printmorning("Ending 4 - Order Decaf Next Time")
                printmorning("*Let's start back from the front yard...*")
                game_state["ending_4"] = True
                front_yard()  # Call the next scene or function
                break
            else:
                printmorning("Yunli: Delicious!")  # Positive feedback for less than 3 cups

        elif choice in ["3", "go home"]:
            printmorning("*You leave the cafe*")
            front_yard()
            break  # Exit the loop if the user decides to go home

def kitchen_room():
    while True:
        if not game_state["morning_getting_ready"]:
            printmorning("*Task: Get ready to go out*")
        if not game_state["pc"]:
            printmorning("*Task: Get on the pc*")
        print1("What would you like to do? \n1. Check cabinets? \n2. Open the fridge? \n3. Enter the garage? \n4. Leave")
        choice = get_input("")  # Use centralized input 
        
        if choice is None:
            continue  # If inventory was opened, re-prompt

        if choice in ["1", "cabinets"]:
            if game_state["pc"] and not game_state["salt"]: #this is to make it so if you interact with the PC you can see these options
                print1("*You find salt in the cabinets.*")
                if input("Do you want to take the salt? (yes/no): ").strip().lower() == "yes":
                    game_state["salt"] = True
                    add_items(inventory, ["salt"])
                    printmorning("*You take the salt.*")
                    printmorning("*type in i to see inventory*")
                else:
                    printmorning("*You leave the salt where it is.*")
            else:
                print1("*You open the cabinets but find nothing unusual.*")
        elif choice in ["2", "fridge"]:
            printmorning("*You open the fridge and find some food, but nothing unusual.*")
        elif choice in ["3", "garage"]:
            if not game_state["3_am_sleep"]:
                garage_room()
                break
            elif game_state["fight_win"]:
                garage_room()
                break
            else:
                night_garage()
                break

        elif choice in ["4", "leave"]:
            downstairs_hallway()
            
def garage_room():
    printmorning("*You enter the garage...*")
    while True:  # Garage loop
        if not game_state["morning_getting_ready"]:
            printmorning("*Task: Get ready to go out*")
        if not game_state["pc"]:
            printmorning("*Task: Get on the pc*")
        print1("What would you like to do?\n1. Check cabinets\n2. Check the shelf\n3. Leave")
        choice = get_input("")  # Use centralized input
        
        if choice is None:
            continue  # If inventory was opened, re-prompt

        if choice in ["1", "cabinets"]:
            print1("*You open the cabinets and find nothing unusual.*")
        elif choice in ["2", "shelf"]:
            if game_state["pc"] and not game_state["paint_and_brushes"]: #this is to make it so if if you interact with the PC you can see these options
                print1("*You check the shelf and find red paint and brushes.*")
                if input("Do you want to take the paint and brushes? (yes/no): ").strip().lower() == "yes":
                    game_state["paint_and_brushes"] = True
                    add_items(inventory, ["paint", "brushes"])                    
                    printmorning("*You take the paint and brushes.*")
                    printmorning("*Type in i to see inventory*")
                else:
                    printmorning("*You leave the paint and brushes.*")
            else:
                print1("*You check the shelf but find nothing unusual.*")

        elif choice in ["paint"]:
            # Ensure the player has the paint and brushes before painting
            if "paint" in inventory and "brushes" in inventory:
                if not game_state["symbol"]:
                    printmorning("Yunli: I think I need to paint something here.")
                    if input("Do you want to paint the symbol? (yes/no): ").strip().lower() == "yes":
                        printmorning("*You paint the symbol on the ground.*")
                        game_state["symbol"] = True
                        game_state["deathmark2"] = True
                        remove_item(inventory, "paint") 
                        remove_item(inventory, "brushes")
                        printmorning("*You used the paint and brushes*")
                else:
                    printmorning("*The symbol has already been painted.*")
            else:
                print1("Yunli: I think I need some paint.. and a brush.")
            
        elif choice in ["ribbon"]:
            if game_state["yarn_picked_up"]:
                printmorning("Yunli: I don't have ribbons, but maybe something similar would suffice?")
        elif choice in ["yarn"]:
                if not game_state["tied_yarn"]:
                    if game_state["yarn_picked_up"]:
                        if not game_state["symbol"]:
                            printmorning("Yunli: Maybe I should draw the symbol first...")
                        else:
                            print1("*Tie the yarn to the ends of the symbol?* (yes/no)")
                            choice = get_input("")  # Use centralized input
                            if choice in ("yes"):
                                printmorning("*You tie some yarn according to the instructions*")
                                game_state["tied_yarn"] = True
                                game_state["deathmark2"] = False
                            else:
                                printmorning("Yunli: Maybe this isn't the best idea...")
                    else:
                        printmorning("Yunli: I think I left some yarn upstairs..")
                else:
                    printmorning("Yunli: I already tied the yarn to the symbol")
                
        
        elif choice in ["3", "leave"]:
            kitchen_room()
            break
    
def night_garage():
    printmorning("*You enter the garage...*")
    while True:  # Garage loop
        if not game_state["morning_getting_ready"]:
            printmorning("*Task: Get ready to go out*")
        if not game_state["pc"]:
            printmorning("*Task: Get on the pc*")
        print1("What would you like to do?\n1. Check cabinets\n2. Check the shelf\n3. Start the ritual\n4. Leave")
        choice = get_input("")  # Use centralized input
        
        if choice is None:
            continue  # If inventory was opened, re-prompt

        if choice in ["1", "cabinets"]:
            print1("*You open the cabinets and find nothing unusual.*")
        elif choice in ["2", "shelf"]:
            if game_state["pc"] and not game_state["paint_and_brushes"]: #this is to make it so if if you interact with the PC you can see these options
                print1("*You check the shelf and find red paint and brushes.*") # I kinda trolled by making it so the pc locks the first room oops
                if input("Do you want to take the paint and brushes? (yes/no): ").strip().lower() == "yes":
                    game_state["paint_and_brushes"] = True
                    add_items(inventory, ["paint", "brushes"])                    
                    printmorning("*You take the paint and brushes.*")
                    printmorning("*type in i to see inventory*")
                else:
                    printmorning("*You leave the paint and brushes.*")
            else:
                print1("*You check the shelf but find nothing unusual.*")

        elif choice in ["paint"]:
            # Ensure the player has the paint and brushes before painting
            if "paint" in inventory and "brushes" in inventory:
                if not game_state["symbol"]:
                    printmorning("Yunli: I think I need to paint something here.")
                    if input("Do you want to paint the symbol? (yes/no): ").strip().lower() == "yes":
                        printmorning("*You paint the symbol on the ground.*")
                        game_state["symbol"] = True
                        game_state["deathmark2"] = True
                        remove_item(inventory, "paint") 
                        remove_item(inventory, "brushes")
                        printmorning("*You used the paint and brushes*")
                else:
                    printmorning("*The symbol has already been painted.*")
            else:
                print1("Yunli: I think I need some paint.. and a brush.")
            
        elif choice in ["ribbon"]:
            if game_state["yarn_picked_up"]:
                printmorning("Yunli: I don't have ribbons, but maybe something similar would suffice?")
        elif choice in ["yarn"]:
                if not game_state["tied_yarn"]:
                    if game_state["yarn_picked_up"]:
                        if not game_state["symbol"]:
                            printmorning("Yunli: Maybe I should draw the symbol first...")
                        else:
                            print1("*Tie the yarn to the ends of the symbol?* (yes/no)")
                            choice = get_input("")  # Use centralized input
                            if choice in ("yes"):
                                printmorning("*You tie some yarn according to the instructions*")
                                game_state["tied_yarn"] = True
                                game_state["deathmark2"] = False
                            else:
                                printmorning("Yunli: Maybe this isn't the best idea...")
                    else:
                        printmorning("Yunli: I think I left some yarn upstairs..")
                else:
                    printmorning("Yunli: I already tied the yarn to the symbol")
            
        elif choice in ["3", "start the ritual"]:
            if game_state["tied_yarn"]: # It is impossible to tie the yarn to the symbol without drawing it first
                if game_state["tied_phone"]:
                    if game_state["number"]:
                        if game_state["placed_salt"]: #Add another game state for a way to start the ritual
                            printmorning("*You start the ritual, following all the instructions given*")
                            printmorning("*As the paint begins to glow, you see something emerge from the circle*")
                            printmorning("Yunli: Wh-What the hell is that?!") # I literally have no idea what to put here
                            printmorning("*You watch as the yarn entangles the summoned creature, binding it*") # Plot armor
                            printmorning("*something something monster noises go brrrrr*")
                            printmorning("Yunli: I have to do something about that!")
                            print1("What would you like to do?\n1. Fight\n2. Run") # Don't ask..
                            choice = get_input("")
                            if choice is None:
                                continue  # If inventory was opened, re-prompt

                            if choice in ("1", "fight"):
                                fight_sequence()
                                break
                            elif choice in ("2", "run"):
                                printmorning("Yunli: I can't deal with that thing!")
                                printmorning("*As you turn to leave the room, you hear a faint click near the door*")
                                print1("What would you like to do\n1. Leave through the kitchen door\n2. Leave through the garage door")
                                choice = get_input("")
                                if choice in ("1", "leave through the kitchen door"):
                                    printmorning("*You try to turn the door handle*")
                                    printmorning("Yunli: It's locked")
                                    printmorning("*As you turn to leave through the garage door, you notice the monster is no longer bound*")
                                    print1(". . .")
                                    print1("*You feel a sharp pain within your body...*")
                                    print1("*As you close your eyes, the blood slowly leaves your body...*")
                                    print1("*You bleed out.*")
                                    print1("Ending 5 - Attempted Escape")
                                    game_state["ending_5"] = True
                                    printmorning("Oh come on, you heard the door lock too!")
                                    printmorning("Tsk.. Try again")
                                    
                                if choice in ("2", "leave through the garage door"):
                                    printmorning("*You swiftly open the garage door and start running*")
                                    printmorning("*You make it a few blocks over before your legs give out*")
                                    printmorning("Yunli: *huff* I think this is far enough *huff*")
                                    printmorning("*As you lift your head to scan the surroundings, a familiar sight greets you*")
                                    print1(". . .")
                                    print1("*You feel a sharp pain within your body...*")
                                    print1("*As you close your eyes, the blood slowly leaves your body...*")
                                    print1("*You bleed out.*")
                                    print1("Ending 5 - Attempted Escape")
                                    game_state["ending_5"] = True
                                    printmorning("Well that was just unfortunate")
                                    printmorning("Try again")
                                    

                        else:
                            printmorning("Yunli: I think I missed a step")
                    else:
                        printmorning("Yunli: I think I missed a step")
                else:
                    printmorning("Yunli: I think I missed a step")
            else:
                printmorning("Yunli: I think I missed a step")
            

        elif choice in ["4", "leave"]:
            kitchen_room()
            break

def fight_sequence():
    total_hp_monster = 4
    total_hp_yunli = 2
    while True:
        print1("What would you like to do?\n1. Hit it\n2. Attempt conversation\n3. Run")
        choice = get_input("")  # Use centralized input

        if choice is None:
            continue  # If inventory was opened, re-prompt
        
        elif choice in ("1", "hit it"):
            printmorning("*You grab a nearby object and strike the creature*")
            total_hp_monster -= 1
            if total_hp_monster == 0:
                printmorning("*insert funny monster noises here*") # lol
                printmorning("*The monster stops trying to break free from its restraints*")
                printmorning("Yunli: Is it dead?")
                printmorning("*It is dead*")
                filler_win()
                break

            elif total_hp_monster == -1:
                printmorning("*insert funny monster noises here*") # lol
                printmorning("*The monster stops trying to break free from its restraints*")
                printmorning("Yunli: Is it dead?")
                printmorning("*It is dead*")
                filler_win()
                break
                
            bnumber = random.randrange(1, 4)
            if bnumber == 1:
                printmorning("*The creature retaliates through the bindings*")
                printmorning("*It hits one of your arms*")
                total_hp_yunli -= 1
                if total_hp_yunli == 0:
                    printmorning("*Your vision goes blurry, and you collapse*")
                    printmorning("Ending 6 - Attemped 1v1")
                    game_state["ending_6"] = True
                    printmorning("It's a scripted win! You still have a weapon after all")
                    printmorning("Try to fight it again...")
                    total_hp_yunli = 2
                    total_hp_monster = 4
                else:
                    printmorning("Yunli: Ow!")
            else:
                printmorning("*The creature retaliates through the bindings*")
                printmorning("*It grazes you*")
                printmorning("Yunli: That was close!")

        elif choice in ("2", "Attempt conversation"):
            printmorning("*You try to talk to it*")
            printmorning("Yunli: Uh, do you mind not trying to kill me?") # Dont ask pt 2
            anumber = random.randrange(1, 3)
            if anumber == 1:
                printmorning("*La creatura decides not to attack you*")
                printmorning("Yunli: Thanks!") #this literally does nothing
            else:
                printmorning("*The creature retaliates through the bindings*")
                printmorning("*It hits one of your arms*")
                total_hp_yunli -= 1
                if total_hp_yunli == 0:
                    printmorning("*Your vision goes blurry, and you collapse*")
                    printmorning("Ending 6 - Attemped 1v1")
                    game_state["ending_6"] = True
                    printmorning("It's a scripted win! You still have a weapon after all")
                    total_hp_yunli = 2
                    total_hp_monster = 4
                else:
                    printmorning("Yunli: Ow!")

        elif choice in ("3", "run"):
            printmorning("*You swiftly open the garage door and start running*")
            printmorning("*You make it a few blocks over before your legs give out*")
            printmorning("Yunli: *huff* I think this is far enough *huff*")
            printmorning("*As you lift your head to scan the surroundings, a familiar sight greets you*")
            print1(". . .")
            print1("*You feel a sharp pain within your body...*")
            print1("*As you close your eyes, the blood slowly leaves your body...*")
            print1("*You bleed out.*")
            print1("Ending 5 - Attempted Escape")
            game_state["ending_5"] = True
            printmorning("Well that was just unfortunate")
            printmorning("Try again")
            total_hp_yunli = 2
            total_hp_monster = 4

        elif choice in ("scissors"):
            if game_state["scissors"]:
                printmorning("*You pull out the strange pair of scissors and strike the creature*")
                printmorning("*insert pained monster sounds here*")
                printmorning("Yunli: Looks like that had some effect...")
                total_hp_monster -= 2
                if total_hp_monster == 0:
                    printmorning("*insert funny monster noises here*") # lol
                    printmorning("*The monster stops trying to break free from its restraints*")
                    printmorning("Yunli: Is it dead?")
                    printmorning("*It is dead*")
                    filler_win()
                    break
                elif total_hp_monster == -1:
                    printmorning("*insert funny monster noises here*") # lol
                    printmorning("*The monster stops trying to break free from its restraints*")
                    printmorning("Yunli: Is it dead?")
                    printmorning("*It is dead*")
                    filler_win()
                    break

def filler_win():
        printmorning("*You manage to pull through and kill the creature you summoned*")
        printmorning("*You watch as its corpse receeds into the circle, until it eventually dissapears*")
        printmorning("*You don't really care though, you're just happy it's gone...*")
        printmorning("Yunli: I'll clean all of this up tomorrow...") # Professional procrastinator
        printmorning("*Congratulations for surviving your first night, well, the night isn't over*")
        printmorning("*On the circle, you find a note that wasn't there before*")
        printmorning("It reads 'Come visit me at the train station!'")
        printmorning("'If you don't know how to get there, just take the bus, and if you can't find it, just ask!'")
        printmorning("Yunli: The train station? I guess I was planning on going there eventually")
        printmorning("Yunli: But where is the bus to get there? What does it mean 'just ask'?")
        printmorning("*As you set the note down, it promptly burns to a crisp*")
        printmorning("Yunli: Ah! Well, there goes my only hint...")
        printmorning("Ending 7 - You survived (You should keep going though)")
        game_state["ending_7"] = True
        game_state["fight_win"] = True
        garage_room()


def train_station():
    printmorning("*You see a nearby building*")
    while True:
        print1("Where would you like to go?\n1. The nearby building\n2. The train tracks") # DONT ADD A LEAVE OPTION HERE
        choice = get_input("")  # Use centralized input

        
        if choice is None:
            continue  # If inventory was opened, re-prompt
        if choice in ["1", "the nearby building"]:
            printmorning("*You enter the building*")
            unknown_building()
        elif choice in ["2", "the train tracks"]:
            printmorning("*You drop down onto the train tracks")
            train_tracks()
            break

def train_tracks():
    while True:
        print1("Where would you like to go?\n1. Head into the tunnel\n2. Leave") # Despite the fact that Yunli probably can't climb up, she needs to be able to find the notes if she dropped down first.
        choice = get_input("")  # Use centralized input

        if choice is None: #wip
            continue  # If inventory was opened, re-prompt
        if choice in["1","head into the tunnel"]:
            print1("*You walk into the tunnel...*")
            print1("*You find a sign*")
            tunnel_system()
            break

        elif choice in ["2", "leave"]:
            printmorning("*You climb back up and off the tracks*")
            train_station()
            break

def tunnel_system(): #This is to implement the looping system without constantly loading the other messages
    loop_counter = 0
    while True:
        print1("It says")
        print1("'For every set of numbers you have, the first one corresponds to the set of tunnels, and the second to the tunnel itself'")
        if loop_counter == 2:
            printmorning("Yunli: Do I just have to try every tunnel? Or is there something I missed...")
        elif loop_counter ==1:
            printmorning("Yunli: I'm back here again...")
        elif loop_counter >=3:
            printmorning("Yunli: This is starting to get on my nerves...")
        else:
            printmorning("Yunli: What does that even mean..?")
            if game_state["note 1"] or game_state["note 2"] or game_state["note 3"]:
                printmorning("Yunli: Maybe it has to do with that note!")
        print1("Which tunnel would you like to go through\n1. Tunnel 1\n2. Tunnel 2\n3. Tunnel 3\n4. Leave") # Set 1
        choice = get_input("")
        if choice is None:
            continue  # If inventory was opened, re-prompt
        
        if choice in ["1", "tunnel 1"]:
            printmorning("*You walk through the first tunnel for a while*")
            printmorning("*You are greeted by a familiar sign*")
            loop_counter += 1
        elif choice in ["4", "leave"]:
            printmorning("*You walk out of the tunnel*")
            train_tracks()
            break
        elif choice in ["2", "tunnel 2"]:
            printmorning("*You walk through the second tunnel for a while*")
            printmorning("*You are greeted by a familiar sign*")
            loop_counter += 1
        elif choice in ["3", "tunnel 3"]:
            printmorning("*You walk through the third tunnel for a while*")
            printmorning("You are greeted by another set of tunnels")
            print1("Which tunnel would you like to go through\n1. Tunnel 1\n2. Tunnel 2\n3. Tunnel 3") # Set 2
            choice = get_input("")
            if choice in ["1", "tunnel 1"]:
                printmorning("*You walk through the first tunnel for a while*")
                printmorning("*You are greeted by a familiar sign*")
                loop_counter += 1
            elif choice in ["2", "tunnel 2"]:
                printmorning("*You walk through the second tunnel for a while*")
                printmorning("*You are greeted by a familiar sign*")
                loop_counter += 1
            elif choice in ["3", "tunnel 3"]:
                printmorning("*You walk through the third tunnel for a while*")
                printmorning("You are greeted by another set of tunnels")
                print1("Which tunnel would you like to go through\n1. Tunnel 1\n2. Tunnel 2\n3. Tunnel 3") # Set 3
                choice = get_input("")
                if choice in ["1", "tunnel 1"]:
                    printmorning("*You walk through the first tunnel for a while*")
                    printmorning("*You are greeted by a familiar sign*")
                    loop_counter += 1
                elif choice in ["3", "tunnel 3"]:
                    printmorning("*You walk through the third tunnel for a while*")
                    printmorning("*You are greeted by a familiar sign*")
                    loop_counter += 1
                elif choice in ["2", "tunnel 2"]:
                    printmorning("*You walk through the second tunnel for a while*")
                    printmorning("*You see a bright light, as your eyes adjust to the light*")
                    printmorning("Yunli: Finally! I made it out!")
                    printmorning ("*You walk through the tunnel to see a forest*")
                    printmorning("*As you walk, you start to realize the path behind you is closing*")
                    printmorning("Yunli: Wh-What the hell!") # pikachu shock 
                    printmorning("*You start running to the opening*")
                    printmorning("*You barely made it*")
                    printmorning("Yunli: I hope I never have to do that again")
                    printmorning("*You take a very long breather*")
                    printtext("*As you look up, you see a beautiful soft blue night sky, with soft lit lanterns illuminating the nearby trees*")
                    printtext('Yunli: "What a beautiful place" As her eyes reflect the soft light from the lanterns') # dies of forest fire
                    unknown_forest() #lol
                    break

def unknown_forest(): #still night btw
    while True:#main gate is locked and you need 3 keys
        print1("Where would you like to go?\n1. Pond\n2. Main gate \n3. Camp site\n4. Lake\n5. Old shrine")
        choice = get_input("")  # Use centralized input\
        if choice is None:
            continue  # If inventory was opened, re-prompt
        
        if choice in ["1", "pond"]: # lemme do the pond
            printmorning("*You come across a small pond*")
            printmorning("*As you get closer. you notice a small fish swimming in the pond*")
            print1("What would you like to do?\n1. Observe the fish\n2. Kill the fish\n3. Leave the fish alone")
            choice = get_input("")
            if choice is None:
                continue  # If inventory was opened, re-prompt
            if choice in ["1", "observe the fish"]:
                if not game_state["fish_dead"]:
                    printmorning("*You watch the fish swim happily in its pond*")
                    printmorning("Yunli: How nice...")

            elif choice in ["2", "kill the fish", "kill"]:
                if not game_state["fish_dead"]:
                    printmorning("Yunli: Sorry, but I need that key...")
                    printmorning("*You pull out your scissors, and attempt to stab the fish*")
                    fnumber = random.randrange(1,5)
                    if fnumber == 1:
                        printmorning("*You miss the fish, but it doesn't flee*")
                    else:
                        printmorning("*You manage to stab the fish, and it flops around before going limp*")
                        printmorning("*You see the pond and sky slowly turn red*")
                        printmorning("*You don't find a key anywhere in the pond*")
                        printmorning("Yunli: All that for nothing...")
                        printmorning("*The forest starts to shake violently")
                        game_state["fish_dead"] = True
                        printmorning("Yunli: That doesn't look very good")
                        printmorning("*The floor underneath you starts to open up*")
                        printmorning("Yunli: !!!")
                        printmorning("*You fall in and black out*")
                        printmorning("*You wake up inside the pond*")
                        printmorning("Yunli: blub blub blub?")
                        printmorning("Ending 8 - MAN WHAT DID THE FISH DO, MY BOI WAS CHILLIN AN-")
                        game_state["ending_8"] = True
                        print1("Maybe lets not kill the fish next time")
                else:
                    printmorning("Yunli: I don't feel so good about that fish")
                    printmorning("*You spare the fish... this time*")

            elif choice in ["3", "leave the fish alone"]:
                printmorning("*You decide to leave the fish alone*")
                printmorning("*The fish waves thanks*")
                printmorning("Yunli: You're welcom- wait did a fish just thank me?")
                printmorning("Yunli: Well that's the least of my worries for now")

        elif choice in["2", "main gate"]:
            printmorning ("*You see a massive gate*")
            printmorning ("*It seems like you need 3 keys to unlock it*") 
            print1("Do you want to unlock the main gate? (yes/no):")
            choice = get_input("")
            if choice in ["yes", "y"]:
                if game_state["key_1"] and game_state["key_2"] and game_state["key_3"]:
                    printmorning("Yunli: Finally, I found all the keys!")
                    printmorning("*You unlock the door*")
                    printmorning("Yunli: Let's get out of this forest")
                    printmorning("*As you're walking out of the forest, creatures with purple and white robes step out from the shadows*")
                    printmorning("*You feel a sharp pain in the back of your head*")
                    printmorning("*You fall unconscious, and wake up in a prison cell*")
                    printmorning("You just can't catch a break, can you...")
                    printmorning("Yunli: Where am I...")
                    printmorning("*You realize that your cell door is unlocked*")
                    printmorning("Or maybe you can... How 'lucky'...")
                    prison_cell()
                    break

                else:
                    printmorning("Yunli: I can't unlock this without the keys")
            elif choice in ["no", "n"]:
                    if game_state ["key_1"] and ["key_2"] and ["key_3"]:
                        printmorning("*You decide not to unlock the main gate*")
                    else:
                        printmorning("Yunli: I can't unlock this without the keys")

        elif choice in["3", "camp site"]:
            printmorning("*You find a camp fire that's unattended*")
            camp_site()
            break
        elif choice in["4", "lake"]: #wip
            printmorning("*You see a small opening within the forest*")
            printmorning("*You walk through the opening to find a lake*")
            lake()
            break
        elif choice in["5", "old shrine"]:
            printmorning ("*You come across an old shrine")
            printmorning ("*You walk underneath the torii...*") #torii are those big red gates right? yes
            old_shrine()
            break
        
    
def prison_cell():#chat let him cook
    while True:
        printmorning("What would you like to do?\n1. Check Lockers\n2. Check cells\n3. Leave the room")
        choice = get_input("")  # Use centralized input 
        if choice in ["1", "Check Lockers"]:
            if not game_state["more keys"]:
                printmorning("*You open the locker and you find a coat and a key*")
                ready_choice = input("Do you want to take some of them? (yes/no): ").strip().lower()
                if ready_choice == "yes":
                    game_state["more keys"] = True
                    add_items(inventory, ["door key"])
                    printmorning("*You pick up the door key and add it to your inventory.*")
                    printmorning("*Type in 'i' to see inventory*")
                else:
                    print1("*You decide to leave the key*")
            else:
                printmorning("*You open the locker and you find a coat*")
                printmorning("*You close the locker*")
        elif choice in ["2", "Check cells"]:
            printmorning("*You check the cells and find nothing unusual.*")
        elif choice in ["3", "Leave the room"]:
            if not game_state["more keys"]:
                printmorning("*You notice that the door is locked*")
                printmorning("Yunli: I need to find a key")
            else:
                printmorning("*You unlock the door*")
                printmorning("*As you are about to open the door you hear*")
                printmorning("*Footsteps*")
                printbus("...")
                printmorning("*You see two entities with a white hoodie*")
                printmorning("Unknown: Subject 265 has died")
                printmorning("Unknown: He couldn’t survive the mutation pills? Another failed experiment...")
                printmorning("Unknown: The boss won't be too pleased")
                printbus("...")
                printmorning("Yunli: I need to get out of here quickly")
                printmorning("*You slowly creak open the door...*")
                printmorning("*You see a room made with black bricks, and blue lights are strewn about*")
                printmorning("*You watch them leave the room*")
                hallway()
                break
            
def hallway():
    printmorning("*You enter the hallway...*")
    while True:
        printmorning("Where would you like to go?\n1. Locked gate\n2. Operating room")
        choice = get_input("")  # Use centralized input 
        
        if choice is None:
            continue  # If inventory was opened, re-prompt

        if choice in ["1", "locked gate"]:
            if not game_state["getmeout keys"]: # Free my boy its like an hour before deadline
                printmorning("*You walk towards the gate...*")
                printmorning("*You stand before the locked gate. It's rusted bars visible in the dim light.*")
                printmorning("*You realize that behind this door, there's a gate to leave*")
                printmorning("Yunli: I need a key, and fast")
            elif game_state["getmeout keys"]:
                print1("Are you sure you want to go through this gate? If you do, you cannot come back... (yes/no)")
                choice = get_input("")
                if choice in ["yes"]:
                    printmorning("*You open the door to see in the distance a with a soft white light*")
                    printmorning("*With no other option, you decide to step through*")
                    printmorning("*You find a familiar looking door covered in blue and red flowers*")
                    printmorning("*You find yourself hesitating wondering if this best idea*")
                    printmorning("*With nowhere else to go you decide to push through*")
                    printmorning("*As you open the door you get blinded soft white lights*")
                    printmorning("*Flower petals start to fly around the air, as winds blow through your hair*")
                    printmorning("*Strangely, you find yourself back to a familiar place*")
                    printmorning("Yunli: Where am I? Actually, I think I've asked that question too much...")
                    printmorning("Yunli: It... seems like home..")
                    printmorning("*You find yourself staring back at your front door*")
                    if game_state["ending_1"] and game_state["ending_2"] and game_state["ending_3"] and game_state["ending_4"] and game_state["ending_5"] and game_state["ending_6"] and game_state["ending_7"] and game_state["ending_8"] and game_state["ending_9"]:
                        printmorning("Yunli: No, something isn't right")
                        printmorning("Yunli: How did I get here?")
                        printmorning("Yunli: There must be a way out")
                        printmorning("*You walk into your house*")
                        game_state["true_ending"] = True
                        downstairs_hallway()
                        break

                    else:
                        printmorning("Yunli: Was it a dream? Well, it doesn't matter to me")
                        printmorning("*And with that, Yunli lived happily ever after, or so we think...*")
                        printmorning("Ending 10 - False End")
                        printmorning("Yes, thats right, 'False' end")
                        printmorning("If you really want the true ending, just simply die!")
                        printmorning("No, I mean seriously...")
                        printmorning("Or you can just read the code of the game, which I assume most of you will do")
                        printmorning("How boring...")
                        end()
                        break

                if choice in ["no"]:
                    printmorning("Yunli: I have more things to do before I leave")

        elif choice in ["2", "Operating room"]:
            printmorning("*You slowly approached the operating room...*")
            printmorning("*You open the door as you see a bunch of bodies on a counter*")
            Operating_room()
            break

def Operating_room():
    while True:
        printmorning("What would you like to do?\n1. Examine the bodies\n2. Shelves\n3. Leave")
        choice = get_input("")  # Use centralized input 
        
        if choice is None:
            continue  # If inventory was opened, re-prompt
        if choice in ["1","examine the bodies"]:
            printmorning("*You check all the putrid bodies*")
            printmorning("Yunli: Why do I do this to mysel- Oh!")
            printmorning("*You you find a shiny green object*")
            ready_choice = input("Do you want to take the shiny green object? (yes/no): ").strip().lower()
            if ready_choice == "yes":
                if not game_state["getmeout keys"]:
                    printmorning("*You take the keys from the body*")
                    printmorning("Yunli: Let's get the hell out of here")
                    game_state["getmeout keys"] = True
                    add_items(inventory, ["Jade keys"])
                else:
                    printmorning("Yunli: I already have the keys. I'm getting out of here")
                        
            elif ready_choice == "no":
                printmorning("*You step away from the body...*")
            else:
                printmorning("Yunli: I am not checking those bodies again")
        elif choice in ["2","shelves"]:
            printmorning("*You open the cabinets and find jars of black liquid.*")
            printmorning("Yunli: What is this?! Actually, do I even want to know?")
        elif choice in ["3","leave"]:
            hallway()
            break
            
def true_ending():
    printmorning("*You wake up grasping your neck, the pain no longer there*")
    printmorning("Yunli: Oh thank god it worke-")
    printmorning("*You abruptly stop your sentence when you hear footsteps coming towards you*")
    printmorning("*Scanning the area, you realize you're in a body bag, and near a gate seemingly leading outside*")
    printmorning("*You also feel a throbbing pain in your head, but the adrenaline nulls it a bit*")
    while True:
        printmorning("Yunli: What should I do... \n1. Hide \n2. Run")
        choice = get_input("")
        if choice in ["1", "Hide"]:
            printmorning("*You lie back down and pretend to be dead*")
            printmorning("*You hear multiple people enter the room*")
            printmorning("Unknown: Where'd you find this one?")
            printmorning("Unknown: She was trying to leave through the gate, I just happened to find her")
            printmorning("Unknown: Did you have to kill her though? Couldn't you just knock her out?")
            printmorning("Unknown: I didn't mean to! I just hit her a bit to hard because she startled me, I mean she should've been in her cell..")
            printmorning("Unknown: The boss wont be too happy with this, just toss her")
            printmorning("Unknown: On it!")
            printmorning("*They walk over to your body bag and zip it up, then promptly carry it through the front gate*")
            printmorning("*You hold your breath*")
            printbus("...")
            printbus("...")
            printbus("...")
            printmorning("*thud*")
            printmorning("*They drop your body bag, although it felt like a longer drop than you'd think*")
            printmorning("Unknown: Alright, now start pouring the cement")
            printmorning("Yunli: The WHAT")
            printmorning("*You struggle to get out of the body bag, but to no avail*")
            printmorning("*Eventually, a dense liquid is poured over you, wherever you are*")
            printmorning("*Although you tried your best, you suffocate in the bag buried in concrete*")
            printmorning("So close! I know running has never been the right answer, but theres a first for everything!")
        if choice in ["2", "Run"]:
            printmorning("*You wriggle your way out of the open body bag and reach for the front gate*")
            printmorning("*You turn the handle, and it seems to be unlocked!*")
            printmorning("Yunli: Oh thank god!")
            printmorning("*You start running as fast as you can, to any civilized area you can find, disregarding whatever is happening behind you*")
            printmorning("=======3 MONTHS LATER=======")
            printmorning("*yawns* *Press enter to continue*")
            input()
            printmorning("*You stretch and feel the warmth of the sun streaming through the window.*")
            printmorning("*As the smell of fresh coffee fills the air.*")
            printmorning("Yunli: I should get ready.")
            printmorning("Yunli: Oh, the newspaper is here")
            printmorning("Yunli: Who even reads this stuff, we have phones for a reason")
            printmorning("*You see an article about some cultists being arrested and interrogated on your front page*")
            printmorning("Yunli: Heh, at least almost dying wasn't for nothing!")
            printbus("...")
            printbus("...")
            printbus("...")
            printmorning("Yunli: Ok maybe it wasn't that worth it...")
            end()
            break
            

            
def old_shrine():
    while True:
        print1("Where you like to go?\n1. Shinsen\n2. Main shrine \n3. Leave")
        choice = get_input("")  # Use centralized input 

        if choice is None:
            continue  # If inventory was opened, re-prompt
        if choice in ["1", "shinsen"]:
            shinsen()
            break
        elif choice in ["2", "main shrine"]:
            printmorning("*You walk towards the main shrine...*")           
            main_shrine()
            break
        elif choice in ["3", "leave"]:
            printmorning ("*You leave the old shrine")
            unknown_forest()
            break
            
def main_shrine():
    while True:
        print1("What would you like to do?\n1. Investigate\n2. Leave")
        choice = get_input("")  # Use centralized input 
        if choice is None:
            continue  # If inventory was opened, re-prompt
        if choice in ["1", "investigate"]:
            if not game_state["offerings"]:
                printmorning("*You find a nearby table covered in miscellaneous foods and alcohols*")
                ready_choice = input("Do you want to take some of them? (yes/no): ").strip().lower() # my fault
                if ready_choice == "yes":
                    if not game_state["Blessing_Book"]:
                        printmorning("*You take the items from the table*")
                        printmorning("Yunli: What would I need food and sake for?")
                        game_state["offerings"] = True
                        add_items(inventory, ["food and sake"])
                    else:
                        printmorning("*You take the items from the table*")
                        printmorning("Yunli: Maybe I can use these as offerings...")
                        game_state["offerings"] = True
                        add_items(inventory, ["food and sake"])
                        
                elif ready_choice == "no":
                    printmorning("*You step away from the offering...*")
            else:
                printmorning("*You find a saisen box but nothing out of the ordinary*")
        elif choice in ["2", "leave"]:
            printmorning("*You leave the main shrine*")
            old_shrine()
            break

def shinsen():
    printmorning("*You walk to the Shinsen*")
    printmorning("*You find statue with moss growing on the side*")
    printmorning("*Infont of the statue, you see a plate illuminated by the warm lights from nearby lanterns...")
    printmorning("*You find a book...*")
    printmorning("It reads 'Tsukuyomi'...")
    printmorning("'Once every blue moon you get a chance to get a blessing from the God named Tsukuyomi'")
    printmorning("'To recieve this blessing you must offer either food or sake'")
    printmorning("Yunli: Maybe I can use this chance to get out of this place!")
    printmorning("*You pick up the Book")
    add_items(inventory, ["Blessing Book"])
    game_state["Blessing_Book"] = True
    print1("*Type Book to re-read the Blessing Book*")
    while True:
        print1("What would you like to do\n1. Give offerings\n2. Leave")
        choice = get_input("")  # Use centralized input 

        if choice is None:
            continue
        if choice in ["1", "Give offerings"]:
            ready_choice = input("Do you want to offer to the shrine? (yes/no): ").strip().lower()
            if not game_state["offerings"]:
                if ready_choice == "yes":
                        printmorning("*You check your pockets and find nothing*")
                        printmorning("Yunli: I need to find some food and sake")
                        
                elif ready_choice == "no":
                    printmorning("*You step away from the offering plate...*")
            else:
                if ready_choice == "yes":
                    printmorning("You give your offerings.")
                    printmorning("*You notice the offerings disappear, and you find a key*")
                    printmorning("*Key 1 has been added to your inventory*")
                    printmorning("Yunli: I'm not even suprised anymore...")
                    add_items(inventory,["key 1"])
                    remove_item(inventory,"food and sake")
                    game_state ["key_1"] = True
                elif ready_choice == "no":
                    printmorning("*You step away from the offering plate...*")
        elif choice in ["2", "leave"]:
            printmorning ("*You leave the shinsen...*")
            old_shrine()
            break

def camp_site():
    while True:
        print1("What would you like to do?\n1. Sit by the camp fire\n2. Sit on the bench \n3. Shop\n4. Leave")
        choice = get_input("")  # Use centralized input 
        if choice is None:
            continue
        
        if choice in ["1", "sit by the camp fire"]:
            if not game_state["water"]:
                printmorning("As you look closely you realize that there's a shining object inside the campfire")
                ready_choice = input("Do you want to pick it up? (yes/no): ").strip().lower()
                if ready_choice == "yes":
                    if not game_state["burned"]:
                        printmorning("*You try to pick up the shining object*")
                        printmorning("Yunli: Ack! Hot!")
                        printmorning("*You were unable to pick up the shining object*")
                        printmorning("Yunli: What was I thinking...")
                        game_state["burned"] = True
                        
                    else:
                        printmorning("Yunli: I'll get burned again if I try to grab that")
                        printmorning("Yunli: Maybe I can put out the fire...")

                elif ready_choice == "no":
                        print1("*You leave the shining object where it is*")    
            else:
                printmorning("*You sit by the campfire for a bit*")
                printmorning("Yunli: How nice...")

        elif choice in ["water bucket", "water"]:
            if game_state["water_bucket"]:
                if not game_state["water"]:
                    ready_choice = input("Do you want to pour water over the camp fire? (yes/no): ").strip().lower()
                    if ready_choice == "yes":
                        printmorning ("*You pour water over the camp fire")
                        game_state["water"] = True
                        game_state["water_bucket"] = False
                        printmorning("*You pick up the shining object*")
                        printmorning("Yunli: It's a key!")
                        printmorning("*Key 3 has been added to your inventory*")
                        add_items(inventory, ["key 3"])
                        add_items(inventory, ["bucket"])
                        remove_item(inventory, "water_bucket")
                        game_state["key_3"] = True
                    elif ready_choice == "no":
                        printmorning("*You leave the camp fire alone*")
                else:
                    printmorning("*You've already put out the campfire*")
            else:
                printmorning("Yunli: I don't have a bucket of water on me, maybe I can find one nearby")

        elif choice in ["2", "sit on the bench"]:
            printmorning("Yunli: Oh, a bench!")
            printmorning("Yunli: My legs are getting pretty tired...")
            if not game_state["coin 1"]:
                ready_choice = input("You find a coin on the bench do you want to pick it up? (yes/no): ").strip().lower()
                if ready_choice == "yes":
                        print1("*You pick up the coin*")
                        printmorning("Yunli: Nice!")
                        add_items(inventory, ["coin"])
                        game_state["coin 1"] = True
                        print1("*You sit on the bench*")
                        print1("*A few minutes pass by*")
                        printbus("...")
                        printbus("...")
                        print1("Yunli: Much better!")
                        print1("*You get off the bench*")
                elif ready_choice == "no":
                        print1("*You leave the coin where it is*")
                        print1("*You sit on the bench*")
                        print1("*A few minutes pass by*")
                        printbus("...")
                        printbus("...")
                        print1("Yunli: Much better!")
                        print1("*You get off the bench*")
            else:
                print1("*You sit on the bench*")
                print1("*A few minutes pass by*")
                printbus("...")
                printbus("...")
                print1("Yunli: Much better!")
                print1("*You get off the bench*")

        elif choice in ["3","shop"]:
            if not game_state["third_visit"]:
                if not game_state["second_visit"]:
                    printmorning("Yunli: Oh, a shop!")
                    printmorning("*You see a woman with a cloak emerge from behind the counter of the mini shop*")
                    printmorning("???: Hello, I'm Kumiko, welcome to my shop")
                    game_state["second_visit"] = True
                    if game_state["coin 1 buy"] == True:
                        printmorning("Kumiko: We're closed right now")
                        printmorning("Yunli: What?! But I was just here not to long ago...")
                        printmorning("Kumiko: That's just how business is, plus, it doesn't look like you have any money on you right now")
                        printmorning("Yunli: Oh... I guess you're right")
                        printmorning("*You walk back to the camp site with a defeated look*")
                        game_state["third_visit"] = True
                    elif game_state ["coin 1"] == True:
                        print1("What would you like to buy?\n1. Paper Lily\n2. Red Scarf\n3. Leave")
                        choice = get_input("")
                        if choice in ["1", "paper lily"]:
                            printmorning("*You buy the Paper Lily*") # Paper lily referenceee
                            printmorning("Yunli: What does it do?")
                            printmorning("Kumiko: Oh it's just a folded piece paper...")
                            game_state["coin 1 buy"] = True
                            remove_item(inventory, "coin")
                            add_items(inventory, ["paper_lily"])
                        elif choice in ["2", "Red Scarf"]:
                            printmorning("*You buy the Red Scarf*")
                            printmorning("*You wrap the red scarf around your neck*") # Paper lily references intensify
                            game_state["coin 1 buy"] = True
                            remove_item(inventory, "coin")
                            add_items(inventory, ["red_scarf"])
                        elif choice in ["3", "leave"]:
                            printmorning("Kumiko: Thanks for visiting!")
                    else:
                        printmorning("Kumiko: It seems you don't have any money, and I don't appreciate window shoppers")
                        printmorning("Yunli: Oh, I guess you're right.. I'll come back when I find some!")
                        # no one question how kumiko knows how much money you have at all times, she just like that fr

                else:
                    printmorning("Kumiko: Welcome to my sho- Oh, it's you again...")
                    if game_state["coin 1 buy"] == True:
                        printmorning("Kumiko: We're closed right now")
                        printmorning("Yunli: What?! But I was just here not to long ago...")
                        printmorning("Kumiko: That's just how business is, plus, it doesn't look like you have any money on you right now")
                        printmorning("Yunli: Oh... I guess you're right")
                        printmorning("*You walk back to the camp site with a defeated look*")
                        game_state["third_visit"] = True
                    elif game_state ["coin 1"] == True:
                        print1("What would you like to buy?\n1. Paper Lily\n2. Red Scarf\n3. Leave")
                        choice = get_input("")
                        if choice in ["1", "paper lily"]:
                            printmorning("*You buy the Paper Lily*") # Paper lily referenceee
                            printmorning("Yunli: What does it do?")
                            printmorning("Kumiko: Oh it's just a folded piece paper...")
                            game_state["coin 1 buy"] = True
                            remove_item(inventory, "coin")
                            add_items(inventory, ["paper_lily"])
                        elif choice in ["2", "Red Scarf"]:
                            printmorning("*You buy the Red Scarf*")
                            printmorning("*You wrap the red scarf around your neck*") # Paper lily references intensify
                            game_state["coin 1 buy"] = True
                            remove_item(inventory, "coin")
                            add_items(inventory, ["red_scarf"])
                        elif choice in ["3", "leave"]:
                            printmorning("Kumiko: Thanks for visiting!")
                    else:
                        printmorning("Kumiko: It seems you don't have any money, and I don't appreciate window shoppers")
                        printmorning("Yunli: Oh, I guess you're right.. I'll come back when I find some!")
                        # no one question how kumiko knows how much money you have at all times, she just like that fr
            else:
                printmorning("Yunli: They're closed right now... and I don't have any money")
        
        elif choice in ["4", "leave"]:
            ("*You leave the camp site*")
            unknown_forest()
            break

def lake():
    while True:
        print1("Where would you like to go?\n1. Abandoned home\n2. Docks\n3. Leave")
        choice = get_input("")  # Use centralized input 
        
        if choice is None:
            continue
        elif choice in ["1", "abandoned home"]:
            print1("*You take a look inside, and find a pitch black room with spider webs, along with some statues covered with a blanket*")
            abandoned_home()
            break
        elif choice in ["2", "the dock"]:
            printmorning("*You walk down to the wooden docks on the lake*")
            printmorning("Yunli: Is that?-")
            docks()
            break
        elif choice in ["3", "leave"]:
            printmorning("*You head back to the forest*")
            unknown_forest()
            break

def docks():
    printmorning("*You find a boat that seems to be docked*")
    while True:
        print1("What would you like to do?\n1. Check out the boat\n2. Leave") # What was that stick thing you wanted to do again
        choice = get_input("")
        if choice in ["1", "check out the boat"]:
            if not game_state["how_boat"]:
                printmorning("Yunli: Maybe I can get out of the forest with this boat!")
                print1("Would you like to get on the boat? (yes/no)")
                choice = get_input("")
                if choice in ["yes", "y"]:
                    printmorning("*You take a step onto the boat, but remember that you don't know how to drive one*")
                    printmorning("Yunli: If only I knew how to use one of these!")
                    game_state["how_boat"] = True
                    printmorning("*During your learning experience, you notice a bucket on the boat*")
                    print1("Would you like to take the bucket? (yes/no)")
                    choice = get_input("")
                    if choice in ["yes", "y"]:
                        printmorning("*You take the bucket*")
                        game_state["bucket"] = True
                        add_items(inventory, ["bucket"])
                        printmorning("Yunli: I could probably fill this with something")
                    elif choice in ["no", "n"]:
                        printmorning("Yunli: I shouldn't take someone elses things...")
                elif choice in ["no", "n"]:
                    printmorning("Yunli: Maybe I shouldn't get on a strangers boat...") # stranger danger yunli, good job
            else:
                if not game_state["bucket"]:
                    printmorning("Yunli: There's a bucket on the boat")
                    print1("Would you like to take the bucket? (yes/no)")
                    choice = get_input("")
                    if choice in ["yes", "y"]:
                        printmorning("*You take the bucket*")
                        game_state["bucket"] = True
                        add_items(inventory, ["bucket"])
                        printmorning("Yunli: I could probably fill this with something")
                    elif choice in ["no", "n"]:
                        printmorning("Yunli: I shouldn't take someone elses things...")
                else:
                    printmorning("Yunli: I should've learned how to operate one of those...")
        elif choice in ["2", "leave"]:
            printmorning("*You decide to go back to the opening in the forest*")
            lake()
            break
        elif choice in ["bucket"]:
            if not game_state["water_bucket"]:
                if game_state["bucket"]:
                    print1("Do you want to fill the bucket with water? (yes/no)")
                    choice = get_input("")
                    if choice in ["yes", "y"]:
                        printmorning("*You fill the bucket with water*")
                        game_state["water_bucket"] = True
                        remove_item(inventory, "bucket")
                        add_items(inventory, ["water_bucket"])
                        printmorning("Yunli: It's heavy...")
                    elif choice in ["no", "n"]:
                        printmorning("*You decide not to fill the bucket with water*")
                else:
                    printmorning("Yunli: I don't have a bucket, maybe I can find one around here")
            else:
                printmorning("Yunli: I already filled the bucket with water")
                             
def abandoned_home():
    while True:
        print1("What would you like to do?\n1. Investigate the area\n2. Climb upstairs \n3. Leave")
        choice = get_input("")  # Use centralized input

        if choice is None:
            continue  # If inventory was opened, re-prompt
        if choice in ["1", "investigate the area"]:
            printmorning("You walk around the house searching for anything of notice")
            printmorning("*After some time...*")
            if not game_state["key_2"]:
                printmorning("*You find a shining object under the carpet*")
                print1("Do you want to pick up shining object? (yes/no): ")
                choice = get_input("")
                if choice == "yes":
                    printmorning("*You pick up the shining object*")
                    printmorning("Yunli: It's a key!")
                    printmorning("*Key 2 has been added to your inventory*")
                    add_items(inventory, ["key 2"])
                    game_state["key_2"] = True
                elif choice == "no":
                    printmorning("*You think nothing of it and leave it under the carpet*")
            else:
                printmorning("*You find nothing*")
                printmorning("Yunli: All that searching for nothing...")
                
        elif choice in ["2", "climb upstairs"]:
            print1("*You head upstairs, and see room filled with cobwebs and dirt*")
            printmorning ("Yunli: I'm not going up there") # I ain't doing allat
            
        elif choice in ["3","leave"]:
            print1("*You leave the abandoned home*")
            lake()
            break
            
            
def unknown_building():

    while True:
        print1("Where would you like to go?\n1. Front desk\n2. Washroom \n3. Waiting area \n4. Leave")
        choice = get_input("")  # Use centralized input

        if choice is None:
            continue  # If inventory was opened, re-prompt

        if choice in ["1", "Front desk"]:
            print1("*You find a note*")
            print1("It reads 'Train 1 is going to be delayed by approximately 3 minutes, due to boarding errors at the previous stop.' 'Make sure to update the schedule accordingly'")
            print1("Yunli: Interesting..")
            print1("*Type notes to re-read the note*") # add in this feature
            add_items(inventory, ["Note"])
            game_state["note 1"] = True
            if not game_state["coin"]:
                ready_choice = input("You find a coin do you want to pick it up? (yes/no): ").strip().lower()
                if ready_choice == "yes":
                        print1("*You pick up the coin*")
                        printmorning("Yunli: Sweet!")
                        add_items(inventory, ["coin"])
                        game_state["coin"] = True
                elif ready_choice == "no":
                        print1("*You leave the coin where it is*")
            else:
                print1("*You find some pens on the desk*")
        elif choice in ["2", "washroom"]:
            printmorning("*You enter the washroom*")
            print1("*You find a note*")
            print1("It reads 'Honestly, people can't even use public restrooms nowadays, everything is always so crowded.'")
            print1("'I mean, I'm stuck here with 3 people and only 2 urinals, and one of them is broken!'")
            print1("'When are the maintenance people going to fix this...'")
            print1("Yunli: Interesting..")
            print1("Yunli: Sounds like a men problem to me!")
            print1("*Type notes to re-read the note*")
            add_items(inventory, ["Note"])
            game_state["note 3"] = True
        elif choice in ["3", "waiting area"]:
                waiting_room()
                break

        elif choice in ["4", "leave"]:
            printmorning("*You leave the building*")
            train_station()
            break

def waiting_room():
    print1("You enter the waiting area...")
    while True:
        print1("What would you like to do?\n1. Check the seats\n2. Vending machine\n3. Check the ticket system\n4. Leave")
        choice = get_input("")  # Use centralized input
        if choice is None:
            continue
        if choice in ["1", "check the seats"]:
            print1("*You find a note*")
            print1("It reads 'DO NOT REMOVE LABEL: This seat is made with 2 percent real leather and the rest are probably some toxic chemicals from the power plants in America, or something.'")
            print1("'Actually, they don't tell us what these are made of, there's probably only 3 people who read labels like this anyway.'")
            print1("Yunli: Interesting..")
            print1("*Type notes to re-read the note*")
            add_items(inventory, ["Note"])
            game_state["note 2"] = True
        elif choice in ["2", "vending machine"]:
            print1("*You find chips in the vending machine...*")
            if not game_state["spook"]:
                if not game_state["vending_machine"]:
                    if not game_state["coin"]:
                        print1("Yunli: Man, I wish I had a coin")
                    elif game_state["coin"]:
                        game_state["vending_machine"] = True
                        print1("*You buy a bag of chips*")
                        print1("*The chips get stuck on the vending machine*")
                        ready_choice = input("Do you want to shake the vending machine? (yes/no): ").strip().lower()
                        if ready_choice == "yes":
                            print1("*Your bag of chips falls down*")
                            remove_item(inventory, "coin")
                            game_state["coin"] = False
                            ready_choice = input("Do you want to eat the chips? (yes/no): ").strip().lower()
                            if ready_choice == "yes": #you can add thing if you want
                                print1("Yunli: These chips taste... strange...")
                                printbus("...")
                                print1("*As you eat the chips, you start feeling dizzy, and eventually collapse")
                                game_state["spook"] = True
                                print1("*You wake up in a dark room, and see a long hallway*")
                                printmorning("Yunli: Where.. am I...")
                                print1("*You start heading through the hallway*")
                                print1("*As you do, you start to hear your classmates laughing*")
                                print1("*You walk into the room, and see something on the table*")
                                printmorning("Yunli: ..!")
                                print1("*You see a dead cat on a plate, with a fork and knife*")
                                print1("Classmate: Yunli! Have a bite!")
                                print1("Yunli: I... don't want to...")
                                print1("Classmate: C'mon, eat it!")
                                print1("Do you want to eat the corpse? (yes/no)") # Closing the terminal here actually boots you back to the waiting room which is really funny
                                choice = get_input("")
                                if choice in ("Yes", "yes"):
                                    printmorning("Yunli: I-I'll do it..")
                                    print1("*You're forced to eat it*")
                                    print1("*The classes laughter intensifies*")
                                    print1("*You feel a burning sensation as it goes down your throat*")
                                    print1("*You feel a sharp pain in your stomach*")
                                    print1("*You faint*")
                                    print1("Ending 9 - That doesn't taste very good does it")
                                    game_state["ending_9"] = True
                                    print1("That was disturbing, to say the least...")
                                    print1("Lets go back to that waiting room you found yourself in")
                                    
                                if choice in ("No", "no"):
                                    printmorning("Yunli: I-I'm not going to eat that..")
                                    print1("*The class goes silent*")
                                    print1("Classmate: Eat. It.")
                                    print1("Do you want to eat the corpse? (yes/no)")
                                    choice = get_input("")
                                    if choice in ("Yes", "yes"):
                                        printmorning("Yunli: I-I'll do it..")
                                        print1("*You're forced to eat it*")
                                        print1("*The classes laughter intensifies*")
                                        print1("*You feel a burning sensation as it goes down your throat*")
                                        print1("*You feel a sharp pain in your stomach*")
                                        print1("*You faint*")
                                        print1("Ending 9 - That doesn't taste very good does it")
                                        game_state["ending_9"] = True
                                        print1("That was disturbing, to say the least...")
                                        print1("Lets go back to that waiting room you found yourself in")
                                        
                                    if choice in ("No", "no"):
                                        printmorning("Yunli: I'm not doing it!")
                                        print1("*The class stares at you, silently*")
                                        print1("*You attempt to leave through the hallway, but are blocked*")
                                        print1("*You see a tall, skinny man, standing in front of you*")
                                        print1("*You feel a sharp pain*")
                                        print1("*You faint*")
                                        print1("Ending 9 - This is slightly different but hey you still died so-")
                                        game_state["ending_9"] = True
                                        print1("That was disturbing, to say the least...")
                                        print1("Lets go back to that waiting room you found yourself in")
                                        

                        elif ready_choice == "no":
                            print1("Yunli: I'll save these for later!")
                    elif ready_choice == "no":
                        print1("*You got scammed*")
                        printmorning("Yunli: Aww...")
                        remove_item(inventory, "coin")
                else:
                    print1("Yunli: I already bought some chips")
            else:
                printmorning("Yunli: I don't have a good feeling about those...") # Basically you are locked out of dying to that sequence twice in one run

        #ticket system

        elif choice in ["4", "leave"]:
            printmorning("*You head back to the main area*")
            unknown_building()
            break

def end():
    printmorning("You may now close the game")
    input()        

# Main Morning Routine
print1 ("Press enter to start game")
input()
printmorning("*beep* " * 3)
printmorning("*yawns* *Press enter to continue*")
input()
printmorning("*You stretch and feel the warmth of the sun streaming through the window.*")
printmorning("*As the smell of fresh coffee fills the air.*")
printmorning("Yunli: I should get ready.")
printmorning("*If you want access to inventory press i*")
printmorning("*If you want to use an item, type the name of the item*")
morning_routine() 