from flask import Flask, render_template, request, session, redirect

# ROUTER IMPORTS
from routers.auth import auth_route
from routers.lights import light_route

app = Flask(__name__)
app.secret_key = "ricksite"

# REGISTER ROUTERS
app.register_blueprint(auth_route, url_prefix="/auth")
app.register_blueprint(light_route, url_prefix="/api/")

@app.route('/', methods=["GET"])
def index_route():
	if session.get("user") != "rick":
		return redirect('/auth')

	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)
