
#Python 3.6

from flask import Flask,send_from_directory,render_template
from flask_restful import Resource, Api
from patient import Patients, Patient
from doctor import Doctors, Doctor
from medicine import medicines,medicine
from appointment import Appointments, Appointment
from bill import bill,bills
from doc_logs import doc_logs,doc_logss
from common import Common
import json
import webbrowser


with open('config.json') as data_file:
    config = json.load(data_file)

app = Flask(__name__, static_url_path='')
api = Api(app)

api.add_resource(Patients, '/patient')
api.add_resource(Patient, '/patient/<int:id>')
api.add_resource(medicines, '/medicine')
api.add_resource(medicine, '/medicine/<int:id>')

api.add_resource(Doctors, '/doctor')
api.add_resource(Doctor, '/doctor/<int:id>')
api.add_resource(Appointments, '/appointment')
api.add_resource(Appointment, '/appointment/<int:id>')
api.add_resource(bills, '/bill')
api.add_resource(bill, '/bill/<int:id>')
api.add_resource(doc_logs, '/doc_logs')
api.add_resource(doc_logss, '/doc_logs/<int:id>')
api.add_resource(Common, '/common')

# Routes

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True,host=config['host'],port=config['port'])
    
