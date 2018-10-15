# delta-encoding

### Installation
` pip install flask`


### Run delta encoding test
` python delta_encoding.py`


### Run the server
` FLASK_APP=main.py flask run `

` FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run ` with watcher


### cUrl examples
` curl -XPOST --data-binary @words_alpha.txt 127.0.0.1:5000/compress `

` curl -XPOST --data-binary @encoded_temp.txt 127.0.0.1:5000/decompress `