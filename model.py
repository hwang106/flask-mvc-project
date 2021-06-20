import os
# needed to pull from giphy databased
import requests
# needed for twilio integration
# from twilio.rest import Client
import random

# twilio authentication (you'll need to fork and add your own environmental variables for the code to run)
# account_sid = os.environ.get['account_sid']
# auth_token = os.environ.get['auth_token']
# giphy authentication (will also need to add your own key if forked)
# giphy_api_key = os.environ.get['giphy_api_key']
# need to find a way to hide api key on Heroku
giphy_api_key = "LLbmPKaorNSdpO3G3qhqduUS3u7HzxDZ"

def gif_chooser(message_type):
    # hard-coding maximum number of results to pull from giphy database
    num_search_results = 25
    # asking for user input for the query term
    query = message_type    
    # accessing giphy database using api key, user query, and hard-coded maximum number of results
    search_url = "https://api.giphy.com/v1/gifs/search?api_key=" + giphy_api_key + "&q="+ query + "&limit=" + str(num_search_results) + "&offset=0&rating=g&lang=en"

    # pulls data in json format
    response = requests.get(search_url).json()
    
    if(len(response["data"]) < 1):
        return "/static/images/nahmark-gif-not-found.png"

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