from settings import logger
from cars.car import get_car_name


def car_name():
    car = get_car_name()
    logger.info(f"The name of the car is {car}")
    
    
if __name__ == "__main__":
    car_name()