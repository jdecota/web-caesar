from flask import Flask, request            
from caesar import rotate_string                                                 
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/" method="POST"style="width: auto; overflow: hidden;">
            <label>
                Rotate by:
                <input type="text" name="rot" value="0" />
            </label>
            <br>
        <textarea name="text">{0}</textarea>
        <br>
        <input type="submit" value="Submit Query"/>
    </body>
</html>
"""
@app.route("/", methods=["POST"])
def encrypt():
    lrot = int(request.form["rot"])
    ltext = request.form["text"]
    return form.format(rotate_string(ltext, lrot))

@app.route("/")
def index():
    # if we have an error, make a <p> to display it
    error = request.args.get("error")
    if error:
        error_esc = cgi.escape(error, quote=True)
        error_element = '<p class="error">' + error_esc + '</p>'
    else:
        error_element = ''

    # build the response string
    content = form.format('')

    return content

app.run()                                               #Passes control to Flask object to run