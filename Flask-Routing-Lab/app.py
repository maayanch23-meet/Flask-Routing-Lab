from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route('/')
def home_html():
    return render_template("home.html")

@app.route('/botlles')
def bottles_html():
    return render_template("water.html")

@app.route('/shirts')
def shirts_html():
    return render_template("shirts.html")

@app.route('/milk')
def milk_html():
    return render_template("milk.html")

@app.route('/eggs')
def eggs_html():
    return render_template("eggs.html")

@app.route('/cart')
def cart_html():
    return render_template("cart.html")

# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
