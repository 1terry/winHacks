# This is used to create a local server and allow the frontend to talk with the backend.
# March 27, 2021 (8:24 pm)

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify

@app.route ('/geo', methods = ['GET', 'POST'])
def geo():
  return render_template ('index.html')


@app.route('/postmethod', methods = ['GET', 'POST'])
def get_post_location():
  where = request.form['location']
  return where

@app.route('/postmethod', methods = ['POST'])
def postmethod():
  data=request.get_json()
  print (data)
  return jsonify(data)