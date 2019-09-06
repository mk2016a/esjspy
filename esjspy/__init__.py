#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/31 18:27 
# @Author : Dothion
# @File : __init__.py 
# @Software: PyCharm

from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Optional, List, Dict, Union

import esjspy.base
from esjspy.settings import *


def build_book_list(proxies: Optional[Dict[str, str]] = PROXIES, black_list=BLACK_LIST, max_page=MAX_PAGES,
                    xpath_dict: Dict[str, str] = XPATH_DICT, cool_down=COOL_DOWN, max_retries=MAX_RETRIES) -> None:
    """
    批量抓取轻小说。

    :param black_list: 黑名单。妥善设置黑名单可以有效减少抓取时间。
        ex:
        ["https://www.esjzone.cc/detail/1552057167.html",  # 去了异世界后能够复制技能了
         "https://www.esjzone.cc/detail/1548502021.html",  # 二转大叔]

    :param max_page: 最大抓取页数。

    :param proxies: 所用的代理。目前 aiohttp 只支持 http 代理。
        ex:
        {'http':'http://127.0.0.1:8080'}
    :param xpath_dict: 所用的 xpath 表达式的集合。请在阅读全部源码后妥善更改。

    :param cool_down: 连接断开后，重新连接时的冷却时间 (s)。

    :param max_retries: 重新连接的最大尝试次数。
    :return: 批量抓取和保存轻小说。无法抓取的部分会在 missing.txt, black_list.log 和 black_list.txt 中列出。
             black_list.log 中不会保存因章节过少而无法抓取的轻小说。
    """
    if isinstance(black_list, list) or isinstance(black_list, tuple):
        black_list = set(black_list)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        esjspy.base.async_build_book_list(proxies=proxies, black_list=black_list, max_page=max_page,
                                          xpath_dict=xpath_dict, cool_down=cool_down, max_retries=max_retries))


def save_book(book_url: str, use_cache=True, language: str = LANGUAGE, style: str = DEFAULT_CSS,
              save_dir: Union[Path, str] = Path(SAVE_DIR), cache_dir: Union[Path, str] = Path(CACHE_DIR),
              proxies: Optional[Dict[str, str]] = PROXIES, xpath_dict: Dict[str, str] = XPATH_DICT,
              cool_down: int = COOL_DOWN, max_retries: int = MAX_RETRIES) -> None:
    """
    批量抓取轻小说。

    :param book_url: 待抓取图书的 Url。
        ex:
        'https://www.esjzone.cc/detail/1563843171.html'

    :param use_cache: 是否使用缓存文件。封面和所有的章节会被缓存。

    :param language: 语言。在 'zh-CN'，'zh-TW' 中选择。

    :param style: CSS 格式。
        ex: '''BODY {color: white;}
               h3{text-align:center;}
               hr{width:50%;margin-left:25%;}'''

    :param save_dir: 小说保存目录。
        ex:
        './books/'

    :param cache_dir: 缓存文件保存目录。
        ex:
        './cache/'

    :param proxies: 所用的代理。目前 aiohttp 只支持 http 代理。
        ex:
        {'http':'http://127.0.0.1:8080'}
    :param xpath_dict: 所用的 xpath 表达式的集合。请在阅读全部源码后妥善更改。

    :param cool_down: 连接断开后，重新连接时的冷却时间 (s)。

    :param max_retries: 重新连接的最大尝试次数。
    :return: 批量抓取和保存轻小说。无法抓取的部分会在 missing.txt, black_list.log 和 black_list.txt 中列出。
             black_list.log 中不会保存因章节过少而无法抓取的轻小说。
    """
    if isinstance(save_dir, str):
        save_dir = Path(save_dir)
    if isinstance(cache_dir, str):
        cache_dir = Path(cache_dir)
    save_books(book_urls=[book_url], black_list=set(), use_cache=use_cache, language=language, style=style,
               save_dir=save_dir, cache_dir=cache_dir, proxies=proxies, xpath_dict=xpath_dict, cool_down=cool_down,
               max_retries=max_retries)


