from flask import Flask, render_template, request, url_for, redirect, send_file
from werkzeug.utils import secure_filename
from kimin.core_db_web import DB_Core
import os, json, subprocess
server = Flask(
	__name__, 
	static_folder='static', 
	template_folder='templates')

server.jinja_env.auto_reload = True
server.config['TEMPLATES_AUTO_RELOAD'] = True
server.config['DEBUG'] = True
server.secret_key='Project NLP'

@server.route('/download')
def Download():
	return send_file('datasetv1.min', as_attachment=True)

@server.route('/', methods=['POST', 'GET'])
def Utama():
	sin = DB_Core()
	if request.method == 'GET':
		sumber_data = [i for i in sin.Get_Data('sumber_data')['data']]
		id_data = [i['id'] for i in sumber_data]
		dataset = []
		for i in sin.Get_Data('data_text')['data']:
			i['id_sumber'] = sumber_data[id_data.index(i['id_sumber'])]['link_website']
			i['publised_date'] = i['publised_date'][i['publised_date'].find(',')+1:i['publised_date'].find("+")-1]
			dataset.append(i)

		data = {"sumber_data":sumber_data, 'dataset':dataset, "total_data":f"{len(dataset)} Dataset"}

		return render_template("index.html", data=data)

	elif request.method == 'POST':
		subprocess.run(["python", "scraping.py"])
		return redirect('/')

if __name__ == "__main__":
	server.run(debug=True, host='0.0.0.0')