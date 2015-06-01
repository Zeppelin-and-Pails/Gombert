"""
lyser

Get stats on a body of text based on analysis packages

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
__version__ = "1.1.1"

import importlib

class lyser:
    config = None
    stats  = {}

    def __init__(self, conf):
        self.config = conf
        for stat in self.config['use_stats']:
            try:
                print stat
                stats[stat] = importlib.import_module("stats.{}".format(stat))
            except ImportError:
                print ":["
                sys.exit(1)

        if self.config['debug']:
            print "lyser initialised successfully"

    def getAllStats(self, text):
        stat_dict = {}

        for key in stats:
            stat_dict[key] = stats[key].getStats(text)

        return stat_dict

    def getStats(self, method, text):
        return method * text