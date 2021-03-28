# This is used to create a local server and allow the frontend to talk with the backend.
# March 27, 2021 (8:24 pm)

# Completed the sample class. It should be able to accept json files of the given format.
# March 27, 2021 (11:41 pm)

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
import maps
import co2
import json

app = Flask(__name__)

@app.route("/")
def home():
  return render_template ("index.html")

# This method is used to handle post requests.
@app.route('/postmethod', methods=['POST'])
def postmethod():

  # Grabs the json file that is provided.
  data = request.get_json()

  # We need to go through the json to get the values we want and create appropriate objects.
  startLat = data["originCoords"]["lat"]
  startLong = data["originCoords"]["lng"]
  destLat = data["destinationCoords"]["lat"]
  destLong = data["destinationCoords"]["long"]
  passengers = int (data["occupancy"]) # This needs to be an integer value
  carSize = data["carSize"]
  
  # Creating a new map object with the given values.
  newMap = map (startLat, startLong, destLat, destLong)

  # Creating a co2 with the required values.
  newCO2 = co2 (passengers, carSize, newMap)

  # Creating a dictionary with the given values.
  data = {'distance': newMap.getDistance(), 'emissions': newCO2.getTotalEmissions()}

  # Creating a json file to be returned.
  return (json.dump(data, indent = 3))

if __name__ == "__main__":
  app.run(debug = True)



