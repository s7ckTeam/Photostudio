# 网页快照

### 开发语言

* Python3

### 运行环境

* Linux
* Windows
* Mac

### 使用依赖库

* requests
* selenium==2.48.0
* colorama
* xlrd


### 安装
	git clone [url]
	cd [dir]
	pip3 install -r requirements.txt

## 三、使用方法：

```
Usage: python3 {parser.prog} --fofa title="admin"
Usage: python3 {parser.prog} -f api.txt
Usage: python3 {parser.prog} --fofa/-f title="admin"/api.txt -o imgs
Usage: python3 {parser.prog} --fofa/-f title="admin"/api.txt -t png


usage: main.py [-h] [-fofa QUERY] [-f FILE] [-o OUTPATH] [-t FILETYPE]


optional arguments:
  -h, --help            show this help message and exit
  -fofa QUERY, --fofa QUERY
                        Input your api query.
  -f FILE, --file FILE  Input your api.txt.
  -o OUTPATH, --outPath OUTPATH
                        Input your outPath.
  -t FILETYPE, --fileType FILETYPE
                        Input your fileType png/jpg...
```
#### 相关配置更改

* API设置
  
  在`config/config.py`中`fofaApi`设置，输入对应的`email`与`key`即可
