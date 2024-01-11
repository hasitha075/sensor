from flask import Flask, render_template
import requests
import json
import hashlib
import uuid
import time

app = Flask(__name__, template_folder='.')

# Insert your generated API keys (http://api.telldus.com/keys)
pubkey = "FEHUVEW84RAFR5SP22RABURUPHAFRUNU"  # Public Key
privkey = "ZUXEVEGA9USTAZEWRETHAQUBUR69U6EF"  # Private Key
token = "060a234349dfc90021cc9ea03945796a06594031d"  # Token
secret = "d78176dbac3ccc72fb904a98f4ffc5b2"  # Token Secret

localtime = time.localtime(time.time())
timestamp = str(time.mktime(localtime))
nonce = uuid.uuid4().hex
oauthSignature = (privkey + "%26" + secret)

def get_sensor_data():



    response = requests.get(
        url="https://pa-api.telldus.com/json/sensors/list",
        params={"includeValues": "1"},
        headers={
            "Authorization": 'OAuth oauth_consumer_key="{}", oauth_nonce="{}", oauth_signature_method="PLAINTEXT", oauth_timestamp="{}", oauth_token="{}", oauth_signat$
            "Content-Type": "application/json",
        },
    )

    responseData = response.json()

    sensor_data = []

    for sensor in responseData.get("sensor", []):
 sensor_name = sensor.get("name", "Unknown Sensor")

        if sensor_name == "TEMP":
            temperature = sensor.get("temp", "N/A")
            humidity = sensor.get("humidity", "N/A")

            current_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            sensor_data.append({
                "time": current_datetime,
                "sensor": sensor_name,
                "temperature": temperature,
                "humidity": humidity
            })

    return sensor_data

@app.route('/')
def index():
    sensor_data = get_sensor_data()
 return render_template('index.html', sensor_data=sensor_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
