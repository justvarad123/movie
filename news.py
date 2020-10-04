from flask import Flask,request,make_response,render_template
import os,json
import requests

app = Flask(__name__) 

@app.route('/weather', methods =['POST', 'GET'])
def weather():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
def processRequest(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    if parameters.get("city") :
    	city = parameters.get("city")
    	BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    	API_KEY = "c7258453da79906d58e0cf0e26e1ab7a"
    	URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
    	# HTTP request
    	response = requests.get(URL)
    	# checking the status code of the request
    	if response.status_code == 200:
    		list_of_data = response.json()
    		report = list_of_data['weather']
    		# data for variable list_of_data
    		temp= list_of_data['main']['temp']- 273.15
    		wt="Nice weather"
    		tempe=float("{0:.2f}".format(temp))
    		pressure=list_of_data['main']['pressure']
    		humidity=list_of_data['main']['humidity']
    		rep=report[0]['description']
    		data="Today's Weather in " + city + ": "+'\n' + "Temperature: " + str(tempe) + " Celsius."+'\n'+ " Pressure: " + str(pressure) +"."+'\n' + " Humidity: " + str(humidity) +"." +'\n'+ " Weather Report: " + rep
    	return {
    		"fulfillmentText": data
    		}
    elif parameters.get("movie") :
    	movie = parameters.get("movie")
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
    		data="Movie Name: " + title +"."+'\n'+ "Released Date: " + release+"."+'\n' + "Movie Runtime: " + runtime+"."+'\n' + "Genre: " + genre+"."+'\n' + "Director: " + director+"."+'\n' + "Writer: " + writer+"."+'\n' + "Actors: " + actors+"."+'\n' + "Plot: " + plot+"."+'\n' + "Language: " + language+"."+'\n' + "Country: " + country+"."+'\n' + "Ratings: "+ratings 
    	return {
            "fulfillmentText": data
            }
    elif parameters.get("news") :
        BASE_URL = "http://newsapi.org/v2/top-headlines?sources=the-times-of-india"
        API_KEY = "958489624d644223868ffc6925ffa67d"
        URL = BASE_URL + "&apikey=" + API_KEY
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:
            list_of_data = response.json()
            le=list_of_data['totalResults']
            l=int(le)
            c=list_of_data['articles']
            news=""
            for i in range(l):
                con=c[i]['title']
                if con!=None:
                    news=news + con +"."+'\n'
        return {
            "fulfillmentText" : news
        }
    

if __name__ == '__main__':
    app.run(debug = True) 
