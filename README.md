# esjspy
用于 esjzone 的 python 爬虫。可以抓取 esjzone 的大部分小说并生成 epub 文件。

## Install 
```
git clone https://github.com/Dothion/esjspy
cd esjspy
```

## Requirements
[![requests_html](https://img.shields.io/pypi/v/EbookLib.svg?label=EbookLib)](https://pypi.org/project/EbookLib/)
[![requests_html](https://img.shields.io/pypi/v/chardet.svg?label=chardet)](https://pypi.org/project/chardet/)
[![requests_html](https://img.shields.io/pypi/v/lxml.svg?label=lxml)](https://pypi.org/project/lxml/)
[![requests_html](https://img.shields.io/pypi/v/aiohttp.svg?label=aiohttp)](https://pypi.org/project/aiohttp/)
[![requests_html](https://img.shields.io/pypi/v/opencc-python-reimplemented.svg?label=opencc-python-reimplemented)](https://pypi.org/project/opencc-python-reimplemented/)


## Usage 
(need python>=3.7)

##### 一次性抓取全部轻小说
```python
import esjspy
esjspy.save_books()
```

##### 抓取单本轻小说
```python
import esjspy
esjspy.save_book(book_url='https://www.esjzone.cc/detail/1563843171.html')
```
##### 抓取选项
```python
import esjspy
esjspy.save_book(
    book_url='https://www.esjzone.cc/detail/1563843171.html',
    language='zh-CN',
    save_dir='./books/',
    proxies={'http':'http://127.0.0.1:8080'})
```

## Todo
- 现在的 settings.py 是写在包里面的，之后的更新会分离出来。
- 完善注释和文档
- 增加其他网站 (qinxiaoshuo、真白萌, etc.) 的支持

## Attention
为了减少 esjzone 站点无谓的流量和服务器资源消耗，请尽可能减少本模块的使用。如果你不是整合君，请最好不要使用本模块。