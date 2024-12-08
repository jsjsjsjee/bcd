from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Your OpenWeatherMap API Key
API_KEY = '9c403be96a22ee3d639c58c109007a50'

def get_weather_data(city_name, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather')
def weather():
    city_name = request.args.get('city_name')
    if city_name:
        weather_data = get_weather_data(city_name, API_KEY)
        if weather_data:
            return jsonify(weather_data)  # Return JSON response
    return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
