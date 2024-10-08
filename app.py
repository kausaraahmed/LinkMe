from flask import Flask, render_template, redirect
from database import linkme_db
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<short_url>")
def redirect_to_user_url(short_url):
    link = linkme_db.get(short_url)

    if link:
        return redirect(link)
    else:
        return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)
