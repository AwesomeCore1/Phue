from flask import Flask, render_template, request, session, redirect

# ROUTER IMPORTS
from routers.auth import authRoute
from routers.lights import lightRoute

app = Flask(__name__)
app.secret_key = "menudocs"

# REGISTER ROUTERS
app.register_blueprint(authRoute, url_prefix="/auth")
app.register_blueprint(lightRoute, url_prefix="/api/")

@app.route('/', methods=["GET"])
def index_route():
	if session.get("user") != "rick":
		return redirect('/auth')

	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)

