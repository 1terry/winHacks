# This is used to create a local server and allow the frontend to talk with the backend.
# March 27, 2021 (8:24 pm)

# Completed the sample class. It should be able to accept json files of the given format.
# March 27, 2021 (11:41 pm)

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
from maps import maps
from co2 import co2
import json


app = Flask(__name__)


@app.route("/")
def home():
    # data = {
    #     "originCoords": {
    #         "lat": "43.663476",
    #         "lng": "-79.658687"
    #     },
    #     "destinationCoords": {
    #         "lat": "43.601354",
    #         "lng": "-79.610622"
    #     },
    #     "occupancy": 1,
    #     "carSize": "SMALL_CAR"
    # }

    # startLat = data["originCoords"]["lat"]
    # startLong = data["originCoords"]["lng"]
    # destLat = data["destinationCoords"]["lat"]
    # destLong = data["destinationCoords"]["lng"]
    # passengers = int(data["occupancy"])  # This needs to be an integer value
    # carSize = data["carSize"]

    # newMap = maps(startLat, startLong, destLat, destLong)
    # newCO2 = co2(passengers, carSize, newMap)

    # response = {'distance': newMap.getDistance(
    # ), 'emissions': newCO2.tripEmissions()}

    # print(response)

    return "<h1>Welcome to the server</h1>"

# This method is used to handle post requests.


@app.route('/post/', methods=['POST'])
def postmethod():

    # Grabs the json file that is provided.
    data = request.json

    # We need to go through the json to get the values we want and create appropriate objects.
    startLat = data["originCoords"]["lat"]
    startLong = data["originCoords"]["lng"]
    destLat = data["destinationCoords"]["lat"]
    destLong = data["destinationCoords"]["lng"]
    passengers = int(data["occupancy"])  # This needs to be an integer value
    carSize = data["carSize"]

    # Creating a new map object with the given values.
    newMap = maps(startLat, startLong, destLat, destLong)

    # Creating a co2 with the required values.
    newCO2 = co2(passengers, carSize, newMap)

    # Creating a dictionary with the given values.
    response = {'distance': newMap.getDistance(
    ), 'emissions': newCO2.tripEmissions()}

    # Creating a json file to be returned.
    # return (json.dump(data, indent=3))
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
