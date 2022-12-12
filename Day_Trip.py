def generate_random_item(list_of_items):
    result = list_of_items
    return result

destinations = ["Destination: Pensacola", "Destination: Cyprus", "Destination: Colorado Springs", "Destination: Dallas"]
restaurants = ["Restaurants: La Cabana", "Restaurants: Burgers and More", "Restaurants: Fresh Garden", "Restaurants: Garcia's"]
transportation = ["Transportation: car", "Transportation: plane", "Transportation: train", "Transportation: helicopter"]
entertainment = ["Entertainment: circus", "Entertainment: boat rides", "Entertainment: parachuting", "Entertainment: hiking"]
list_of_items = ["destinations", "restaurants", "transportation", "entertainment"]

import random
print(random.choice(destinations))

import random
print(random.choice(restaurants))

import random
print(random.choice(transportation))

import random
print(random.choice(entertainment))

#results = random.choice(destinations) + random.choice(restaurants) + random.choice(transportation) + random.choice(entertainment)

user_input = input("Are you satisfied with your trip? Y or N ")
if user_input == "Y":
  print("Here is your final trip! Enjoy!")
elif user_input == "N" :
  print("Which option would you like to change? destinations, restaurants, transportation, entertainment")



#choice = random.choice(list_of_items)
#print(choice)

#import random
#trip_options = random.sample(destinations, 1) + random.sample(restaurants, 1) + random.sample(transportation, 1) + random.sample(entertainment, 1)
    


#for trip_option in trip_options:
 #   list_of_items =  random.sample(destinations, 1) + random.sample(restaurants, 1) + random.sample(transportation, 1) + random.sample(entertainment, 1)
  #  print(*list_of_items)


# 


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
