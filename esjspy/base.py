#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/31 18:30 
# @Author : Dothion
# @File : base.py 
# @Software: PyCharm
import asyncio
import hashlib
import logging
import pickle
import shutil
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, List, Dict, NamedTuple, Set, Optional

import aiohttp
from ebooklib import epub
from lxml import html
from opencc import OpenCC

from esjspy.settings import *

logger = logging.getLogger('esjspy')
logger.setLevel(logging.DEBUG)
_logfile = './LOG.log'
_logger_file_handler = logging.FileHandler(_logfile, mode='w', encoding='utf8')
_logger_file_handler.setLevel(FILE_LOG_LEVEL)
_logger_black_list_handler = logging.FileHandler('black_list.log', mode='w', encoding='utf8')
_logger_black_list_handler.setLevel(logging.ERROR)
_logger_stream_handler = logging.StreamHandler()
_logger_stream_handler.setLevel(STREAM_LOG_LEVEL)
_logger_message_formatter = logging.Formatter(LOG_MESSAGE)
_logger_black_list_formatter = logging.Formatter('    %(message)s')
_logger_file_handler.setFormatter(_logger_message_formatter)
_logger_stream_handler.setFormatter(_logger_message_formatter)
_logger_black_list_handler.setFormatter(_logger_black_list_formatter)
logger.addHandler(_logger_file_handler)
logger.addHandler(_logger_black_list_handler)
logger.addHandler(_logger_stream_handler)

_simplified = {'zh-CN', 'zh-SG', }
_default_cc = OpenCC('t2s') if LANGUAGE in _simplified else OpenCC('s2t')
_file_name_replace = '\\/:*?"<>|'
_file_name_trans_tab = str.maketrans(_file_name_replace, '-' * len(_file_name_replace))

missing_log = []
black_list_log = []


@dataclass
class BookData:
    url: str
    title: str
    author: str
    cover_url: str = field(hash=False, compare=False)
    cover: bytes = field(hash=False, compare=False, repr=False)
    detail: List[str] = field(hash=False, compare=False, repr=False)
    describe: List[str] = field(hash=False, compare=False, repr=False)
    toc: List[str]


class MissingChapter(NamedTuple):
    number: int
    title: str
    url: str


@dataclass
class Chapter:
    url: str
    title: str = field(hash=False, compare=False)
    content: List[str] = field(hash=False, compare=False)

    def __post_init__(self):
        self._length = len(''.join(self.content))

    def as_html(self) -> str:
        escape_set = {'<br>', '<br/>', '<br />', '<tr>', '<tr/>', '<tr />'}
        return '\n'.join(['<h3>%s</h3>' % self.title,
                          '<hr /><p>来源：<a href=%s>%s</a></p><hr />' % (self.url, self.url) if self.url else '',
                          *[para if para in escape_set else '<p>%s</p>' % para for para in self.content]])

    def __len__(self):
        return self._length


# 我本人举双手双脚赞同著作权保护法
# 可是我真的有两头牛
_copyright_page = Chapter(url='', title='关于著作权', content=[
    '''本 epub 副本由 esjspy 工具自动生成，仅供个人学习、     
       研究和欣赏使用。''',
    '''本书原书著作权由原书著作权方所有，翻译著作权由译者所有。
       若未取得著作权方的授权，则任何人不得修改、转载、
       以任何渠道分发此书，不得将此书用于商业用途。'''])


