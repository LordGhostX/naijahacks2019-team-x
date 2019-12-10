from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
@app.route("/index.html", methods=["POST", "GET"])
def index():
    form_type = request.form.get("formType", None)
    if form_type == "subscribe":
        email = request.form.get("email")
        add_subscriber(email)
        return render_template("index.html", subscribed=True)

    return render_template("index.html")

def add_subscriber(subscriber):
    open("lists/subscribers.txt", "a+").write(subscriber + "\n")

if __name__ == "__main__":
    app.run(debug=True)
