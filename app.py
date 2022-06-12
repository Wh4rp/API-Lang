from flask import Flask, jsonify, request, render_template
from runners import PythonRunner, CppRunner

from flask_cors import CORS

app =  Flask(__name__)
CORS(app)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/ping', methods=['GET'])
def ping():
  return jsonify({"message": "Pong!"})

@app.route('/run/<string:language>/')
def createcm(language=None, code=None):
  code = request.args.get('code')
  datain = request.args.get('datain') or ""
  print(code)
  if language == 'python':
    response = jsonify(PythonRunner(code, datain=datain))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  if language == 'cpp':
    response = jsonify(CppRunner(code, datain=datain))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/runner', methods=['POST'])
def createcm_post():
  content = request.json
  print(content)
  try:
    language = content['language']
    code = content['code']
    datain = content['datain'] or ""
  except:
    return jsonify({"error": "Invalid JSON"})
  
  print("El codigo es: ", code)
  if language == 'python':
    response = jsonify(PythonRunner(code, decode=False, datain=datain))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  if language == 'cpp':
    response = jsonify(CppRunner(code, decode=False, datain=datain))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  return jsonify({"message": "No se encontro el lenguaje"})

if __name__ == '__main__':
  app.run(debug=True, port=4000)
