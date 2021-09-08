from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_navigation import Navigation
from flask_cors import CORS
import json
# from webapp.scripts import test_script, key_64
import datetime
# import socket
from scss.compiler import compile_string

app = Flask(__name__)
app.config.update(
	ENV='development',
	DEBUG=True
)


def css_load():
	app.css_cache = {}
	css_file_map = {
		"about": ["about"]
	}
	for page, files in css_file_map.items():
		app.css_cache[page] = ""
		page_css = []
		for file in files:
			filepath = str("webapp/static/scss/" + file + ".scss")  # .replace("\\", "/")
			with open(filepath, "r") as contents:
				scss = contents.read()
			page_css.append(compile_string(scss))
		app.css_cache[page] = "\n".join(page_css)


app.css_cache = {}
css_load()

from webapp import routes
