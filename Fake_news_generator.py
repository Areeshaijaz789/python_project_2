import random
objects=["apple",
         "banana",
         "cherry",
         "date",
         "fig",
         "grape",
         "kiwi",
         "lemon",
         "mango",
         "nectarine",
         "orange",
         "papaya",
         "quince",
         "raspberry",
         "strawberry",
         "tangerine",
         "ugli fruit",
         "vanilla bean",
         "watermelon",
         "xigua",
         "yellow passion fruit",
         "Areesha"
         ]
actions=["eats",
         "throws",  
         "kicks",
         "juggles",
         "paints",
         "sings to",
         "dances with",
         "writes about",
         "reads to",
         "cooks",   ]
place_or_things=["in the park",
                 "at home",
                 "at school",
                 "in the office",
                 "at the beach",
                 "on the moon",
                 "under the sea",
                 "in a treehouse",
                 "at a concert",
                 "in a museum",
                 ]
while True: 
    object1=random.choice(objects)
    
    action=random.choice(actions)
    place_or_thing=random.choice(place_or_things)
    print(f"{object1} {action} {place_or_thing}.")
    user_input=input("Press Enter to generate another fake news headline...").strip()
    if user_input.lower() in ['exit', 'quit', 'q']:
        break   