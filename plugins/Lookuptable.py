import logging
from yapsy.IPlugin import IPlugin
from modules.common.Downloads import Downloads
logger = logging.getLogger(__name__)

"""

"""
class Lookuptable(IPlugin):
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def process(self, conf, output, cmd_conf):
        self._logger.info("LookupTable step")
        # Todo: create the config
        #Downloads(output.prod_dir).exec(conf)