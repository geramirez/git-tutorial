from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/Kwame")
def Qat():
    return "Hello, World KwameB!"

@app.route("/chuck")
def chuck():
    return "Hello, Chuck!"

@app.route("/Kizzie")
def Kizzie():
	return "Hello, Kizzie!"
	
@app.route("/franklin")
def franklin():
    return "Hello, Franklin!"

if __name__ == "__main__":
    app.run()

