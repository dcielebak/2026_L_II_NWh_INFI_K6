from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import JSON, SUPPORTED, PLAIN
from flask import Response, request

moje_imie = "Daniel"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    output = output.lower()
    result = get_formatted(msg, moje_imie, output)
    if output == JSON:
        return Response(result, mimetype="application/json")
    return result


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
