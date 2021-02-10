# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 02:19:07 2020

@author: k.kirilov
"""
import random as rm

def zoneCreator():
    #function that creates objects of the zone class
    pass

class Nation:
    #Nations start with 1 or 2 zones, or 1 or 2 cities ,and then try to conquer more (to conquer a zone, you have to conquer all the cities in it)
    #Perhaps move to another file 
    #Nation level resources would be land, labor and capital.
    pass
class Zone:
    #Contains cities, the largest unit on the map. Has natural resources.
    def __init__(self, metals=rm.randint(0, 100), wood=rm.randint(0, 100), water=rm.randint(0, 100), temperature=rm.randint(0, 100)):
        self.resources = {'metals':metals, 'wood':wood, 'water':water, 'temperature':temperature}
        self.cities = []
class City:
    #Within zone, smaller unit on the map. Has produced resources, manpower, etc. All dependent on zone resources.
    def __init__(self, population=rm.randint(1000, 999999))

class Building:
    #base class for all subsequent building classes.
    pass

class Person:
    #Lives in cityy. Does shit. Potentially takes places in armies and other groups that go out of city. Everything depends on profession.
    #each profession will have different risk values and depending on them, they might die on their job.

test = Zone()