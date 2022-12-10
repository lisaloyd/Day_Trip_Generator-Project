def generate_random_item(list_of_items):
    result = list_of_items
    return result


destinations = ["Destination: Pensacola", "Destination: Cyprus", "Destination: Colorado Springs", "Destination: Dallas"]
restaurants = ["La Cabana", "Burgers and More", "Fresh Garden", "Garcia's"]
transportation = ["car", "plane", "train", "helicopter"]
entertainment = ["circus", "boat rides", "parachuting", "hiking"]

import random
list_of_items = ["destinations", "restaurants", "transportation", "entertainment"]
trip_options = random.sample(destinations, 1) + random.sample(restaurants, 1) + random.sample(transportation, 1) + random.sample(entertainment, 1)
    


for trip_option in trip_options:
    list_of_items =  random.sample(destinations, 1) + random.sample(restaurants, 1) + random.sample(transportation, 1) + random.sample(entertainment, 1)
    print(*list_of_items)





# random.sample()
# Are you satisfied with your trip? Y or N
# Which option would you like to change? distinations, restaurants, transportation, entertainment
# Here is your final trip!

# def run_day_trip_generator():

# def print_full_trip(list_of_options):
# def generate_random_item(list_of_items):
# def determine_satisfaction(current_trip, trip_options):
# def re_select_option(current_trip, options):

# run_day_trip_generator()

# random.sample(list,k) where k represents, number of values to be sampled.
# list_1 = [1,3,5]

# final_list = random.sample(list_1,1)+random.sample(list_2,1)+random.sample(list_3,1)
