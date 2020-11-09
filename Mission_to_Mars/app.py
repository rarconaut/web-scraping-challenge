from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mission_to_mars
scrape_mars = db.scrape_mars


@app.route("/scrape")
def scrape():
    # write a statement that finds all the items in the db and sets it to a variable
    items = list(scrape_mars.find())
    print(items)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)
