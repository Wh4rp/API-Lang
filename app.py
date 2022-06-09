from flask import Flask, jsonify, request
from runners import PythonRunner, CppRunner

app =  Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
  return jsonify({"message": "Pong!"})

@app.route('/run/<string:language>/')
def createcm(language=None, code=None):
  code = request.args.get('code')
  datain = request.args.get('datain') or ""
  print(code)
  if language == 'python':
    status = PythonRunner(code, datain=datain)
    return jsonify(status)
  if language == 'cpp':
    status = CppRunner(code, datain=datain)
    return jsonify(status)

if __name__ == '__main__':
  app.run(debug=True, port=4000)
