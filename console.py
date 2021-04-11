# /usr/bin/env python
# -*- coding: utf-8 -*-
import random
import argparse
from lib.log import MY_LOGGER as logger
from config.config import pyVersion, seleVersion, Version, Banner
from script.page_img_pool import run_short
from lib.update import update



def version_check():
    if pyVersion < "3.6":
        logger.error(
            f"此Python版本 ('{pyVersion}') 不兼容,成功运行Screenshot你必须使用版本 >= 3.6 (访问 ‘https://www.python.org/downloads/’)")
        exit(0)
    if seleVersion > "2.48.0":
        logger.error(f"selenium库版本 ('{seleVersion}') 不兼容，2.48.0之后不支持PhantomJS")
        logger.info('运行 (python3 -m pip install -U "selenium==2.48.0") 进行库降低版本')
        logger.info(
            "或者运行 (python3 -m pip install -r requirements.txt) 进行全部库的安装")
        exit(0)


def args_check(cmdparse, usage):
    print(random.choice(Banner))
    confs = {}
    args = []
    if hasattr(cmdparse, "items"):
        cmdlines = cmdparse.items()
    else:
        cmdlines = cmdparse.__dict__.items()
    for key, value in cmdlines:
        confs[key] = value
        args.append(value)
    if confs['version']:
        logger.info(f"Version: {Version}")
        exit(0)
    if confs['updateprogram']:
        update()
        exit(0)
    if not confs['query'] and not confs['file']:
        print(usage)
        exit(0)
    return args


def main():
    version_check()
    parser = argparse.ArgumentParser(description="Screenshot.")
    parser.add_argument('-fofa', '--fofa', type=str,
                        dest='query', help='Input your api query.')
    parser.add_argument('-f', '--file', type=str,
                        dest='file', help='Input your api.txt.')
    parser.add_argument('-o', '--outPath', type=str, default='result',
                        dest='outPath', help='Input your outPath.')
    parser.add_argument('-t', '--fileType', type=str, default='png',
                        dest='fileType', help='Input your fileType png/jpg...')
    parser.add_argument('-v', '--version', dest='version',
                        action='store_true', help="Show program's version number and exit.")
    parser.add_argument('--update', dest='updateprogram',
                        action='store_true', help="Update the program.")
    args = parser.parse_args()
    usage = f'''
Usage: python3 {parser.prog} --fofa www.baidu.com
Usage: python3 {parser.prog} -f api.txt
Usage: python3 {parser.prog} --fofa/-f www.baidu.com/api.txt -o imgs
Usage: python3 {parser.prog} --fofa/-f www.baidu.com/api.txt -t png
    '''
    args = args_check(args, usage)
    run_short(*args)
