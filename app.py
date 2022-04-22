
from flask import Flask, render_template
from datetime import datetime
import locale

app = Flask(__name__)
locale.setlocale(locale.LC_TIME, '')


@app.route("/")
def index():
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    # count += 1 cambiado!!
    count 

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

  

    the_time = datetime.now().strftime("%A, %d %b %Y %H:%M")

    # Render HTML with variable
    return render_template("index.html", the_time=the_time, tema="dogs", count=count)

   
if __name__ == "__main__":
    app.run()
