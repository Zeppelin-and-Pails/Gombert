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
                if self.config['debug']:
                    print stat
                self.stats[stat] = importlib.import_module("stats.{}".format(stat))
            except ImportError:
                if self.config['debug']:
                    print ":["
                sys.exit(1)

        if self.config['debug']:
            print "lyser initialised successfully"

    def getAllStats(self, text):
        stat_dict = {}

        for key in self.stats:
            if self.config['debug']:
                print "key - {} \n".format(self.stats[key])
            class_ = getattr(self.stats[key], key)
            instance = class_()
            stat_dict[key] = instance.process(text)

        return stat_dict

    def getStats(self, method, text):
        return {method: self.stats[method].process(text)}