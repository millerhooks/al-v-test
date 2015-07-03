import urllib2
import json
import re
import calendar
import time

# test case: 69.43.161.174

class IPDetails(object):
    def __init__(self, *args, **kw):
        ip = args[0]
        self.address = ip
        self.is_tracked = False
        self.is_error = False

        # get raw data from
        # http://reputation.us.alienvault.com/panel/ip_json.php?ip=69.43.161.174

        # assign values to self

        return

class Reputation(object):
    @staticmethod
    def get_details(ip):
        if ip:
            try:
                url = "your-url-here" # go fetch the results from the source
                return urllib2.urlopen(url).read()
            except:
                return "fetch_error"
        else:
            return None