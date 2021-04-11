import queue
import os
import time
import xlrd
import threading
from lib.log import MY_LOGGER as logger
import random

from config.config import USER_AGENTS, OS, BASE_DIR
from urllib.parse import urlparse
from lib.api_to_ip import Get_Api
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class conphantomjs:
    phantomjs_max = 1
    jiange = 0.00001
    timeout = 10
    executable_path = f'{BASE_DIR}/webdrive/{OS}/phantomjs'
    service_args = []
    service_args.append('--disk-cache=yes')
    service_args.append('--ssl-protocol=any')
    service_args.append('--web-security=false')
    service_args.append('--ignore-ssl-errors=true')


    def __init__(self):
        self.q_phantomjs = queue.Queue()


    def getbody(self, url, out_path, file_type='png'):
        d = self.q_phantomjs.get()
        if 'http' not in url:
            url = f"http://{url}"
        try:
            d.get(url)
            title = d.title
            if not title:
                out_file(f"{url}网页打开失败{title}", out_path)
            elif ("403" or "404" or "500") in title:
                out_file(f"{url}网页错误{title}", out_path)
            else:
                rep_str = '\ / : * ? " < > |'.split()
                for x in rep_str:
                    title = title.replace(x, '')
                title = title.strip()
                domain = urlparse(url).netloc
                logger.info(f"{domain}               访问成功！")
                d.save_screenshot(f"{out_path}/{title}-{domain}-{int(time.time())}.{file_type}")
        except:
            out_file(f"Phantomjs Open url Error:{url}", out_path)
        try:
            urls = d.current_url
        except:
            urls = ''
        d.get("about:blank")
        self.q_phantomjs.put(d)
        out_file(f"{url}*****{urls}", out_path)


    def open_phantomjs(self):

        def open_threading():
            cap = DesiredCapabilities.PHANTOMJS.copy()
            cap["phantomjs.page.settings.userAgent"] = random.choice(USER_AGENTS)
            d = webdriver.PhantomJS(executable_path=conphantomjs.executable_path,
                                    desired_capabilities=cap, service_args=conphantomjs.service_args)
            d.implicitly_wait(conphantomjs.timeout)
            d.set_page_load_timeout(conphantomjs.timeout)
            d.maximize_window()

            self.q_phantomjs.put(d)

        th = []
        for i in range(conphantomjs.phantomjs_max):
            t = threading.Thread(target=open_threading)
            th.append(t)
        for i in th:
            i.start()
            time.sleep(conphantomjs.jiange)
        for i in th:
            i.join()


    def close_phantomjs(self):
        th = []
        def close_threading():
            d = self.q_phantomjs.get()
            d.quit()

        for i in range(self.q_phantomjs.qsize()):
            t = threading.Thread(target=close_threading)
            th.append(t)
        for i in th:
            i.start()
        for i in th:
            i.join()


def red_api(file_path):
    api_list = []
    file_type = file_path.split('.')[-1]
    if file_type in ["xlsx", "xls"]:
        wb = xlrd.open_workbook(file_path)
        for sh in wb.sheets():
            for r in range(sh.nrows):
                api_list.append(sh.row(r))
    elif file_type in ["txt", "csv"]:
        with open(file_path) as f:
            for line in f:
                api_list.append(line)
    else:
        logger.warning("不支持文件类型")
    return api_list


def out_file(message, dir):
    file_name = f"{dir}/err.txt"
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(f"{message}\n")



def run_short(*args):
    keyword, input_file, out_path, file_type, *_ = args
    if input_file:
        api_list = red_api(os.path.abspath(input_file))
    else:
        api_list = Get_Api(keyword).run()
    date_time = int(time.time())
    out_path = os.path.abspath(f'{out_path}/{date_time}')
    is_dir(out_path)

    cur = conphantomjs()
    conphantomjs.phantomjs_max = 10
    cur.open_phantomjs()

    th = []
    for i in api_list:
        t = threading.Thread(target=cur.getbody, args=(i, out_path, file_type))
        th.append(t)
    for i in th:
        i.start()
    for i in th:
        i.join()

    cur.close_phantomjs()


def is_dir(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