def save_books(book_urls: Optional[List[str]] = None, black_list: set = BLACK_LIST, use_cache=True,
               language: str = LANGUAGE, style: str = DEFAULT_CSS, save_dir: Union[Path, str] = Path(SAVE_DIR),
               cache_dir: Union[Path, str] = Path(CACHE_DIR), proxies: Optional[Dict[str, str]] = PROXIES,
               xpath_dict: Dict[str, str] = XPATH_DICT, cool_down: int = COOL_DOWN,
               max_retries: int = MAX_RETRIES):
    """
    批量抓取轻小说。

    :param book_urls: 待抓取图书的 Url。
        ex:
        ['https://www.esjzone.cc/detail/1563843171.html']

    :param black_list: 黑名单。妥善设置黑名单可以有效减少抓取时间。
        ex:
        ["https://www.esjzone.cc/detail/1552057167.html",  # 去了异世界后能够复制技能了
         "https://www.esjzone.cc/detail/1548502021.html",  # 二转大叔]

    :param use_cache: 是否使用缓存文件。封面和所有的章节会被缓存。

    :param language: 语言。在 'zh-CN'，'zh-TW' 中选择。

    :param style: CSS 格式。
        ex: '''BODY {color: white;}
               h3{text-align:center;}
               hr{width:50%;margin-left:25%;}'''

    :param save_dir: 小说保存目录。
        ex:
        './books/'

    :param cache_dir: 缓存文件保存目录。
        ex:
        './cache/'

    :param proxies: 所用的代理。目前 aiohttp 只支持 http 代理。
        ex:
        {'http':'http://127.0.0.1:8080'}
    :param xpath_dict: 所用的 xpath 表达式的集合。请在阅读全部源码后妥善更改。

    :param cool_down: 连接断开后，重新连接时的冷却时间 (s)。

    :param max_retries: 重新连接的最大尝试次数。
    :return: 批量抓取和保存轻小说。无法抓取的部分会在 missing.txt, black_list.log 和 black_list.txt 中列出。
             black_list.log 中不会保存因章节过少而无法抓取的轻小说。
    """
    if isinstance(save_dir, str):
        save_dir = Path(save_dir)
    if isinstance(cache_dir, str):
        cache_dir = Path(cache_dir)
    loop = asyncio.get_event_loop()
    if not book_urls:
        if not Path('all_books.py').exists():
            loop.run_until_complete(
                esjspy.base.async_build_book_list(black_list=black_list, max_page=MAX_PAGES, proxies=proxies,
                                                  xpath_dict=xpath_dict, cool_down=cool_down, max_retries=max_retries))
        all_books = __import__('all_books')
        book_urls = all_books.ALL_URLS
    loop.run_until_complete(
        esjspy.base.async_save_books(book_urls=book_urls, black_list=black_list, use_cache=use_cache, language=language,
                                     style=style, save_dir=save_dir, cache_dir=cache_dir, proxies=proxies,
                                     xpath_dict=xpath_dict, cool_down=cool_down, max_retries=max_retries))
    if esjspy.base.missing_log:
        with open('missing.txt', 'w', encoding='utf8') as f:
            f.writelines(esjspy.base.missing_log)
    if esjspy.base.black_list_log:
        with open('black_list.txt', 'w', encoding='utf8') as f:
            f.writelines(esjspy.base.black_list_log)


def check_update(book_urls: Optional[List[str]] = None, cache_dir: Union[Path, str] = Path(CACHE_DIR),
                 black_list: set = BLACK_LIST, proxies: Optional[Dict[str, str]] = PROXIES,
                 xpath_dict: Dict[str, str] = XPATH_DICT, cool_down: int = COOL_DOWN,
                 max_retries: int = MAX_RETRIES):
    """
    检查多部小说是否含有更新。

    :param book_urls: 待检查更新图书的 Url。默认为全部。
        ex:
        ['https://www.esjzone.cc/detail/1563843171.html']

    :param cache_dir: 缓存文件保存目录。
        ex:
        './cache/'

    :param proxies: 所用的代理。目前 aiohttp 只支持 http 代理。
        ex:
        {'http': 'http://127.0.0.1:8080'}

    :param xpath_dict: 所用的 xpath 表达式的集合。请在阅读全部源码后妥善更改。

    :param cool_down: 连接断开后，重新连接时的冷却时间 (s)。

    :param max_retries: 重新连接的最大尝试次数。

    :return: 无返回，待更新小说会在运行目录下产生更新列表。

    usage::
    >>> import esjspy
    >>> esjspy.check_update()
    """
    if isinstance(cache_dir, str):
        cache_dir = Path(cache_dir)
    loop = asyncio.get_event_loop()
    if not book_urls:
        if not Path('all_books.py').exists():
            loop.run_until_complete(
                esjspy.base.async_build_book_list(black_list=black_list, max_page=MAX_PAGES, proxies=proxies,
                                                  xpath_dict=xpath_dict, cool_down=cool_down, max_retries=max_retries))
        all_books = __import__('all_books')
        book_urls = all_books.ALL_URLS
    loop.run_until_complete(
        esjspy.base.async_check_update(book_urls=book_urls, black_list=black_list, cache_dir=cache_dir, proxies=proxies,
                                       xpath_dict=xpath_dict, cool_down=cool_down, max_retries=max_retries))


def update_all(book_urls: Optional[List[str]] = None, black_list: set = BLACK_LIST, use_cache=True,
               language: str = LANGUAGE, style: str = DEFAULT_CSS, save_dir: Union[Path, str] = Path(SAVE_DIR),
               cache_dir: Union[Path, str] = Path(CACHE_DIR), proxies: Optional[Dict[str, str]] = PROXIES,
               xpath_dict: Dict[str, str] = XPATH_DICT, cool_down: int = COOL_DOWN, end_update=True,
               max_retries: int = MAX_RETRIES):
    if isinstance(cache_dir, str):
        cache_dir = Path(cache_dir)
    if isinstance(save_dir, str):
        save_dir = Path(save_dir)
    loop = asyncio.get_event_loop()
    if not book_urls:
        if not Path('all_books.py').exists():
            loop.run_until_complete(
                esjspy.base.async_build_book_list(black_list=black_list, max_page=MAX_PAGES, proxies=proxies,
                                                  xpath_dict=xpath_dict, cool_down=cool_down, max_retries=max_retries))
        all_books = __import__('all_books')
        book_urls = all_books.ALL_URLS
    loop.run_until_complete(
        esjspy.base.async_update_all(book_urls=book_urls, black_list=black_list, use_cache=use_cache, language=language,
                                     style=style, save_dir=save_dir, cache_dir=cache_dir, proxies=proxies,
                                     end_update=end_update, xpath_dict=xpath_dict, cool_down=cool_down,
                                     max_retries=max_retries))
    if esjspy.base.missing_log:
        with open('missing.txt', 'w', encoding='utf8') as f:
            f.writelines(esjspy.base.missing_log)
    if esjspy.base.black_list_log:
        with open('black_list.txt', 'w', encoding='utf8') as f:
            f.writelines(esjspy.base.black_list_log)
