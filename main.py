from flask import Flask, render_template, request

from model import Wheel

app = Flask(__name__)

@app.route("/")
def MainPage() -> str:
    return render_template("entry.html", 
                           the_title = "Добро пожаловать в калькулятор диаметра шины")

@app.route("/count", methods = ["POST"])
def CountDiameter() -> str:
    width = request.form["width"]
    percent = request.form["percent"]
    discDiameter = request.form["discDiameter"]
    return render_template("results.html", 
                           the_title = "Результаты вычисления",
                           the_options = width + " / " + percent + " R " + discDiameter,
                           the_result = Wheel.CountDiameter(float(width), float(percent), float(discDiameter)))

app.run()