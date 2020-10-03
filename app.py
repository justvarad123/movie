from flask import Flask,request,make_response,render_template
import os,json
import requests

movie = "kaithi"
BASE_URL = "http://www.omdbapi.com/?"
API_KEY = "c868370f"
URL = BASE_URL + "t=" + movie + "&apikey=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
	list_of_data = response.json()
	rat=list_of_data['Ratings']
	title=list_of_data['Title']
	release=list_of_data['Released']
	runtime=list_of_data['Runtime']
	genre=list_of_data['Genre']
	director=list_of_data['Director']
	writer=list_of_data['Writer']
	actors=list_of_data['Actors']
	plot=list_of_data['Plot']
	language=list_of_data['Language']
	country=list_of_data['Country']
	ratings=rat[0]['Value']
	data={
	"Title" : title,
	"Release Date" : release,
	"Runtime" : runtime,
	"Genre" : genre,
	"Director" : director,
	"Writer" : writer,
	"Actors" : actors,
	"Plot" : plot,
	"Language" : language,
	"Country" : country,
	"Ratings" : ratings

	}
	
	print(data)
	

      
        