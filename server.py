from flask import Flask, render_template, request, url_for
import os
IGNA_FOLDER=os.path.join('server','static')
app=Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER']=IGNA_FOLDER
@app.route('/')
@app.route('/index', methods=['GET'])
def show_index():
	full_filename=os.path.join(app.config['UPLOAD_FOLDER'], 'igna.jpg')
	return render_template("index.html",user_image=full_filename)
if __name__=="__main__"
	app.run(host='192.168.45.128',port=5000)
#def web_server1():
#	return 'Web Server 1'
#if __name__=="__main__":
#	app.run(host='192.168.24.133',port=5000)

