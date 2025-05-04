
'''
  Copyright (C) 2025  Linked Ideal LLC.[https://linked-ideal.com/]
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, version 3.
 
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.
 
  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from logging import config
import yaml
#config.dictConfig(yaml.load(open("logging.yml", encoding="utf-8").read(), Loader=yaml.SafeLoader))
from importlib import resources
config.dictConfig(yaml.load(resources.read_text('ToposoidCommon', 'logging.yml'), Loader=yaml.SafeLoader))
import logging

class LogUtils():

    moduleName = ""
    LOG = None
    
    def __init__(self, moduleName):
        self.moduleName = moduleName        
        self.LOG = logging.getLogger(moduleName)

    def formatMessageForLogger(self, message:str, username:str) -> str:
        if message is None:
            return "\t" + username
        else:
            return message.replace("\n", "\\n").replace("\t", " ") + "\t" + username

    def info(self, s, transversalState):
        self.LOG.info(self.formatMessageForLogger(s, transversalState.userId))
    
    def warning(self, s, transversalState):
        self.LOG.warning(self.formatMessageForLogger(s, transversalState.userId))

    def error(self, s, transversalState):
        self.LOG.error(self.formatMessageForLogger(s, transversalState.userId))
        
    def debug(self, s, transversalState):
        self.LOG.debug(self.formatMessageForLogger(s, transversalState.userId))