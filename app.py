from os import name
import re
from flask import Flask, render_template, request

import price

app = Flask(__name__)

# [pPrice, kmsDriven, noOfOwners, carAge, diesel, petrol, individual, manual]

@app.route("/", methods = ["GET"])
def Home():
    return render_template("index.html")


@app.route("/predict", methods = ["POST"])
def predict():
    
    if request.method == "POST":
        showPrice = float(request.form['pPrice'])
        distance = int(request.form['kmsDriven'])
        owners = int(request.form['noOfOwners'])
        age = int(request.form['carAge'])
        dies = int(request.form['diesel'])
        pet = int(request.form['petrol'])
        individual = int(request.form['individual'])
        man = int(request.form['manual'])

        sell = price.price_prediction(showPrice, distance, owners, age, dies, pet, individual, man)
        if sell > 0:
            return render_template("index.html", selling_price = "You can sell the car at: Rs. {}Lakhs".format(sell))
        else:
            return render_template("index.html", selling_price = "Sorry! You cannot sell your car. :(")
    
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
