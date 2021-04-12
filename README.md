* ## Photostudio-红队快速爬取网页快照工具
  
  
  
  ## 一、简介：
  
  ###### 正如其名：这是一款能进行自动化检测,实时给网页拍照的工具
  
  信息收集要求所收集到的信息要真实可靠。
  
  当然，这个原则是信息收集工作的最基本的要求。为达到这样的要求，信息收集者就必须对收集到的信息反复核实，不断检验，力求把误差减少到最低限度。我们经常面临条件下不同的网络、资产、框架、进行信息收集 每次我们都面临不得不解决的新挑战，而收集资产状态是最繁琐的一种，工具和脚本来让我们的工作变得更加轻松，由于每个人都有每个人收集的方式和方法，但愿我们这款工具可以帮助您更轻快的完成工作。
  
  Photostudio是一款能进行自动化检测网页存活并实时给网页拍照的工具，通过调用Fofa/Zoomeye/360qua/shodan等 Api快速准确查询资产并进行网页截图，从而实施进一步的信息筛查。
  
  适应场景：内外网资产梳理快照
  
  #### 功能点
  
  - 批量检测url
  
  - 自动化检测url存活，拍照截图
  
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
  
  	git clone https://github.com/s7ckTeam/Photostudio
  	cd Photostudio
  	pip3 install -r requirements.txt
  
  ## 二、使用方法：
  
  ```
  Usage: python3 Photostudio.py --fofa title="admin"
  Usage: python3 Photostudio.py -f api.txt
  Usage: python3 Photostudio.py --fofa/-f title="admin"/api.txt -o imgs
  Usage: python3 Photostudio.py --fofa/-f title="admin"/api.txt -t png
  
  
  usage: Photostudio.py [-h] [-fofa QUERY] [-f FILE] [-o OUTPATH] [-t FILETYPE]
  
  
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
  
  ## 三、效果：
  
  ##### 1、python3 Photostudio.py --fofa title="admin"
  
  ![image.png](https://i.loli.net/2021/04/12/nc4ZXmU8DhkrGly.png)
  
  ##### 2、保存路径
  
  ![image.png](https://i.loli.net/2021/04/12/t5nz7UvABkpaIde.png)
  
  ## 四、特别感谢
  
  冰海
  
  狗一样的男人
  
  s7ck Team
  
  ## 五、文末
  
  红队武器库，我们在一线
  
  商务/投稿/加入团队：s7ck@qq.com
  
  
