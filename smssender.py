import paho.mqtt.client as mqtt
from flask import Flask, request, make_response, render_template, url_for, g
from flask import send_from_directory, jsonify
from flask_restful import Resource, Api






#Set Parameters
#mqtt connection Params
server = '' #MQTT Broker Address
port = 1883 #MQTT Broker Port
user = '' #MQTT Broker Username
passw = '' #MQTT Broker Password
zanzitoDevice = '' #Name tou gave your device in zanzito settings

def sendSms(phone_number,message):
    client = mqtt.Client("smsSender")
    client.username_pw_set(user,passw)
    client.connect(server)
    return(str(client.publish("zanzito/"+ zanzitoDevice +"/sendsms/"+ str(phone_number),str(message),qos=0,retain=False)))

app = Flask(__name__)
api = Api(app)



@app.route('/')
def start():
    return render_template('index.html')

@app.route('/send', methods=['POST','GET'])
def send_sms():
    try:
        phone_number = str(request.form['phone'])
        message = str(request.form['message'])
        return str(sendSms(phone_number,message))
    except Exception as e:
        return str(e)



# Serve Javascript
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('dist/js', path)

# Serve CSS
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('dist/css', path)

# Serve Images
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('dist/img', path)

# Serve Fonts
@app.route('/webfonts/<path:path>')
def send_webfonts(path):
    return send_from_directory('dist/webfonts', path)

# endregion



# Start Application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7040)