from flask import Flask

app = Flask(__name__)

@app.route("/")    #app.route is the subpage you can define. Anything that comes after the "/" in a site name. e.g. (google.com/images) images is the app.route
def home():
    return ('This is a blank example web page made in Flask, Flask is a lighter weight version of something like Django which has databases and authentication, which Flask does not')

def user(name):
    return ":"

if __name__ == "__main__":
    app.run()