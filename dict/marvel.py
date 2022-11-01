#!/usr/bin/env python3

heroes= {"flash":
                   {"speed": "fastest", 
                    "intelligence": "lowest", 
                    "strength": "lowest"}, 
         "batman":
                   {"speed": "slowest", 
                    "intelligence": "highest", 
                    "strength": "money"}, 
         "superman":
                   {"speed": "fast", 
                    "intelligence": "average", 
                     "strength": "strongest"}}

print("Flash is " + heroes["flash"]["speed"])  
print("Superman is " + heroes["superman"]["strength"])
print("Batman has the ultimate super power: " + heroes["batman"]["strength"])