@dataclass
class Book:
    book_data: BookData
    content: List[Chapter]
    missing_chapters: List[MissingChapter]

    def write_epub(self, save_dir: Path = Path(SAVE_DIR), style: str = DEFAULT_CSS, use_cache: bool = USE_CACHE,
                   language: str = LANGUAGE, cache_dir: Path = Path(CACHE_DIR), add_copyright_page=True):
        length = len(self.content)
        missing_number = len(self.missing_chapters)
        title = _default_cc.convert(self.book_data.title)
        # 处理过短书籍
        if length < MIN_CHAPTERS:
            black_list_log.append('"%s",  # %s\n' % (self.book_data.url, title))
            logger.debug('《%s》过短。' % title if LANGUAGE in _simplified else '《%s》過短。' % title)
            return
        # 处理缺章
        if (length >= 200 and missing_number >= 10) or missing_number >= 5:
            black_list_log.append('"%s",  # %s\n' % (self.book_data.url, title))
            logger.debug('《%s》一书缺失章节过多，达 %d 章。' % (title, len(self.missing_chapters))
                         if LANGUAGE in _simplified else
                         '《%s》一書缺失章節過多，達 %d 章。' % (title, len(self.missing_chapters)))
            logger.error('"%s",  # %s\n' % (self.book_data.url, title))
            return
        if self.missing_chapters:
            missing_log.append('《%s》\n' % title)
            missing_log.extend(['   - 第 %d 章《%s》- %s\n' % (i.number, i.title, i.url) for i in self.missing_chapters])
            logger.warning('《%s》一书缺 %d 章。' % (title, missing_number) if LANGUAGE in _simplified else
                           '《%s》一書缺 %d 章。' % (title, missing_number))

        book = epub.EpubBook()
        cc = OpenCC('t2s') if language in _simplified else OpenCC('s2t')

        # 设置图书属性
        book_data = self.book_data
        book.set_identifier(_gen_identifier_from_url(book_data.url))
        title = cc.convert(self.book_data.title)
        book.set_title(title)
        book.set_language(language)
        book.add_author(book_data.author)
        # 添加“关于本书”
        detail = '\n'.join(['<p>%s</p>' % cc.convert(para) for para in self.book_data.detail])
        describe = '\n'.join(['<p>%s</p>' % cc.convert(para) for para in self.book_data.describe])
        about = epub.EpubHtml(title=cc.convert('关于本书'), file_name='about.xhtml', lang=language,
                              content='<p><h1>%s</h1></p>%s<p><h3>介绍</h3></p>%s' % (title, detail, describe))
        book.add_item(about)
        # 添加各章节
        counter = 1
        for chapter in self.content:
            chapter_html = epub.EpubHtml(title=cc.convert(chapter.title), file_name='%04d' % counter + '.xhtml',
                                         lang=language, content=cc.convert(chapter.as_html()))
            book.add_item(chapter_html)
            counter += 1

        if add_copyright_page:
            chapter_html = epub.EpubHtml(title=cc.convert('关于著作权'), file_name='copyright.xhtml',
                                         lang=language, content=cc.convert(_copyright_page.as_html()))
            book.add_item(chapter_html)
        # 添加目录
        book.toc = ([i for i in book.items if type(i) == epub.EpubHtml])
        # 添加 Ncx 和 Nav
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        # 添加 CSS 样式
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
        book.add_item(nav_css)
        # 添加 spine
        book.spine = ['cover', 'nav', *[i for i in book.items if type(i) == epub.EpubHtml]]
        # 写入 epub
        if not save_dir.exists():
            save_dir.mkdir(parents=True)
        save_path = save_dir.cwd() / save_dir / ('%s - 至第 %d 章.epub' % (title, len(self.content)))
        epub.write_epub('writing.epub', book, {})
        shutil.move('./writing.epub', str(save_path))
        logger.debug('已生成《%s》一书。' % title if LANGUAGE in _simplified else '已生成《%s》一書。' % title)
        # 更新缓存中图书信息
        _dump(identifier=_gen_identifier_from_url(book_data.url), some_obj=self.book_data,
              cache_dir=cache_dir, use_cache=use_cache)


@lru_cache(maxsize=None)
def _gen_identifier_from_url(any_url: str) -> str:
    for end in ['.jpg', '.jpeg', '.png', '.bmp']:
        if end in any_url:
            any_url = any_url[:any_url.rfind('?') - 1] if '?' in any_url else any_url
            return 'pic:%s' % any_url
    if 'esjzone.cc/detail' in any_url:
        return 'esjzone:book:' + any_url[any_url.find('detail/') + 7:any_url.rfind('htm') - 1]
    # https://www.esjzone.cc/forum/1545673947/20693.html
    elif 'esjzone.cc/forum' in any_url:
        return 'esjzone:chapter:' + any_url[any_url.find('forum/') + 6:any_url.rfind('htm') - 1]
    # https://tieba.baidu.com/p/6030543047
    elif 'tieba.baidu.com/p' in any_url:
        if '?' in any_url:
            return 'tieba:' + any_url[any_url.find('p/') + 2:any_url.rfind('?') - 1]
        else:
            return 'tieba:' + any_url[any_url.find('p/') + 2:]
    else:
        return 'unknown:%s' % any_url


