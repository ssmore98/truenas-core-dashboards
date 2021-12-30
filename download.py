#!/usr/bin/python3

import sys
import os
import requests
import glob
import json
import shutil
from pprint import pprint

server = "{0}:3000".format(sys.argv[1])
GDIR   = '{HOME}/.config/grafana'.format(HOME=os.getenv("HOME"))

uids = ['novl4l-ik']

with open("{0}/token".format(GDIR), "r") as fp:
    token = fp.read()
    token = token.strip()

grafana_headers = {"Authorization": "Bearer {0}".format(token),
    "Content-Type":"application/json"}

for uid in uids:
    url = "http://{0}".format(server)
    url = "{0}/api/dashboards/uid/{1}".format(url, uid)
    with requests.get(url, headers=grafana_headers, verify=False) as response:
        if response.ok:
            retval = response.json()
            filename = '{0}.json'.format(retval['dashboard']['title'])
            print('Saving {0}'.format(filename))
            with open(filename, "w") as fp:
                json.dump(retval['dashboard'], fp, indent=4)
            print('Saved {0}'.format(filename))
        else:
            print('Could not download dashboard {0}'.format(uid))
