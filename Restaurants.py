from flask import Flask
from flask import render_template
from flask import url_for
import json

def get_Restaurants(Name, Description):
    
    Restaurant_name = Name
    
    Restaurant_Description = Description
    
    return get_Restaurants