@lru_cache(maxsize=None)
def _gen_url_from_identifier(identifier: str) -> str:
    if identifier.startswith('pic:'):
        return identifier[4:]
    elif identifier.startswith('esjzone:book:'):
        return 'https://www.esjzone.cc/detail/%s.html' % identifier[13:]
    elif identifier.startswith('esjzone:chapter:'):
        return 'https://www.esjzone.cc/forum/%s.html' % identifier[16:]
    elif identifier.startswith('tieba:'):
        return 'https://tieba.baidu.com/p/%s' % identifier[6:]
    elif identifier.startswith('unknown:'):
        return identifier[8:]


@lru_cache(maxsize=None)
def _gen_md5(identifier: str) -> str:
    hashed = hashlib.md5(identifier.encode('utf8'))
    return hashed.hexdigest()


def _dump(identifier: str, some_obj: Any, cache_dir: Path = Path(CACHE_DIR), use_cache=True) -> None:
    if not use_cache:
        return
    md5 = _gen_md5(identifier)
    cache_dir = cache_dir / md5[0:2] / md5[2:4]
    if not cache_dir.exists():
        cache_dir.mkdir(parents=True)
    cache_path = cache_dir / md5
    with cache_path.open('wb') as f:
        pickle.dump(some_obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    logger.debug('保存了 %s 的内容到缓存。' % identifier if LANGUAGE in _simplified else
                 '保存了 %s 的內容到 cache。' % identifier)


def _scan(identifier: str, cache_dir: Path = Path(CACHE_DIR)) -> Any:
    md5 = _gen_md5(identifier)
    cache_dir = cache_dir / md5[0:2] / md5[2:4]
    cache_path = cache_dir / md5
    logger.debug('从缓存中读取了 %s 的内容。' % identifier if LANGUAGE in _simplified else
                 '從 cache 中讀取了 %s 的內容。' % identifier)
    with cache_path.open('rb') as f:
        return pickle.load(f)


@lru_cache(maxsize=None)
def _has_cached(identifier: str, cache_dir: Path = Path(CACHE_DIR), use_cache=True) -> bool:
    if not use_cache:
        return False
    md5 = _gen_md5(identifier)
    cache_dir = cache_dir / md5[0:2] / md5[2:4]
    cache_path = cache_dir / md5
    return cache_path.exists()


async def _async_fetch_text(any_url: str, session: aiohttp.ClientSession, retries: int = 0, cool_down: int = COOL_DOWN,
                            max_retries: int = MAX_RETRIES, **kwargs: Any) -> str:
    async with session.get(any_url, **kwargs) as response:
        try:
            logger.debug('正在连接到 %s...' % any_url if LANGUAGE in _simplified else '正在連接到%s...' % any_url)
            text = await response.text()
        except UnicodeDecodeError:
            raw = await response.read()
            # 强行解释.jpg
            text = raw.decode(response.get_encoding(), 'replace').encode('utf-8')
        except aiohttp.ClientConnectionError or aiohttp.ServerConnectionError as e:
            logger.warning('%s 的连接已断开。' % any_url if LANGUAGE in _simplified else '%s 的連接已斷開' % any_url)
            if retries <= max_retries:
                logger.debug('正在重试第 %d 次...' % retries if LANGUAGE in _simplified else '正在重試第 %d 次...' % retries)
                if cool_down:
                    await asyncio.sleep(cool_down)
                return await _async_fetch_text(any_url=any_url, session=session, retries=retries + 1,
                                               cool_down=cool_down, *kwargs)
            else:
                raise e
        return text


async def _async_fetch_content(any_url: str, session: aiohttp.ClientSession, retries: int = 0,
                               cool_down: int = COOL_DOWN, max_retries: int = MAX_RETRIES, **kwargs: Any) -> bytes:
    async with session.get(any_url, **kwargs) as response:
        try:
            logger.debug('正在连接到 %s...' % any_url if LANGUAGE in _simplified else '正在連接到 %s...' % any_url)
            content = await response.read()
        except aiohttp.ClientConnectionError as e:
            logger.warning('%s 的连接已断开。' % any_url if LANGUAGE in _simplified else '%s 的連接已斷開' % any_url)
            if retries <= max_retries:
                logger.debug('正在重试第 %d 次...' % retries if LANGUAGE in _simplified else '正在重試第 %d 次...' % retries)
                if cool_down:
                    await asyncio.sleep(cool_down)
                return await _async_fetch_content(any_url=any_url, session=session, retries=retries + 1,
                                                  cool_down=cool_down, *kwargs)
            else:
                raise e
        return content


async def _async_fetch_book_data(book_url: str, xpath_dict: Dict[str, str] = XPATH_DICT, use_cache: bool = USE_CACHE,
                                 cache_dir: Path = Path(CACHE_DIR), _fetch_cover=True, **kwargs: Any) -> BookData:
    tree_root = html.fromstring(await _async_fetch_text(book_url, **kwargs))
    default_cover_url = 'https://www.esjzone.cc/assets/img/empty.jpg'
    raw_dict = {key: tree_root.xpath(xpath_dict[key]) for key in
                {'title', 'author', 'cover_url', 'detail', 'describe', 'toc'}}
    # 生成作者
    author = raw_dict['author'][0] if raw_dict['author'] else '未知'
    # 生成标题
    title = _default_cc.convert(raw_dict['title'][0]).translate(_file_name_trans_tab) if raw_dict['title'] else '未知'
    logger.debug('正在抓取《%s》一书相关信息。' % title if LANGUAGE in _simplified else
                 '正在抓取《%s》一書相關信息。' % title)
    # 生成封面
    cover_url_564x = raw_dict['cover_url'][0] if raw_dict['cover_url'] else default_cover_url
    cover_url = cover_url_564x.replace('564x', 'originals')
    if not cover_url.startswith('http'):
        cover_url = 'https://www.esjzone.cc%s' % cover_url
    if _fetch_cover:
        cover_identifier = _gen_identifier_from_url(cover_url)
        if _has_cached(cover_identifier, cache_dir=cache_dir, use_cache=use_cache):
            cover = _scan(cover_identifier, cache_dir=cache_dir)
        else:
            try:
                cover = await _async_fetch_content(cover_url, **kwargs)
                _dump(cover_identifier, cover, cache_dir=cache_dir, use_cache=use_cache)
            except aiohttp.ClientConnectionError or aiohttp.ServerConnectionError:
                cover = await _async_fetch_content(default_cover_url, **kwargs)
                _dump(cover_identifier, cover, cache_dir=cache_dir, use_cache=use_cache)
                logger.warning('《%s》一书封面获取失败，请检查代理设置。' % title
                               if LANGUAGE in _simplified else '《%s》一書封面獲取失敗，請檢查代理設置。' % title)
    else:
        cover = ''
    # 生成索引
    detail = [i.xpath('string(.)') for i in raw_dict['detail']
              if len(i.xpath('string(.)')) and not i.xpath('@class')]
    # 生成描述
    describe = [i.xpath('string(.)') for i in raw_dict['describe']
                if len(i.xpath('string(.)')) and not i.xpath('@class')]
    # 生成目录
    toc = [chapter_url for chapter_url in raw_dict['toc']
           if 'esjzone' in chapter_url or 'tieba' in chapter_url]

    book_data = BookData(url=book_url, title=title, author=author, cover_url=cover_url,
                         detail=detail, cover=cover, describe=describe, toc=toc)
    return book_data


async def _async_fetch_chapter_from_esjzone(chapter_url: str, xpath_dict: Dict[str, str] = XPATH_DICT,
                                            use_cache: bool = USE_CACHE,
                                            cache_dir: Path = Path(CACHE_DIR), **kwargs: Any) -> Chapter:
    identifier = _gen_identifier_from_url(chapter_url)
    if _has_cached(identifier, cache_dir, use_cache=use_cache):
        chapter = _scan(identifier, cache_dir)
        return chapter
    tree_root = html.fromstring(await _async_fetch_text(chapter_url, **kwargs))
    raw_dict = {key: tree_root.xpath(xpath_dict[key]) for key in {'title', 'esj_content'}}
    title = raw_dict['title'][0] if raw_dict['title'] else '未知'
    title = _default_cc.convert(title)
    content = raw_dict['esj_content']
    content = [i.text for i in content if i.text and i.text.strip('\xa0')]
    chapter = Chapter(url=chapter_url, title=title, content=content)
    if len(chapter) >= MIN_LENGTH:
        _dump(identifier, chapter, cache_dir, use_cache=use_cache)
    return chapter


async def _async_fetch_chapter_from_tieba(chapter_url: str, see_lz: bool = True, use_cache: bool = USE_CACHE,
                                          xpath_dict: Dict[str, str] = XPATH_DICT,
                                          cache_dir: Path = Path(CACHE_DIR), **kwargs: Any) -> Chapter:
    identifier = _gen_identifier_from_url(chapter_url)
    if _has_cached(identifier, cache_dir, use_cache):
        chapter = _scan(identifier, cache_dir)
        return chapter

    # 设置只看楼主
    if see_lz:
        fetch_url = chapter_url + '?see_lz=1'
    else:
        fetch_url = chapter_url

    tree_root = html.fromstring(await _async_fetch_text(fetch_url, **kwargs))
    if tree_root.xpath('//body/@class') == ['page404'] or tree_root.xpath('//div[@class=\'head_content\']'):
        return Chapter(url=chapter_url, title=_default_cc.convert('贴吧404'), content=['贴吧404'])
    raw_dict = {key: tree_root.xpath(xpath_dict[key]) for key in {'title', 'tieba_content'}}
    title = raw_dict['title'][0] if raw_dict['title'] else '未知'
    title = _default_cc.convert(title)
    raw_content = raw_dict['tieba_content']
    content = []
    for post in raw_content:
        if post.xpath('.//div[@class=\'post_bubble_middle_inner\']'):
            post = post.xpath('.//div[@class=\'post_bubble_middle_inner\']')[0]
        if not post.xpath('a'):
            post_text = [i.strip() for i in post.xpath('text()') if i.strip('\xa0')]
        else:
            post = post.xpath('text()|a/text()|br')
            post_text = []
            current_list = []
            for fragment in post:
                if isinstance(fragment, str):
                    current_list.append(fragment)
                else:
                    post_text.append(''.join(current_list))
                    current_list = []
            if current_list:
                post_text.append(''.join(current_list))
            post_text = [i.strip() for i in post_text if i.strip('\xa0')]
        if see_lz and len(''.join(post_text)) > 5:
            content += post_text
            content += ['<hr />']
        elif not see_lz and len(''.join(post_text)) > MIN_LENGTH / 2:
            content += post_text
            content += ['<hr />']
    chapter = Chapter(url=chapter_url, title=title, content=content[:-1])
    if len(chapter) >= MIN_LENGTH:
        _dump(identifier, chapter, cache_dir, use_cache=use_cache)
    return chapter


async def _async_fetch_chapter(chapter_url: str, **kwargs: Any) -> Chapter:
    identifier = _gen_identifier_from_url(chapter_url)
    if identifier.startswith('tieba'):
        chapter = await _async_fetch_chapter_from_tieba(chapter_url, see_lz=True, **kwargs)
        if len(chapter) <= MIN_LENGTH:
            chapter = await _async_fetch_chapter_from_tieba(chapter_url, see_lz=False, **kwargs)
        if len(chapter) <= MIN_LENGTH:
            logger.debug('本章过短！' if LANGUAGE in _simplified else '本章過短！')
        return chapter
    elif identifier.startswith('esjzone'):
        chapter = await _async_fetch_chapter_from_esjzone(chapter_url, **kwargs)
        if len(chapter) <= MIN_LENGTH:
            logger.debug('本章过短！' if LANGUAGE in _simplified else '本章過短！')
        return chapter
    else:
        raise ValueError('无法识别网址 %s。' % chapter_url if LANGUAGE in _simplified else
                         '無法識別網址 %s。' % chapter_url)


async def _async_fetch_book(book_url: str, **kwargs: Any) -> Book:
    book_data = await _async_fetch_book_data(book_url, **kwargs)
    logger.info('正在构建《%s》一书...' % book_data.title if LANGUAGE in _simplified else
                '正在構建《%s》一書...' % book_data.title)
    book_content = []
    missing_chapters = []
    counter = 1
    for chapter_url in book_data.toc:
        chapter = await _async_fetch_chapter(chapter_url, **kwargs)
        book_content.append(chapter)
        logger.debug('已抓取第 %d 章：《%s》。' % (counter, chapter.title))
        if len(chapter) <= MIN_LENGTH:
            missing_chapters.append(MissingChapter(number=counter, title=chapter.title, url=chapter.url))
        counter += 1
    return Book(book_data=book_data, content=book_content, missing_chapters=missing_chapters)


async def async_save_books(book_urls: List[str], use_cache: bool = True, proxies: Dict[str, str] = PROXIES,
                           black_list: set = BLACK_LIST, language: str = LANGUAGE, style: str = DEFAULT_CSS,
                           save_dir: Path = Path(SAVE_DIR), cache_dir: Path = Path(CACHE_DIR), **kwargs: Any) -> None:
    if proxies:
        kwargs['proxy'] = proxies['http']
    if black_list:
        book_urls = list(set(book_urls) - set(black_list))
    async with aiohttp.ClientSession() as session:
        for book_url in book_urls:
            book = await _async_fetch_book(book_url=book_url, use_cache=use_cache, session=session,
                                           cache_dir=cache_dir, **kwargs)
            book.write_epub(style=style, save_dir=save_dir, language=language, use_cache=use_cache, cache_dir=cache_dir)


async def _async_has_update(book_url: str, cache_dir=CACHE_DIR, **kwargs: Any) -> bool:
    if not _has_cached(identifier=_gen_identifier_from_url(book_url), cache_dir=cache_dir):
        return True
    online_book_data = await _async_fetch_book_data(book_url, **kwargs)
    cached_book_data = _scan(identifier=_gen_identifier_from_url(book_url), cache_dir=cache_dir)
    return online_book_data != cached_book_data


async def async_check_update(book_urls: List[str], black_list: set = BLACK_LIST,
                             proxies: Optional[Dict[str, str]] = PROXIES, **kwargs: Any):
    if proxies:
        kwargs['proxy'] = proxies['http']
    if black_list:
        book_urls = list(set(book_urls) - set(black_list))
    checked_list = []
    async with aiohttp.ClientSession() as session:
        for book_url in book_urls:
            if await _async_has_update(book_url=book_url, session=session, proxy=proxies['http'], **kwargs):
                checked_list.append(book_url)
    with open('update.log', 'w', encoding='utf8') as f:
        f.writelines(["'%s',\n" % i for i in checked_list])


def _check_toc(toc: List[str]) -> bool:
    if len(toc) < MIN_CHAPTERS:
        return False
    for chapter_url in toc:
        identifier = _gen_identifier_from_url(any_url=chapter_url)
        if identifier.startswith('unknown') or identifier.startswith('pic'):
            return False
    return True


async def _async_build_book_list(black_list: Set[str] = BLACK_LIST, max_page=MAX_PAGES,
                                 xpath_dict: Dict[str, str] = XPATH_DICT, **kwargs: Any) -> None:
    book_urls = []
    checked_urls = []
    counter = 1
    logger.info('正在构建全部小说列表。' if LANGUAGE in _simplified else '正在構建全部小說列表。')
    if max_page <= 0:
        max_page = 200
    while counter <= max_page:
        page_url = 'https://www.esjzone.cc/list/%d.html' % counter
        text = await _async_fetch_text(page_url, **kwargs)
        tree_root = html.fromstring(text)
        book_urls_in_page = ['https://www.esjzone.cc%s' % i for i in tree_root.xpath(xpath_dict['book_list'])
                             if i not in black_list]
        if book_urls_in_page and book_urls_in_page[0] in book_urls:
            break
        book_urls += book_urls_in_page
        logger.debug('已获取第 %d 页内容。' % counter if LANGUAGE in _simplified else '已獲取第 %d 页內容。' % counter)
        counter += 1
    for book_url in book_urls:
        book_data = await _async_fetch_book_data(book_url, xpath_dict=xpath_dict,
                                                 _fetch_cover=False, **kwargs)
        if _check_toc(book_data.toc):
            checked_urls.append((book_data.title, book_url))
    with open('all_books.py', 'w', encoding='utf8') as f:
        f.write('ALL_URLS = [\n')
        for title, url in checked_urls:
            if url not in BLACK_LIST:
                f.write("    '%s',  # %s\n" % (url, title))
        f.write(']\n\n')


async def async_build_book_list(proxies: Optional[Dict[str, str]] = PROXIES, **kwargs: Any) -> None:
    if proxies:
        kwargs['proxy'] = proxies['http']
    async with aiohttp.ClientSession() as session:
        await _async_build_book_list(session=session, **kwargs)
