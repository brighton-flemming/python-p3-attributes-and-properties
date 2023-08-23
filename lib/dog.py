#!/usr/bin/env python3
class Dog:
   
   APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer",
    "Dobberman"
 ]
   

   def __init__(self, name, breed):
      self._name = name
      self._breed = breed
   
   @property
   def name(self):
      return self._name 

   @property
   def breed(self):
      return self._breed
   
   @name.setter
   def name(self, another_name):
      if not (isinstance(another_name, str) and 1 <= len(another_name) <= 25):
         print("Name must be a string between 1 and 25 characters.")
  
      else:
          self._name = another_name

   @breed.setter
   def breed(self, new_breed):
      if new_breed not in  Dog.APPROVED_BREEDS:
        print("Breed must be in the list of approved breeds.")
      else:
        self._breed = new_breed

dog = Dog("Buddy", "Golden Retriever")
print(f"Dog's name: {dog.name}")
print(f"Dog's breed: {dog.breed}")

dog.name = "Max"
dog.breed = "Poodle"

print(f"Dog's name: {dog.name}")
print(f"Dog's breed: {dog.breed}")

dog.name = "A very long dog name that is too long"
dog.breed = "Chihuahua"

print(f"Dog's name: {dog.name}")
print(f"Dog's breed: {dog.breed}")



    



      

