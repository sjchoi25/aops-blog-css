from random import choice
import urllib.parse
from datetime import datetime

from flask import Flask, make_response, request, redirect, render_template

files = {
	"circuit.css": "5.2vw",
	"cloud.css": "50px",
	"blue.css": "5vw"
}

app = Flask(__name__)

def getcss(filename):
	importLink = urllib.parse.urljoin("https://Nhv24.github.io/aops-blog-css/", filename)

	newcss = "@import url(\"" + importLink + '");\n' + """#header h1 {
    font-size: 0 !important;
}

#header h1:after {
    content: \""""+filename+"""\";
    font-size: """+files[filename]+""";
}"""
	return newcss

def retrive(filename, inserts):
	"""
	Get the css from the file and insert
	"""
	with open(filename) as file:
		return file.read().replace("<INSERT>", inserts)

# ----------------------------------
#     Helper functions
# ----------------------------------
def ishexclr(clr):
	"""
	Return true if clr is hex, false otherwise
	"""
	# Check if the color is hex with a simple try/except statement
	try:
		# Check if its hex
		int(clr, 16)
		return True
	except ValueError:
		# Not hex
		return False

@app.route("/")
def index():
	"""
	Index view
	"""
	# Redirect to the Fire-css official website
	return redirect("https://Fire-css.github.io")


# ----------------------------------
#     Files
# ----------------------------------
@app.route('/font.css')
def return_font_css():
	"""
	Return the font css according to the url parameters
	"""
	# Get the family url parameter
	font = request.args.get("family", default="")

	# Create the css from the url parameter
	output = retrive("font.css", font)

	# Check for proper usage of css
	if font == "":
		# Make the output nothing
		output = ""

	res = make_response(output)
	res.mimetype = 'text/css'
	return res

@app.route("/blink.css")
def return_blink_css():
	"""
	Return the blink css according to the url parameters
	"""
	# Get the clr and hex url parameter
	clr = request.args.get("clr", default="")

	# Check if color is hex
	if ishexclr(clr):
		# Color is hex
		clr = f"#{clr}"

	# Create the css from the url parameter
	output = retrive("blink.css", clr)
	# Check for proper usage of css
	if clr == "":
		# Make the output nothing
		output = ""

	res = make_response(output)
	res.mimetype = 'text/css'
	return res

@app.route("/typewriter.css")
def return_type_css():
	"""
	Return the typewriter css
	"""
	# Get the clr and hex url parameter
	clr = request.args.get("clr", default="")

	# Check if color is hex
	if ishexclr(clr):
		# Color is hex
		clr = f"#{clr}"

	output = retrive("typewrite.css", clr)
	# Check for proper usage of css
	if clr == "":
		# Make the output nothing
		output = ""

	res = make_response(output)
	res.mimetype = 'text/css'
	return res

# ----------------------------------
#     Help page
# ----------------------------------
@app.route("/help")
def helppage():
	"""
	Displays a help page
	"""
	# Descriptions
	descriptions = {
		"/blink.css": ": Returns css for blinking header. Parameters: clr (the color or the cursor), hex (either true or false, determines if clr is hex or not",
		"/font.css": ": Returns css for blog font. Parameters: family (the font family)"
	}

	# Render help.html
	return render_template("help.html", 
		dirs = descriptions
	)

@app.route("/random.css")
def return_css():
	"""
	Return a random css file
	"""
	res = make_response(getcss(choice(list(files.keys()))))
	res.mimetype = "text/css"

	return res

@app.route("/april-fools.css")
def return_april_css():
	"""
	Return a special April fools css file
	"""
	date = datetime.now()

	if date.day == 1 and date.month == 4:
		with open("april-fools.css") as file:
			res = make_response(file.read())
			res.mimetype = 'text/css'
			return res
	return ""

@app.route("/wakeup")
def wake():
	print("\n\n\n\nThis page was requested\n\n\n\n")
	return ""

app.run(host='0.0.0.0', port=8080)