#!/usr/binn/python3
""" Defines Place Class """
from models.base_model import BaseModel

class Place(BaseModel):
    """ Place class that inherites from BaseModel class

    Args:
        BaseModel (class): A Base Class for sub classes
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest =  0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []