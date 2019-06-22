from flask import Flask,render_template,request
from func import weather_api,quotes_api


app=Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/weather', methods=['POST'])
def weather_quote():
	city=request.form['city']
	weather=weather_api(city)
	quote=quotes_api()
	return render_template('weather.html', city=city, weather=weather, quote=quote)

if __name__ == '__main__':

	app.run(debug="True")