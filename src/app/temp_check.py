"""
Module to take temp measurements and write to the DB
"""

from .models import TempCheck 
from gpiozero import CPUTemperature
from datetime import datetime
from pony.orm import db_session

# Initialize the CPU measurement 
cpu = CPUTemperature()


@db_session
def take_measurement():
"""Takes the reading and writes it to the DB model. """

    temp_check = TempCheck(
            temp_value = cpu.temperature,
            time_of_measurement = datetime.now()
            )

    return temp_check
