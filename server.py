
from flask import Flask
app=Flask(__name__)
@app.route('/')
def web_server1():
	return 'Web Server 1'
if __name__=="__main__":
	app.run(host='192.168.24.133',port=5000)

