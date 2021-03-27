from flask import Flask, render_template, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
  return render_template("index.html") 

@app.route('/index', methods =["POST", "GET"])
def getInfo():
  if request.method == "POST":
    loc1 = request.form["start"]    #make name start in field
    loc2 = request.form["end"]      #make name end in field

if __name__ == "__main__":
  app.run(debug=True)
