import os
import redis
import simplejson

from flask import abort
from flask import Flask
from flask import render_template
from db.loaf import loaf_from_alias

r = redis.StrictRedis(host='127.0.0.1', charset="utf-8", decode_responses=True)

application = Flask(__name__)

@application.route('/loaf/<loaf_alias>')
def loaf(loaf_alias):
    return render_template(
        'loaf.html',
        loaf=loaf_from_alias(r, loaf_alias),
	images=_list_image_paths(loaf_alias)
    )

def _list_image_paths(loaf_alias):
    return [
        'images/{}/{}'.format(loaf_alias, file)
        for file in os.listdir('static/images/{}'.format(loaf_alias))
    ]

if __name__ == "__main__":
    application.run(host='0.0.0.0')
