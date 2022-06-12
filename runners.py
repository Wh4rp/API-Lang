import subprocess
from encode import base64_encode, base64_decode

def dict_status(status):
  """
  This function converts the status to a dictionary
  """
  return {
    'exit status':status.returncode,
    'result':status.stdout.decode(),
    'stderr':status.stderr.decode()
  }

def PythonRunner(code, decode=True, datain=None):
  """
  This function runs the python Code
  """
  if decode:
    code = base64_decode(code).decode('utf-8')
    if datain:
      datain = base64_decode(datain).decode('utf-8')
  
  with open("tmp/python.py", "w+") as f:
    f.write(code)

  status = subprocess.run(["python3", 'tmp/python.py'], input=datain.encode(), capture_output=True)

  return dict_status(status)

def CppRunner(code, decode=True, datain=None):
  """
  This function runs the C++ Code
  """
  if decode:
    code = base64_decode(code).decode('utf-8')
  if datain:
    datain = base64_decode(datain).decode('utf-8')
  
  with open("tmp/cpp.cpp", "w+") as f:
    f.write(code)

  status = subprocess.run(["g++", 'tmp/cpp.cpp', '-o', 'tmp/cpp.out'], capture_output=True)

  if status.returncode != 0:
    return dict_status(status)

  status = subprocess.run(["tmp/cpp.out"], input=datain.encode(), capture_output=True)

  return dict_status(status)