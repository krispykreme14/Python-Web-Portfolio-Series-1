import projects #projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
  return render_template("home.html", projects=projects.setup())

#connects /hello path of server to render hello.html
@app.route('/comediansdecades/')
def comediansdecades_route():
  return render_template("comediansdecades.html", projects=projects.setup())

#connects /historyofcomedy path of server to render historyofcomedy.html
@app.route('/historyofcomedy/')
def historyofcomedy_route():
  return render_template("historyofcomedy.html", projects=projects.setup())

@app.route("/playground")
def playground_route():
  return render_template("playground.html")

if __name__ == "__main__":
  #runs the application on the repl development server
  app.run(port='3000', host='0.0.0.0')