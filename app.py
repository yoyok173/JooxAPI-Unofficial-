import src

from flask import Flask,request,jsonify,json

joox = src.Object()
app = Flask(__name__)

@app.route('/',methods=['GET'])
def get_home():
	return ("Berhasil")

@app.route('/api/joox/search',methods=['GET'])
def get_searchResults():
	if 'q' in request.args:
		results = joox.searchResults(keywords=request.args.get('q'))
		return jsonify({"results":results, "status":200})

@app.route('/api/joox/songid',methods=['GET'])
def get_songinfoResults():
	if 'q' in request.args:
		results  = joox.songinfoResults(songid=request.args.get('q'))
		return jsonify({"results":results, "status":200})

@app.route('/api/gimage/search',methods=['GET'])
def get_gimageResults():
	if 'q' in request.args:
		result = joox.gooogleimage(keywords=request.args.get('q'))
		return json.dumps(result, indent=4, sort_keys=False)
    
if __name__ == "__main__":
	app.run(debug=True)
