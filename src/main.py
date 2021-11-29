"""
Main application loop, runs the main function at the intervals. 
"""

import time 
from app.temp_check import take_measurement


def main():
    take_measurement()


if __name__ == "__main__":
    while True:
        main()
