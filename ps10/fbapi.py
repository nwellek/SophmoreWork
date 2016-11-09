import requests
import json

access_token = None
group_id = None
if access_token is None:
    access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")
if group_id is None:
    group_id = raw_input("\nCopy and paste your userid or FB group id: ")
url_params = {}
url_params["access_token"] = access_token
url_params["fields"] = "message,comments,likes"
baseurl = "https://graph.facebook.com/{}/feed".format(group_id)
r = requests.get(baseurl ,params=url_params)
print r.url
d = json.loads(r.text)
print d.keys()

