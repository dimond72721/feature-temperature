

app = Flask(temperature)

@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    celsius = None
    fahrenheit = None

    if request.method == "POST":
        celsius = float(request.form["celsius"])
        fahrenheit = celsius * 9 / 5 + 32

    return render_template(
        "temperature.html",
        celsius=celsius,
        fahrenheit=fahrenheit
    )

if __name__ == "__main__":
    app.run(debug=True)
