from flask import Flask, request, abort
import delta_encoding

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/compress", methods=['POST'])
def compress():
  try:
    data = request.get_data()
    return delta_encoding.encoding(data), 200, {'Content-Type': 'text/plain'}
  except:
    abort(400)
  

@app.route("/decompress", methods=['POST'])
def decompress():
  try:
    data = request.get_data()
    return delta_encoding.decoding(data), 200, {'Content-Type': 'text/plain'}
  except:
    abort(400)

# curl -XPOST --data-binary @encoded_temp.txt 127.0.0.1:5000/decompress
# curl -XPOST --data-binary @temp.txt 127.0.0.1:5000/compress