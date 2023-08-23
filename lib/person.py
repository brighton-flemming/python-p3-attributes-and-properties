#!/usr/bin/env python3



class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

    def __init__(self, name, job):
        self._name = name
        self._job = job
        
    @property
    def name(self):
       return self._name
    
    @property
    def job(self):
        return self._job
    
    @name.setter
    def name(self, new_name):
        if  not (isinstance(new_name, str) and 1 <= len(new_name) <= 25):
         print("Name must be a string between 1 and 25 characters.")
        else:
           self._name = new_name

    @job.setter
    def job(self, new_job):
        if new_job not in  Person.APPROVED_JOBS:
         print("Job must be in list of approved jobs." )
        else:
         self._job = new_job


person = Person("Gwen", "Finance")
print(f"Person's name: {person.name}")
print(f"Person's job: {person.job}")

person.name = "Max"
person.job = "Education"

print(f"Person's name: {person.name}")
print(f"Person's job: {person.job}")

person.name = "Wolfeschlegelsteinhausenbergerdorff,"
person.job = "Production"

print(f"Person's name: {person.name}")
print(f"Person's job: {person.job}")
       
           