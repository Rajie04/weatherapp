import requests

api_key = 'd084d3ea1a9aa98ebcf26383957e6a97'
#get user input
userInput = input('Enter City: ')

#fetch weather data
weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userInput}&units=imperial&APPID={api_key}")
if weatherData.json()['cod'] == '404':
    print("No City Found")
else: 
    #choose which data to display
    weather = weatherData.json()['weather'][0]['main']
    temp = round(weatherData.json()['main']['temp'])
    tempMin = round(weatherData.json()['main']['temp_min'])
    tempMax = round(weatherData.json()['main']['temp_max'])

    print(f'The weather in {userInput} is {weather}')
    print(f'The temperature is {temp}°F, with a high of {tempMax}°F and a low of {tempMin}°F.')