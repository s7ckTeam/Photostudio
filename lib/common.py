# /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import random
import requests
from config.config import USER_AGENTS


def getLatestRevision():
    """
    获取版本信息
    """
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
    }
    readVersion = None
    try:
        req = requests.get(
            url="http://tools.version.weapons.red/tools/Photostudio.txt", headers=headers)
        content = req.text
        readVersion = re.findall(
            "Version\s*=\s*[\"'](?P<result>[\d.]+)", content)
    except:
        pass

    return readVersion[0]

