from flask import Flask, request, render_template, redirect, url_for
from json import load, dumps
import os

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
@app.route("/index.html", methods=["POST", "GET"])
def index():
    form_type = request.form.get("formType", None)
    if form_type == "subscribe":
        email = request.form.get("email")
        add_subscriber(email)

        return render_template("index.html", subscribed=True)

    if form_type == "message":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        add_message(name, email, subject, message)

        return render_template("index.html", message=True)

    return render_template("index.html")

def check_list():
    if not os.path.exists("lists/contact-list.json"):
        contact_list = {"subscribers": [], "messages": []}
        open("lists/contact-list.json", "w").write(dumps(contact_list))

def read_list():
    with open("lists/contact-list.json") as list:
        contact_list = load(list)
    return contact_list

def write_list(data):
    open("lists/contact-list.json", "w").write(dumps(data, indent=4))

def add_subscriber(subscriber):
    check_list()

    contact_list = read_list()
    contact_list["subscribers"].append(subscriber)
    write_list(contact_list)

def add_message(name, email, subject, message):
    check_list()

    contact_list = read_list()
    contact_list["messages"].append({"name": name, "email": email, "subject": subject, "message": message})
    write_list(contact_list)


if __name__ == "__main__":
    app.run(debug=True)
