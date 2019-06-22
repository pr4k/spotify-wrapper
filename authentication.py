API_TUTOR_TOKEN = 'API_TUTOR_API_KEY'

import urllib.request
from urllib.request import urlopen
import json

def get_token(url):

    url += '?auth_manager_token=' + API_TUTOR_TOKEN
    try:
        results = urlopen(url).read().decode('utf-8', 'ignore')
        # print(results)
        return json.loads(results)['token']
    except urllib.error.HTTPError as e:
        error_code = e
        msg = e.read().decode('utf-8', 'ignore')
        msg_object = json.loads(msg)
        error_detail = msg_object.get('error')
        raise Exception(str(error_code) + '\n' + error_detail)