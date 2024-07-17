from flask import Flask
app = Flask(__name__)

@app.route("/") #registering the url
def hello_world(): #define the function which return the o/p
  return "Hello Jovian"

#to run
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)