import logging
import os
import json


MYDIR = os.path.join(os.getenv("BASE_DIR"),"log")
CHECK_FOLDER = os.path.isdir(MYDIR)
if not CHECK_FOLDER:
    os.makedirs(MYDIR)
    # os.system(f"sudo mkdir {MYDIR}")

def getLoggerInstance(name,fileName):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(
        os.path.join(os.getenv("BASE_DIR"),"log",fileName),"w"
    )
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

AppLogger = getLoggerInstance("application","app.log")
SqlLogger = getLoggerInstance("sql","sql.log")
