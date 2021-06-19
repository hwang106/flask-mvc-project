import os
# needed to pull from giphy databased
import requests
# needed for twilio integration
from twilio.rest import Client
import random

# twilio authentication (you'll need to fork and add your own environmental variables for the code to run)
# account_sid = os.environ.get['account_sid']
# auth_token = os.environ.get['auth_token']
# giphy authentication (will also need to add your own key if forked)
# giphy_api_key = os.environ.get['giphy_api_key']
giphy_api_key = "LLbmPKaorNSdpO3G3qhqduUS3u7HzxDZ"

# greetings = [
#     {
#         "topic" : "Back to School",
#         "generic_message" : 
#         {
#             "bland" : "Happy 1st Day!",
#             "reassuring" : "You got this!",
#             "optimistic" : "Today is a good day to change the world!",
#             "questionable" : "180 more schools days until summer..."   
#         }

#     },
#     {
#         "topic" : "Anniversary",
#         "generic_message" : 
#         {
#             "bland" : "Happy Anniversary!",
#             "reassuring" : "Another Beautiful Year!",
#             "optimistic" : "Just Us Forever!",
#             "questionable" : "Still Stuck With Me I See..."   
#         }
#     },

#     {
#         "topic" : "Birthday",
#         "generic_message" : 
#         {
#             "bland" : "Happy Birthday!",
#             "upbeat" : "Go Shawty, It's Your Birthday!",
#             "dad jokey" : "A long time ago, in a galaxy far, far away...you were born.",
#             "questionable" : "Another year from the beginning; another year closer to the end..."   
#         }
#     },    

#     {
#         "topic" : "Graduation",
#         "generic_message" : 
#         {
#             "bland" :  "You made it!",
#             "optimistic" : "Oh! The Places You'll Go!",
#             "dad jokey" : "You did virtually the best job ever, GRAD.",
#             "questionable" : "Uh, so you can move out now, right?"   
#         }
#     },

#     {
#         "topic" : "Appreciation",
#         "generic_message" : 
#         {
#             "bland" : "I appreciate you.",
#             "optimistic" : "If only everyone were a little more like you.",
#             "mawkish" : "You shine the brightest when the night is darkest.",
#             "questionable" : "I choose you Pikachu!"   
#         }
#     },

#     {
#         "topic" : "Sympathy",
#         "generic_message" : 
#         {
#             "bland" : "My condolences.",
#             "reassuring" : "Our thoughts are with you.",
#             "assuming" : "Anyone who has loved a lot knows how your heart is breaking.",
#             "questionable" : "I'm sorry for your loss, but not sorry enough to pick up a phone and call you."   
#         }
#     }

# ]

# # will need method for reading and writing file for permanent adjustment of list/dictionary database

# # method for appending or replacing generic message, eventually based on user input 
# def append_message(topic_index, generic_message_cat, generic_message):
#   global greetings
#   greetings[topic_index]["generic_message"][generic_message_cat] = generic_message

# # method for appending list, eventually based on user input
# def append_category(topic):
#   global greetings
#   greetings.append({
#     "topic" : topic,
#     "generic_message" : {}
#     })


# print("We only have a limited number of categories to choose from, and here they are: \n")
# # iterating through list of dictionaries
# for category in range(len(greetings)):
#     print(category + 1, end = " ")
#     print(greetings[category]["topic"])

# print("\n")
# choice = int(input("Type the number of the category you are interested in. \n"))
# # user validation; still need to add validation for string input, which throws error during int casting above.
# while(choice - 1 not in range(len(greetings))):
#     print("You need to type one of the numbers above.")
#     choice = int(input("Type the number of the category you are interested in. \n"))

# # adding this variable of a specific dictionary in the list for better readability when referencing sub=dictionaries within the dictionary
# chosen_dictionary = greetings[choice - 1]

# print("\nFor your choice of " + chosen_dictionary["topic"].lower() + ", these are the generic messages: \n")
# # adding a index variable that increments during iteration for UI reasons during print statements
# i = 0
# # iterating through the keys and values in the sub-dictionary of the list of dictionaries 
# for mehssage_flavor, mehssage  in chosen_dictionary["generic_message"].items():
#     print(str(i + 1) + " " + mehssage_flavor.capitalize() + ": " + mehssage)
#     i += 1

# print("\n")
# mehssage_choice = int(input("Type the number of the message you are interested in sending. \n"))
# # validates input; still needs validation for string input
# while(mehssage_choice - 1 not in range(len(chosen_dictionary["generic_message"]))):
#   print("You need to type one of the numbers above.")
#   mehssage_choice = int(input("Type the number of the message you are interested in sending. \n"))

# # there must be a better way to access the value based on key index, especially since dictionaries are now ordered in Python by default?
# chosen_mehssage = list(chosen_dictionary["generic_message"].values())[mehssage_choice - 1]

# #print(chosen_mehssage)

def gif_chooser(message_type):
    # hard-coding maximum number of results to pull from giphy database
    num_search_results = 25
    # asking for user input for the query term
    query = message_type    
    # accessing giphy database using api key, user query, and hard-coded maximum number of results
    search_url = "https://api.giphy.com/v1/gifs/search?api_key=" + giphy_api_key + "&q="+ query + "&limit=" + str(num_search_results) + "&offset=0&rating=g&lang=en"

    # pulls data in json format
    response = requests.get(search_url).json()
    
    # deals with user query's that pulls no results from giphy; should probably rewrite as separate method for readability
    # while(len(response["data"]) < 1):
    #     print("Sorry, there were no GIFs that matched your search term. Try something simpler.")
    #     query = input("\nWhat kind of GIF would you like to send along with your message? \n")
    #     search_url = "https://api.giphy.com/v1/gifs/search?api_key=" + giphy_api_key + "&q="+ query + "&limit=" + str(num_search_results) + "&offset=0&rating=g&lang=en"
    #     response = requests.get(search_url).json()

    #print(len(response["data"]))

    # picks a random gif from the results pulled from giphy
    random_search_index = random.randint(0, len(response["data"])-1)
    random_gif = response["data"][random_search_index]["images"]["original"]["url"]
    return random_gif

# twilio setup
# client = Client(account_sid, auth_token)
# # still need to add user input validation for phone number
# send_number = input("What phone number would you like the GIF sent to? Use the +1XXXXXXXXXX format. \n")
# message = client.messages.create(
#     to=send_number, 
#     from_="+13474932766",
#     body=chosen_mehssage,
#     media_url=[random_gif]
#     )