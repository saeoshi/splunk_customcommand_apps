#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import app
import os,sys
import time
import urllib2
import json

splunkhome = os.environ['SPLUNK_HOME']
sys.path.append(os.path.join(splunkhome, 'etc', 'apps', 'searchcommands_app', 'lib'))
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators
from splunklib import six
from splunklib.six.moves import range

@Configuration()
class RestCallCommand(GeneratingCommand):

    yid = Option(require=True)

    def generate(self):
	yid = self.yid
    	req = urllib2.Request('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s' % yid)
    	response = urllib2.urlopen(req)
    	weatraw = response.read()
    	weatjson = json.loads(weatraw)
   	print(json.dumps(weatjson,indent=2))
	yield {'_time': time.time(), 'event_no': 1, '_raw': weatjson}

dispatch(RestCallCommand, sys.argv, sys.stdin, sys.stdout, __name__)
