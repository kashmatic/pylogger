import os
import logging

logging.basicConfig(format="%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s:%(message)s")
LEVEL = logging.getLevelName(os.environ.get('LOGLEVEL').upper()) if 'LOGLEVEL' in os.environ else 'ERROR'
logging.getLogger().setLevel(LEVEL)
