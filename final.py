#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
from matplotlib import pyplot as plt
from matplotlib import image as mpimg


#Living Room
door_d = {
    "name": "door d",
    "type": "door"
}

dining_table = {
    "name": "dining table",
    "type": "furniture"
}

living_room = {
    "name": "living room",
    "type": "room"
}

mystery_door = {
    "name" : "mystery door",
    "type" : "door"
}

mystery_key = {
    "name" : "mystery key",
    "type" : "key",
    "target" : mystery_door

}

#game room
couch = {
    "name": "couch",
    "type": "mystery",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}


#bedroom
queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

nightstand = {
    "name": "nightstand",
    "type": "mystery",
}


door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}


key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

bedroom = {
    "name": "bedroom",
    "type": "room",
}



#bedroom 2

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}
door_b = {
    "name": "door b",
    "type": "door"
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c
}

key_d = {
    "name": "key for door d",
    "type" : "key",
    "target": door_d
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room"
}

#bathroom

outside = {
  "name": "outside"
}

trap = {
    "name" : "trap"
}

all_rooms = [game_room, bedroom, bedroom_2, living_room, outside,trap]

all_doors = [door_a, door_b, door_c, door_d, mystery_door]

# define which items/rooms are related

object_relations = {
    #game room
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "outside": [door_d],
    "door a": [game_room, bedroom],

    #bedroom
    "bedroom": [nightstand, queen_bed, door_b, door_a, door_c],
    "queen bed": [key_b],
    "door b": [bedroom, bedroom_2],
    "door c": [bedroom, living_room],

    #bedroom 2
    "bedroom 2": [double_bed, dresser, door_b],
    "double bed": [key_c],
    "dresser": [key_d],

    #living room
    "living room": [dining_table, door_d, door_c, mystery_door],
    "door d": [outside, living_room],
    "mystery door" : [trap, living_room],
    "dining table" : [mystery_key],
}

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside,
    "game_over_room": trap
}


# In[ ]:


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    image = mpimg.imread("Games_room.png")
    plt.imshow(image)
    plt.show()
    
    
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
   
        #Sound (Good ending)
        pygame.init()
        pygame.mixer.music.load("good_ending.mp3")
        pygame.mixer.music.play()
        
        print("Despite the sounds, you brace yourself, turn the key and open the door. \nYou are blinded by the sunlight, and after a moment you realise that you are outside a big warehouse building, with strange sounds you heard moments before playing over the speaker. \nThere is not a soul around. \nAs you consider your surroundings, you see a banner taped to the door saying 'Congratulations! You are safe... for now' \nYou have escaped the room, but have you escaped the game?")
        
        image = mpimg.imread("Game_ending.png")
        plt.imshow(image)
        plt.show()
        
    elif (game_state["current_room"] == game_state["game_over_room"]):
        
        #Sound (game over)
        pygame.init()
        pygame.mixer.music.load("bad_ending.mp3")
        pygame.mixer.music.play()
        
        #Image (Doungeon)
        image = mpimg.imread("Dungeon.png")
        plt.imshow(image)
        plt.show()
        
        print("Lured by the welcoming sounds, you eagerly open the door waiting for the sweet escape. \nHowever, as you come into the room, the door shuts closed behind you, leaving you in complete darkness. \nThe air is staler than in the previous room. \nAs your eyes adjust, the only thing you can see are the shattered stairs down to what seems like a tomb. \nYou find a plaque next to it reading 'Welcome to level 2. Will you be the first human ever to escape?'")
        
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()
    
def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    if item_name=="mystery door":
                        
                        pygame.init()
                        pygame.mixer.music.load("bloody_door_sound.mp3")
                        pygame.mixer.music.play()
                       
                    
                        #Image (Bright door)
                        image = mpimg.imread("Bright_door.png")
                        plt.imshow(image)
                        plt.show()
                        output += "As you are unlocking the door, you hear faint sounds of birds chirping mixed with pleasant music on the other side. \nThe whole door is lit up, as if sunlight on the other side is too bright not to sip in to the living room. \nAlmost too bright? \nIt seems unnatural and makes you feel ill at ease."
                        next_room = get_next_room_of_door(item, current_room)
                    elif item_name=="door d":
                    #howling sounds
                        pygame.init()
                        pygame.mixer.music.load("bright_door_sound.mp3")
                        pygame.mixer.music.play()
        
                    #Image (Blood Door)
                        image = mpimg.imread("Bloody_door.jpg")
                        plt.imshow(image)
                        plt.show()
                        output += "As you are unlocking the door, you hear strange inhuman sounds on the other side. \nOn closer inspection, you see blood and scratch marks all around the door. \nWho has this much blood? It almost looks fake... \nSomething is off here."
                        next_room = get_next_room_of_door(item, current_room)
                    else:
                        output += "You unlock it with a key you have."
                        pygame.init()
                        pygame.mixer.music.load("door_sound.mp3")
                        pygame.mixer.music.play()
                        next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked and you don't have the key."
            elif (item["type"] == "mystery"):
                if item_name=="couch":
                  output +="At first, nothing seems out of sorts, but on closer inspection, you find a tiny piece of paper wedged between the cushions. \nYou open the note to find a very shakey handwriting, clearly written in a big hurry. \nThe note reads 'Nothing is as it seems. Trust your instincts.'"
                elif item_name=="nightstand":
                  output +="As you open the drawer, something falls out from behind the back wall. A note? \nThe handwriting on this one seems less rushed, written in different ink. \nYou open the note and read 'Look for the mystery door. This is your only chance to escape.'"
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    #Schlüssel geräusch
                    pygame.init()
                    pygame.mixer.music.load("keys_sound.mp3")
                    pygame.mixer.music.play()
                    
                    
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")

    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):

        play_room(next_room)
        
    else:
        play_room(current_room)


# 

# In[ ]:


game_state = INIT_GAME_STATE.copy()

start_game()


# In[ ]:




