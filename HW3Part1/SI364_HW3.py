## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).
import requests
from flask import Flask, request, render_template, json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)


##artistform
@app.route('/artistform')
def artistForm():
    return render_template('artistform.html')

@app.route('/artistinfo', methods = ['GET', 'POST'])
def artist_result():
	if request.method == 'GET':
		result = request.args
		params = {}
		params['term'] = result.get('artist')
		resp = requests.get('https://itunes.apple.com/search?', params = params)
		data_return = json.loads(resp.text)
		r = json.dumps(data_return, indent = 2)
		print(r)
		return render_template('artist_info.html', objects = data_return["results"])

@app.route('/artist_links')
def artistLinks():
    return render_template('artist_links.html')

@app.route('/specific/song/<artist_name>')
def specific_artist(artist_name):
	if request.method == 'GET':
		result = request.args
		params = {}
		params['term'] = artist_name
		resp = requests.get('https://itunes.apple.com/search?', params = params)
		data_return = json.loads(resp.text)
		r = json.dumps(data_return, indent = 2)
		print(r)
		return render_template('specific_artist.html', results = data_return["results"])


##artist_info

##artist_links


##specific song, artist name, specific artist.html 
