#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/31 19:14 
# @Author : Dothion
# @File : settings.py 
# @Software: PyCharm

# 默认参数
USE_CACHE = True
CACHE_DIR = './.cache/'
SAVE_DIR = './books/'

DEFAULT_CSS: str = '''
BODY {color: white;}
h3{text-align:center;}
hr{width:50%;margin-left:25%;}
'''

LANGUAGE = 'zh-CN'

PROXIES = {
    'http': 'http://127.0.0.1:12333'
}

COOL_DOWN = 1
MAX_RETRIES = 5

MAX_PAGES = 50

# 日志等级
# FATAL, ERROR, WARNING, INFO, DEBUG, NOTSET
STREAM_LOG_LEVEL = 'DEBUG'
FILE_LOG_LEVEL = 'ERROR'

# 日志格式
LOG_MESSAGE = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# 长度检测
# 短于此值则会报 warning
MIN_LENGTH = 300
# 一本书少于 MIN_CHAPTERS 章会
MIN_CHAPTERS = 5


XPATH_DICT = {
    'author': '//ul[@class=\'nav nav-list\']/li[1]/span/a/text()',
    'cover_url': '//img[@class=\'product-image img-responsive\']/@src',
    'toc': '//div[@id=\'tab1\']//a/@href',
    'title': '//h3/text()',
    'content': '//div[@class=\'col-xs-12 m-b-30 forum-content\']//p',
    'describe': '//div[@class=\'row m-b-15 book_description\']//div[@class=\'col-xs-12\']//p',
    'detail': '//div[@class=\'book-detail col-xs-12 col-sm-9 col-md-9 col-lg-9\']//ul[@class=\'nav nav-list\']//li',
    'post_list': '//div[@class=\'d_post_content j_d_post_content \']',
    'esj_content': '//div[@class=\'col-xs-12 m-b-30 forum-content\']//p',
    'tieba_content': '//div[@class=\'d_post_content j_d_post_content \']',
    'book_list': '//div[@class=\'caption-txt\']//a/@href'
}

