from flask import Flask, make_response, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
	# Redirect to the Fire-css official website
	return redirect("https://Fire-css.github.io")

@app.route('/font.css')
def return_font_css():
	"""
	Return the font css according to the url parameters
	"""
	# Get the family url parameter
	font = request.args.get("family", default="")

	# Create the css from the url parameter
	output = """/* THIS IS AN AUTO GENERATED FILE FROM https://Fire-css.player010.repl.co/font.css */

@import url('https://fonts.googleapis.com/css2?family="""+"+".join(font.split())+"""&display=swap');
    
/**   Font  **/
/* Credits to pog */
body, #header h1, .btn-primary, #navigation_box a, 
.inputbox, input.button2, .cmty-post-textarea, 
.cmty-subject-input, .cmty-items-input.ui-autocomplete-input, 
div.cmty-item-tag, button.btn.btn-run, button.btn.btn-reset,
button.btn.btn-link.btn-pop, div.cmty-topic-cell-post, 
div.cmty-topic-cell-subtitle, 
span.cmty-color-main.cmty-topic-cell-username, 
div.cmty-topic-cell-subject, div.cmty-topic-watchers, 
div.cmty-topic-cell-left-bottom, div.cmty-topic-cell-source, 
div.cmty-topic-cell-second-row, select, 
input#login-username.form-control, 
input#login-password.form-control, button#login-cancel-button.btn, 
div.cmty-topic-subject, input.cmty-submit-button.btn.btn-primary, 
textarea {
    font-family: '"""+font+"""';
    letter-spacing: 0.8px; 
    word-spacing: 1.6px;
    font-size: 16px;
}
.cmty-reply-window input.cmty-submit-button.btn.btn-primary {
    font-size: 12px;
}"""
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
	# Get the family url parameter
	clr = request.args.get("clr", default="")
	ishex = request.args.get("hex", default="")

	# Check if the color is hex with a simple try/except statement
	if ishex.lower() == 'true':
		try:
			# Check if its hex
			int(clr, 16)
			clr = f"#{clr}"
		except ValueError:
			# Not hex
			return "ERROR: Value is not hex color"

	# Create the css from the url parameter
	output = """/* This is an auto-generated file */
/* DO NOT REMOVE THE COMMENT ABOVE */
@keyframes blink {
    from, to {
        color: transparent;
    }
    50% {
    	color: """+clr+""";
    }
}
#header h1:after {
    content: "_";
    -webkit-animation: 1s blink step-end infinite;
    -moz-animation: 1s blink step-end infinite;
    -ms-animation: 1s blink step-end infinite;
    -o-animation: 1s blink step-end infinite;
    animation: 1s blink step-end infinite;
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
    text-decoration: none;
}	
"""
	# Check for proper usage of css
	if clr == "":
		# Make the output nothing
		output = ""

	res = make_response(output)
	res.mimetype = 'text/css'
	return res

app.run(host='0.0.0.0', port=8080)
