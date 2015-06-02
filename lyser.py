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
        # Assign the config
        self.config = conf
        # For each stat package definined in the config import it
        for stat in self.config['use_stats']:
            try:
                if self.config['debug']:
                    print stat
                self.stats[stat] = importlib.import_module("stats.{}".format(stat))
            except ImportError:
                if self.config['debug']:
                    print "import failed :["
                sys.exit(1)

        if self.config['debug']:
            print "lyser initialised successfully"

    def getAllStats(self, text):
        stat_dict = {}
        # For each of the stats packages loaded cycle through and get the details
        for key in self.stats:
            class_ = getattr(self.stats[key], key)
            instance = class_()
            stat_dict[key] = instance.process(text)

        return stat_dict

    def getStats(self, method, text):
        if self.config['debug']:
            print "/method/{} called".format(method)
        class_ = getattr(self.stats[method], method)
        instance = class_()
        return {method: instance.process(text)}