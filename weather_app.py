import requests
import json

'''
NOTE : YOU NEED SIGNUP IN OPENWEATHERMAP WEBSITE TO GET YOUR OWN API KEY. COPY & PASTE IT IN API_Key VARIABLE
'''
API_Key = ''

city_name = str(input('Enter city name : '))
print(f"Here's the data for {city_name}")
try:
    response_API = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}')
    data = response_API.text
    json_data = json.loads(data)
    print("Temp : ", int(json_data['main']['temp']) - 273)
except:
    print('Invalid City name!!!');

# you can write all the data by observing the json file