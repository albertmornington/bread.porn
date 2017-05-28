import redis
import simplejson
from flask import abort
from flask import Flask
from flask import render_template

r = redis.StrictRedis(host='127.0.0.1', charset="utf-8", decode_responses=True)

application = Flask(__name__)

@application.route('/loaf/<loaf_alias>')
def show_post(loaf_alias):
    return render_template('loaf.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')
