# -*- coding: utf-8 -*-

import os
import sys
ROOT = os.getcwd()
sys.path.append(ROOT)

from util import logger


if __name__ == "__main__":
    log = logger.Logger()
    try:
        print(10/0)
    except Exception:
        error = traceback.format_exc()
        log.error(message=error)
