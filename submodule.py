import json
from flask import Blueprint

submodule = Blueprint('submodule', __name__)
version = '0.0.1'

@submodule.route('/')
def default():
    global version
    returnDict = {
        'name': __name__,
        'version':version
    }
    return json.dumps(returnDict, indent=4, sort_keys=True)