from flask import Flask
from flask import request
import delta_encoding

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/compress", methods=['POST'])
def compress():
  try:
    data = request.get_data()
    
    return delta_encoding.encoding(data)
  except:
    return 400
  

@app.route("/decompress", methods=['POST'])
def decompress():
  data = request.get_data()
  return delta_encoding.decoding(data)

# curl -XPOST --data-binary @encoding_temp.txt 127.0.0.1:5000/decompress
# curl -XPOST --data-binary @decoding_temp.txt 127.0.0.1:5000/compress