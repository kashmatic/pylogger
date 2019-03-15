"""
Set up logger
"""

import os
import logging

logging.basicConfig(
    format="%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s:%(message)s"
)
if 'LOGLEVEL' in os.environ:
    LEVEL = logging.getLevelName(os.environ.get('LOGLEVEL').upper())
else:
    LEVEL = logging.getLevelName('ERROR')

logging.getLogger().setLevel(LEVEL)