BLACK_LIST = {
    'https://www.esjzone.cc/detail/1546616882.html',  # 神眼的勇者
    "https://www.esjzone.cc/detail/1548939269.html",  # 余生延长六个月
    "https://www.esjzone.cc/detail/1548938667.html",  # 欢迎来到巨蚁地下城
    "https://www.esjzone.cc/detail/1546793005.html",  # 重生的猫骑士与精灵娘的日常
    "https://www.esjzone.cc/detail/1548341113.html",  # 魔法使的婚约者
    "https://www.esjzone.cc/detail/1544283587.html",  # 边境都市的培养者
    "https://www.esjzone.cc/detail/1550677773.html",  # 田中的工作室
    "https://www.esjzone.cc/detail/1550570658.html",  # 枪使与黑猫
    "https://www.esjzone.cc/detail/1545907524.html",  # 失格纹的最强贤者
    "https://www.esjzone.cc/detail/1547198497.html",  # 婚约者恋上我的妹妹
    "https://www.esjzone.cc/detail/1550071884.html",  # ＜Infinite Dendrogram＞无尽连锁-无限树图
    "https://www.esjzone.cc/detail/1546788042.html",  # 禁忌的迷宫之王 (迷宫与后宫与主人)
    "https://www.esjzone.cc/detail/1548245645.html",  # 注意到的时候TS成了精灵
    "https://www.esjzone.cc/detail/1553107665.html",  # 召唤士的变态召唤论
    "https://www.esjzone.cc/detail/1545825949.html",  # 陶都物语
    "https://www.esjzone.cc/detail/1548593084.html",  # 那个逃犯是伪娘
    "https://www.esjzone.cc/detail/1545054501.html",  # 只有无职是不会辞掉
    "https://www.esjzone.cc/detail/1542939607.html",  # 爱书的下克上
    "https://www.esjzone.cc/detail/1550568689.html",  # 业之塔
    "https://www.esjzone.cc/detail/1558018541.html",  # 魔导具师妲莉雅不会低头　～从今天开始自由的职人生活～
    "https://www.esjzone.cc/detail/1551093501.html",  # 七星旅团的刻印使
    "https://www.esjzone.cc/detail/1550108010.html",  # 欧德·佛·海特加尔是个游戏脑
    "https://www.esjzone.cc/detail/1552054379.html",  # 被夺走一切的男子
    "https://www.esjzone.cc/detail/1550593056.html",  # 可喜可贺我进化成了美少女
    "https://www.esjzone.cc/detail/1542940812.html",  # 异世界药局
    "https://www.esjzone.cc/detail/1551091482.html",  # 空色的魔法使
    "https://www.esjzone.cc/detail/1552579267.html",  # 我的怪物眷族
    "https://www.esjzone.cc/detail/1543650954.html",  # 平凡士兵梦回过去
    "https://www.esjzone.cc/detail/1545922563.html",  # 异世界悠闲农家
    "https://www.esjzone.cc/detail/1545711775.html",  # 想吃龙先生的肉
    "https://www.esjzone.cc/detail/1561963678.html",  # 从领民0人开始的边境领主生活
    "https://www.esjzone.cc/detail/1546787149.html",  # 转职神殿开了
    "https://www.esjzone.cc/detail/1548342790.html",  # 异世界的气象预报员
    "https://www.esjzone.cc/detail/1558409389.html",  # 身为恶役千金的我重新做人
    "https://www.esjzone.cc/detail/1543764912.html",  # 全人类穿越异世界但我被留下了
    "https://www.esjzone.cc/detail/1542940140.html",  # 异世界支配的skilltake
    "https://www.esjzone.cc/detail/1543646749.html",  # 无属性魔法的救世主
    "https://www.esjzone.cc/detail/1543308788.html",  # 贤者的孙子
    "https://www.esjzone.cc/detail/1546060924.html",  # 龙套男孩重生成了美少女的事
    "https://www.esjzone.cc/detail/1543764367.html",  # 转生龙蛋
    "https://www.esjzone.cc/detail/1548592581.html",  # 谁都能做到的暗中协助魔王讨伐
    "https://www.esjzone.cc/detail/1543387217.html",  # 在异世界迷宫开后宫
    "https://www.esjzone.cc/detail/1546322876.html",  # 成为塔的管理者
    "https://www.esjzone.cc/detail/1548939756.html",  # 轮到自己转移去异世界
    "https://www.esjzone.cc/detail/1552148473.html",  # 女主角、你来当
    "https://www.esjzone.cc/detail/1544268740.html",  # 转生成了少女漫里的白豚千金
    "https://www.esjzone.cc/detail/1550147463.html",  # 最强之人转生成F级冒险者
    "https://www.esjzone.cc/detail/1546275874.html",  # 被召唤的贤者前往异世界
    "https://www.esjzone.cc/detail/1550151168.html",  # 赤目的公爵千金
    "https://www.esjzone.cc/detail/1552062647.html",  # 以剑士为目标入学
    "https://www.esjzone.cc/detail/1548582043.html",  # 公爵大人讨厌女人
    "https://www.esjzone.cc/detail/1546169443.html",  # 在异世界转移从女神那得到祝福
    "https://www.esjzone.cc/detail/1547093995.html",  # 大叔捡到了勇者和魔王
    "https://www.esjzone.cc/detail/1552203932.html",  # 狼领主
    "https://www.esjzone.cc/detail/1545635365.html",  # 利用时空魔法往返地球和异世界
    "https://www.esjzone.cc/detail/1552053053.html",  # 我突破技能等级
    "https://www.esjzone.cc/detail/1546789147.html",  # 异世界迷宫都市治愈魔法师
    "https://www.esjzone.cc/detail/1551091950.html",  # 异世归来的我变成了银发美少女
    "https://www.esjzone.cc/detail/1547285888.html",  # 萝丝千金希望成为平民
    "https://www.esjzone.cc/detail/1545636740.html",  # 豚猪公爵
    "https://www.esjzone.cc/detail/1545636000.html",  # 幸存炼金术师想在城里静静生活
    "https://www.esjzone.cc/detail/1546275874.html",  # 被召唤的贤者前往异世界
    "https://www.esjzone.cc/detail/1550151168.html",  # 赤目的公爵千金
    "https://www.esjzone.cc/detail/1552062647.html",  # 以剑士为目标入学
    "https://www.esjzone.cc/detail/1548582043.html",  # 公爵大人讨厌女人
    "https://www.esjzone.cc/detail/1546169443.html",  # 在异世界转移从女神那得到祝福
    "https://www.esjzone.cc/detail/1547093995.html",  # 大叔捡到了勇者和魔王
    "https://www.esjzone.cc/detail/1552203932.html",  # 狼领主
    "https://www.esjzone.cc/detail/1545635365.html",  # 利用时空魔法往返地球和异世界
    "https://www.esjzone.cc/detail/1552053053.html",  # 我突破技能等级
    "https://www.esjzone.cc/detail/1546789147.html",  # 异世界迷宫都市治愈魔法师
    "https://www.esjzone.cc/detail/1551091950.html",  # 异世归来的我变成了银发美少女
    "https://www.esjzone.cc/detail/1547285888.html",  # 萝丝千金希望成为平民
    "https://www.esjzone.cc/detail/1545636740.html",  # 豚猪公爵
    "https://www.esjzone.cc/detail/1545636000.html",  # 幸存炼金术师想在城里静静生活
}
