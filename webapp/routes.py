from flask import render_template, redirect, send_file, url_for, request, make_response
from webapp import app, css_load


@app.get("/")
def landing():
	return redirect(url_for("about"))


@app.get("/control")
def control():
	return render_template("control.html")


@app.get("/about")
def about():
	return render_template("about.html", debug=app.config['DEBUG'])


@app.get("/css/<page_name>")
def css(page_name):
	if app.config['ENV'] == "development":
		css_load()
	output_blob = app.css_cache[page_name[:-4]]
	response = make_response(output_blob)
	response.mimetype = "text/css"
	return response


@app.get('/img/<filename>')
def img(filename):
	return send_file("static/img/" + filename)
