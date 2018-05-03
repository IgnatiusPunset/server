
from flask import Flask
app=Flask(__name__)
@app.route('/')
def web_server1():
	return 'Web Server 1'
if __name__=="__main__":
	app.run(host='0.0.0.0',port=50000)

