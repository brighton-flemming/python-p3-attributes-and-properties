#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
      
   def __init__(self, name=""):
    self._name = ""
    self.name = name
     
   @property
   def name(self):
      return self._name 

   @name.setter
   def name(self, another_name):
      if (isinstance(another_name, str) and 1 <= len(another_name) <= 25):
         self._name = another_name
      else:
         print("Name must be string between 1 and 25 characters.")
         self._name = ""
    
pluto = Dog()
pluto.name = "Randy"
print(pluto.name)



      

