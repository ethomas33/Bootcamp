# @TODO: Your code here
# * Create a dictionary to store the following:
#   * Your pet's name
#   * Your pet's age
#   * A list of a few of your pet's hobbies
#   * A dictionary of a few times you wake up during the week

# * Print out the following:
#   * Your pet's name and age.
#   * How many hobbies your pet has.
#   * What your pet's favorite hobby is.
#   * What time your pet wakes on one of the days of the week.
pets = {
        "name": "MaryJane",
        "age": 6,
        "hobbies": {"sleeping", "mud puddles", "eating"},
        "wakeup" : {7, 8, 10},
        }

print(f'Pets name: {pets["name"]}\n Number of hobbies {len(pets["hobbies"])}\n Favorite hobby: {pets["hobbies"]}' )