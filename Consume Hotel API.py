# Import package
import requests
import pandas as pd

# Assign URL to variable: url
url = 'https://hotels-apis.herokuapp.com/state/lagos'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
hotel_data = pd.DataFrame(json_data)

hotel_dataframes = hotel_data[['hotel_name','location','city','state']]

hotel_csv = hotel_dataframes.to_csv('hotels.csv')
