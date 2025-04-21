from flask import Flask, request, jsonify, Response
import random
from datetime import datetime, timedelta

app = Flask(__name__)

weather_conditions=forecast_conditions = [
    ["Breezy",23],
    ["Mostly Sunny",34],
    ["Mostly Cloudy",28],
    ["Partly Cloudy",30],
    ["Cloudy",26],
    ["Clear",31]
]
def forecast_cond(current_date):
    forecast = []
    for i in range(10):
        day = current_date + timedelta(days=i)
        condition = random.choice(weather_conditions)
        high = random.randint(25, 35)
        low = random.randint(13, 24)
        forecast.append({
            "code": condition[1],
            "date": current_date.strftime("%d %b %Y"),
            "day": current_date.strftime("%a"),
            "high": str(high),
            "low": str(low),
            "text": condition[0]
        })
    return forecast   
     
@app.route('/w/<city>', methods=['GET'])
def Weather(city):
    format=request.args.get('format','json')
    current_date = datetime.now()
    if format =='json':
        resp = { "query": {
    "count": 1,
    "created": "2025-04-21T08:52:56Z",
    "lang": "en-IN",
    "results": {
      "channel": {
    "title": f"Yahoo! Weather - {city}",
       "description": f"Yahoo! Weather for {city}",
            "lastBuildDate": current_date.strftime("%a, %d %b %Y %I:%M %p"),
            "location": {
                            "city": city,
                        },
            "wind": {
                    "chill": str(random.randint(0, 50)),
                    "direction": str(random.randint(0, 360)),
                    "speed": str(random.randint(20, 75))
                    },
            "item":{"forecast": forecast_cond(current_date),
            "guid": {
                            "isPermaLink": "false"
                    }
           }}}}}
                    
        return jsonify(resp)
    else:
        forecast=''
        for f in forecast_cond(current_date):
            print("hi")
            forecast+=f"""
            <yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="{f["code"]}" date="{f["date"]}" day="{f["day"]}" high="{f["high"]}" low="{f["low"]}" text="{f["text"]}"/>
            """
        resp=f"""<?xml version="1.0" encoding="UTF-8"?>
        <query> <results> <channel>
        <title>Yahoo! Weather - {city}</title>
        <description>Yahoo! Weather for {city}</description>
        <lastBuildDate>{current_date.strftime("%a, %d %b %Y %I:%M %p")}</lastBuildDate>
        <item>{forecast}</item>
        </channel> </results> </query>
        """
        return Response(resp,mimetype='application/xml')


app.run()
