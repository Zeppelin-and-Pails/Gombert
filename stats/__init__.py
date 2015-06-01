"""
Gombert stats package __init__

package for getting readability scored based on text characteristics

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""

import os
import yaml

DIR = os.path.dirname(os.path.realpath(__file__))
config = yaml.safe_load(open("{}/stats.cfg".format(DIR)))
__all__ = config["def_packs"]