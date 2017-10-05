import requests
import omdb
import re
from flask import Flask, request, render_template, json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

# @app.route('/movieform')
# def movieForm():
#     return render_template('movieform.html')

# @app.route('/movieinfo', methods = ['GET', 'POST'])
# def movie_result():
# 	if request.method == 'GET':
# 		result = request.args
# 		movie_title = result.get('movie')
# 		movie_info = omdb.title(movie_title)
# 		movie_title_attr = movie_info["title"]
# 		movie_imdb = movie_info["imdb_rating"]
# 	print(movie_info)
# 	return(movie_info)
# 	# return render_template(movieinfo.html, movie_name = movie_title_attr, rating = movie_imdb)	
#     # return render_template('movieinfo.html')

@app.route('/wordform')
def wordForm():
	return render_template('wordform.html')

@app.route('/wordinfo')
def wordinformation():
	if request.method == 'GET':
		result = request.args
		the_word = result.get('favoriteword')
		if "z" in the_word:
			answer = "is"

		else:
			answer = "is not"

	return render_template('wordinfo.html', the_response = answer)


@app.route('/wordcount')
def wordCount():
	return render_template('wordcount.html')

@app.route('/countinfo')
def countinfo():
	if request.method == 'GET':
		result = request.args
		word = result.get('enteredword')
		regex = r'(\w+)'
		word_list = re.findall(regex, word)
		word_counter = 0
		for word in word_list:
			word_counter+=1
		print(word_counter)
		return render_template('countinfo.html', wordcount = word_counter)





