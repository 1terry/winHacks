from flask import Flask, render_template, request, redirect, url_for

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
    print(loc1 + loc2)
    
    # Pulling from the textbox and redirecting to a new screen.
    user = request.form["nm"]
    return redirect (url_for ("user", usr = user))
  else:

    # Otherwise we just load the start screen.
    return render_template("index.html")

# Testing to see if we can get to the user screen.
@app.route ("/<usr>")
def user(usr):
  return f"<h1>{usr}</h1>"

# Starting the server.
if __name__ == "__main__":
  app.run(debug=True)
