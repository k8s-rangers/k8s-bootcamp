import requests
import time
api_key = 'd546d2a965f4b0993fecca033f7664df'
city_name1 = 'Bengaluru'
city_name2 = 'Mumbai'
city_name2 = 'Chennai'
city_names=['Bengaluru','Mumbai','Chennai']
#base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name},IN&appid={api_key}'
#print(base_url)
for city_name in city_names: 
	base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name},IN&appid={api_key}'
	try:
		response = requests.get(base_url)
		data = response.json()

		if data['cod'] == 200:
			temperature = data['main']['temp'] - 273.15  
			print(f"Current temperature in {city_name}: {temperature:.2f}°C")
		else:
			print(f"Error: {data['message']}")

	except Exception as e:
		print(f"An error occurred: {e}")
#time.sleep(50)

