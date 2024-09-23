#!/usr/bin/python3 env

"""
A dictionary that prints a name, destination, day,
and time
"""
# sentence =[{
#     "name": "Peter",
#     "Destination": "Church",
#     "day": "Monday",
#     "Time": "11.00p.m",
# },
#     {
#         "name": "Enid",
#         "Destination": "Market",
#         "day": "Thursday",
#         "Time": "8.00a.m"
#     }]
# first_sentence = f"{sentence[0]["name"]} went to {sentence[0]["Destination"]} on {sentence[0]["day"]} at {sentence[0]["Time"]}"
# second_sentence = f"{sentence[1]["name"]} went to {sentence[1]["Destination"]} on {sentence[1]["day"]} at {sentence[1]["Time"]}"
# #third_sentence = f"{sentence[0]["name"]} went to {sentence[0]["Destination"]} on {sentence[0]["day"]} at {sentence[0]["Time"]}" #and then went to the {sentence[1]["Destination"]}
#
# my_list = []
# my_list.append(first_sentence)
# my_list.append(second_sentence)
# print(my_list)
# Activities =[]
# this_dict = {}
# for letter in my_list:
#     words = letter.split()
#     #print(words)
#     this_dict["name"] = words[0]
#     this_dict["Destination"] = words[3]
#     this_dict["day"] = words[5]
#     this_dict["Time"] = words[7]
#     #print(this_dict)
#     my_dict = this_dict.copy()
#     Activities.append(my_dict)
# print(Activities)
sentences = {"name": ['Enid', 'Remi', 'Alicia', 'Bii'],
             "Destination": ['Market', 'Church', 'Mosque', 'School'],
             "day": 'Monday',
             "Time": ['11.00am', '12.00pm', '1.00pm', '2.00pm']}

#first_sentence = f"{sentences["name"][0]} went to the {sentences["Destination"][0]} on {sentences["day"]} at {sentences["Time"][0]}"
# second_sentence = f"{sentences["name"][0]} and {sentences["name"][1]} went to {sentences["Destination"][1]} on {sentences["day"]} at {sentences["Time"][1]}"
# third_sentence = f"{sentences["name"][2]} went to the {sentences["Destination"][2]} on {sentences["day"]} at {sentences["Time"][1]} and then went to {sentences["Destination"][3]} at {sentences["Time"][3]}"
# print(f"{sentences["name"][1]} went to the {sentences["Destination"][1]} on {sentences["day"][1]} at {sentences["Time"][1]}")
# print(f"{sentences["name"][2]} went to the {sentences["Destination"][2]} on {sentences["day"][2]} at {sentences["Time"][2]}")
# print(f"{sentences["name"][3]} went to the {sentences["Destination"][3]} on {sentences["day"][3]} at {sentences["Time"][3]}")
my_list = []
#my_list.append(first_sentence)
def to_dictionary(first_sentence, second_sentence):
    my_list = []
    my_list.append(first_sentence)
    my_list.append(second_sentence)
    print(my_list)
    Activities = []

    for letter in my_list:
        words = letter.split()
        #print(words)
        if "and then went to" in letter:
            this_dict={
                "name" : [words[0]],
                "Destination" : [words[4], words[13]],
                "day" : words[6],
                "Time" : [words[8], words[15]]
            }
        else:
            this_dict={
                "name": [words[0], words[2]],
                "Destination": [words[5]],
                "day": words[7],
                "Time": [words[9]]
            }
        #print(this_dict)
        Activities.append(this_dict)
    print(Activities)

to_dictionary('Enid and Remi went to Church on Monday at 12.00pm','Alicia went to the Mosque on Monday at 12.00pm and then went to School at 2.00pm')












# dictionary = {
#                 'name': 'Peter',
#               'Destination': ['Church'],
#               'day': 'Monday',
#               'Time': ['11.00a.m', ]}