from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/')
def test():
	return render_template('webUI.html')

#angle_start, angle_stop, n_angles, n_nodes, n_levels, num_samples, visc, speed, time
@app.route('/', methods=['POST', 'GET'])
def result():
	if request.method == 'POST':


	    angle_start = request.form['angle_start']
	    angle_stop = request.form['angle_stop']
	    n_angles = request.form['n_angles']
	    n_nodes = request.form['n_nodes']
	    num_samples = request.form['num_samples']
	    visc = request.form['visc']
	    speed = request.form['speed']
	    time = request.form['time']

	    #run get_flow_results and inputs

    	return render_template("result.html")



# @app.route('/file-downloads/')
# def file_downloads():
# 	try:
# 		return render_template('result.html')
# 	except Exception as e:
# 		return str(e)

# @app.route('/return-files/')
# def return_files_tut():
# 	try:
# 		return send_file('txt/python.jpg', attachment_filename='hej.png')
# 	except Exception as e:
# 		return str(e)


if __name__ == '__main__':
    app.run(debug = True)
