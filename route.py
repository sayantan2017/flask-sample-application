from flask import Flask 
  
app = Flask(__name__) 
  
# Pass the required route to the decorator. 
@app.route("/Sayantan") 
def hello(): 
    return "Hello, Welcome to Sayantan's Home"
    
@app.route("/") 
def index(): 
    return "Homepage of Python"
  
if __name__ == "__main__": 
    app.run(debug=True) 