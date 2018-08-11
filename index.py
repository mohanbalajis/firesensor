from flask import request
import email
@app.route('/data')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    data = request.args.get('data')
    email.message(data)
     
