# !/usr/bin/python
# coding: utf-8
import json
import base64
import random
from lib.log import MY_LOGGER as logger
import requests
from requests.adapters import HTTPAdapter

from config.config import fofaApi, USER_AGENTS


class Get_Api():

    def __init__(self, ip):
        super(Get_Api, self).__init__()
        self.email = fofaApi['email']
        self.key = fofaApi['key']
        self.headers = {
            "Cache-Control": "max-age=0",
            "User-Agent": random.choice(USER_AGENTS),
            "Upgrade-Insecure-Requests": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        }
        self.ip = ip

    def run(self):
        keywordsBs = base64.b64encode(self.ip.encode('utf-8'))
        keywordsBs = keywordsBs.decode('utf-8')
        try:
            req = requests.Session()
            req.keep_alive = False
            datas = self.get_data(req, keywordsBs)
            domain_data = list({x[0] for x in datas['results']}) if datas else []
            if not domain_data:
                logger.info('获取到的数据为空！')
                exit(0)
            size = len(domain_data)
            data = input(f"获取到 {size} 条数据, 请输入您要截屏的数目：")
            try:
                data = int(data)
            except:
                logger.warning('输入不合法')
                exit(0)
            return domain_data[:data]

        except Exception as e:
            logger.error(e)
            return []


    def get_data(self, req, keywordsBs):
        url = f"https://fofa.so/api/v1/search/all?email={self.email}&key={self.key}&qbase64={keywordsBs}&size=10000"
        try:
            req.headers = self.headers
            req.mount("https://", HTTPAdapter(max_retries=2))
            target = req.get(url, timeout=10)
            datas = json.loads(target.text)
            return datas
        except Exception as e:
            logger.error(e)
            return {}