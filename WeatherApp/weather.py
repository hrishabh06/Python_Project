from flask import Flask, render_template, request
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])
def weather():
	if request.method == 'POST':
		city = request.form['city']
	else:
		# for default name mathura
		city = 'Bangalore'

	# your API key
	api = '264c97493345c6795515d829098aee87'

	# source contain json data from api
	source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api).read()

	# converting JSON data to a dictionary
	list_of_data = json.loads(source)

	# data for variable list_of_data
	data = {
		"country_code": str(list_of_data['sys']['country']),
		"city_name" : str(list_of_data['name']),
		"desc" : str(list_of_data['weather'][0]['description']),
		"coordinate": str(list_of_data['coord']['lon']) +' '+ str(list_of_data['coord']['lat']),
		"temp": str(list_of_data['main']['feels_like']) + 'K',
		"pressure": str(list_of_data['main']['pressure']),
		"humidity": str(list_of_data['main']['humidity']),
	}
	print(data)
	return render_template('index.html', data = data, temp = data['temp'])




if __name__ == '__main__':
	app.run(debug = True)
