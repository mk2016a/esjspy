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
    "https://www.esjzone.cc/detail/1548330034.html",  # 水果糖香味的千金物语
    "https://www.esjzone.cc/detail/1546881804.html",  # 转生异世界成为美少女城主
    "https://www.esjzone.cc/detail/1552057167.html",  # 去了异世界后能够复制技能了
    "https://www.esjzone.cc/detail/1548502021.html",  # 二转大叔
    "https://www.esjzone.cc/detail/1543763174.html",  # 中了40亿的我要搬到异世界去住了
    "https://www.esjzone.cc/detail/1548510795.html",  # 告白了九十九次却还是不行
    "https://www.esjzone.cc/detail/1546342666.html",  # 等级只有1级但固有技能是最强
    "https://www.esjzone.cc/detail/1549701459.html",  # 恶役转生但是为什么会变成这样
    "https://www.esjzone.cc/detail/1545129972.html",  # 这是技能也没能发挥威力的事
    "https://www.esjzone.cc/detail/1544269417.html",  # 恋爱就会死亡什么的、好难受
    "https://www.esjzone.cc/detail/1556615673.html",  # 龙峰之足
    "https://www.esjzone.cc/detail/1544273256.html",  # 最强的黑骑士转职成了战斗女仆
    "https://www.esjzone.cc/detail/1543671826.html",  # 必胜迷宫运营方法
    "https://www.esjzone.cc/detail/1545828734.html",  # 迷宫少女
    "https://www.esjzone.cc/detail/1544281174.html",  # 你这种家伙别想打赢魔王
    "https://www.esjzone.cc/detail/1543764259.html",  # 转生恶役只好拔除破灭旗标
    "https://www.esjzone.cc/detail/1543757174.html",  # 药水在身胜积千金
    "https://www.esjzone.cc/detail/1548246156.html",  # 成为四胞胎姐妹中一员的三二事
    "https://www.esjzone.cc/detail/1543764438.html",  # 沃特尼亚战记
    "https://www.esjzone.cc/detail/1548242085.html",  # 讨伐魔王后的低调生活
    "https://www.esjzone.cc/detail/1543990827.html",  # 因为校工桑并不是勇者
    "https://www.esjzone.cc/detail/1546168917.html",  # THE NEW GATE
    "https://www.esjzone.cc/detail/1546365128.html",  # 即使是不起眼剑圣亦是最强
    "https://www.esjzone.cc/detail/1546314666.html",  # 人偶地下城
    "https://www.esjzone.cc/detail/1546281566.html",  # 召唤出的杀戮者
    "https://www.esjzone.cc/detail/1543662598.html",  # 猫耳猫（只有我知道这个世界是游戏）
    "https://www.esjzone.cc/detail/1545651078.html",  # 异世界转移后一个星期就建国了
    "https://www.esjzone.cc/detail/1542941840.html",  # 贤者之剑
    "https://www.esjzone.cc/detail/1545569030.html",  # 转生为售货机的我在迷宫徘徊
    "https://www.esjzone.cc/detail/1560850775.html",  # 其实，我乃最强？
    "https://www.esjzone.cc/detail/1549069251.html",  # 事与愿违的不死冒险者
    "https://www.esjzone.cc/detail/1552147959.html",  # 第三王子的光芒过于耀眼无法直视
    "https://www.esjzone.cc/detail/1546093661.html",  # 在这个世界排行第9左右的我,被派去负责监视异世界人了
    "https://www.esjzone.cc/detail/1545917973.html",  # 药屋少女的呢喃
    "https://www.esjzone.cc/detail/1546061567.html",  # 在异世界使用魅力开了奴隶后宫
    "https://www.esjzone.cc/detail/1553101073.html",  # 坚持就是魔力
    "https://www.esjzone.cc/detail/1557190133.html",  # 我仰赖淫魔术建立了奴隶后宫
    "https://www.esjzone.cc/detail/1546925812.html",  # 回家路上捡到妻女
    "https://www.esjzone.cc/detail/1552056630.html",  # 再临勇者想当普通人
    "https://www.esjzone.cc/detail/1545652646.html",  # 为了养老金去异界存八万金
    "https://www.esjzone.cc/detail/1550223630.html",  # 从最底层生物到杀神为止
    "https://www.esjzone.cc/detail/1550224094.html",  # 转生从上位世界到下位世界
    "https://www.esjzone.cc/detail/1545206694.html",  # lv999的村民
    "https://www.esjzone.cc/detail/1544078732.html",  # 那个人后来
    "https://www.esjzone.cc/detail/1550681386.html",  # 狩猎史莱姆300年
    "https://www.esjzone.cc/detail/1546060392.html",  # 万年d等级的中年冒险者
    "https://www.esjzone.cc/detail/1542937524.html",  # 被卷入异世界转移的家伙
    "https://www.esjzone.cc/detail/1544163514.html",  # 我不是说了能力要平均值么
    "https://www.esjzone.cc/detail/1543763022.html",  # 异世界狂想曲
    "https://www.esjzone.cc/detail/1560194058.html",  # Nostalgia world online
    "https://www.esjzone.cc/detail/1547287409.html",  # 恶役千金奋斗记
    "https://www.esjzone.cc/detail/1543650163.html",  # 战栗的魔术师与五帝兽
    "https://www.esjzone.cc/detail/1551090774.html",  # 超丑的我再转生的结果
    "https://www.esjzone.cc/detail/1546090205.html",  # 被病娇妹妹爱的死去活来
    'https://www.esjzone.cc/detail/1546092615.html',  # 打造魔王大人的城镇
    "https://www.esjzone.cc/detail/1550223018.html",  # 然后少女得到了恶女的身体
    "https://www.esjzone.cc/detail/1548841218.html",  # 等级无限的契约者
    "https://www.esjzone.cc/detail/1553704150.html",  # 转生王子的英雄谭
    "https://www.esjzone.cc/detail/1548297882.html",  # 俺不可能攻略好友
    "https://www.esjzone.cc/detail/1543763167.html",  # 尼特族的异世界就职记
    "https://www.esjzone.cc/detail/1545804255.html",  # 原将军的不死骑士
    "https://www.esjzone.cc/detail/1542942767.html",  # 小说家连载7th
    "https://www.esjzone.cc/detail/1546365987.html",  # 以剪切粘贴在这个世界生活
    "https://www.esjzone.cc/detail/1543303378.html",  # 黑之创造召唤师
    "https://www.esjzone.cc/detail/1543305738.html",  # 迷宫的魔王最虚弱
    "https://www.esjzone.cc/detail/1551092733.html",  # 宛若恶魔般的公爵一家
    "https://www.esjzone.cc/detail/1545674180.html",  # 重装大小姐玛娜特〜解除他人魔咒的方法〜
    "https://www.esjzone.cc/detail/1548246397.html",  # 月桂树之歌
    "https://www.esjzone.cc/detail/1544265729.html",  # 乙女游戏世界对路人角色太严厉
    "https://www.esjzone.cc/detail/1552055348.html",  # 看起来等级是0
    "https://www.esjzone.cc/detail/1543303989.html",  # 没落预订
    "https://www.esjzone.cc/detail/1546223076.html",  # 异世界转生骚动记
    "https://www.esjzone.cc/detail/1547024145.html",  # 为鲜血献上吻
    "https://www.esjzone.cc/detail/1547286247.html",  # 折断逆后宫旗标
    "https://www.esjzone.cc/detail/1547286560.html",  # 自称转生者的恶役令媛
    "https://www.esjzone.cc/detail/1552053324.html",  # Cheese
    "https://www.esjzone.cc/detail/1543764936.html",  # 圣女的魔力是万能的
    "https://www.esjzone.cc/detail/1546618252.html",  # 怕痛少女的防御特化
    "https://www.esjzone.cc/detail/1544271664.html",  # 暗黑骑士物语
    "https://www.esjzone.cc/detail/1548734437.html",  # 运用开挂魔术扭转命运
    "https://www.esjzone.cc/detail/1550914310.html",  # 原最强玩家在异世界成为最强
    "https://www.esjzone.cc/detail/1544272723.html",  # 异世界人的指南书
    "https://www.esjzone.cc/detail/1548946126.html",  # 驱除人-驱除者
    "https://www.esjzone.cc/detail/1549007916.html",  # 回复术士重来人生
    "https://www.esjzone.cc/detail/1543763301.html",  # 精灵幻想记
    "https://www.esjzone.cc/detail/1543764573.html",  # 现实主义勇者的王国再建记
    "https://www.esjzone.cc/detail/1548841674.html",  # 脚踏实地的努力就是开挂
    "https://www.esjzone.cc/detail/1546090764.html",  # 转生成为自己前世的妹妹
    "https://www.esjzone.cc/detail/1549259030.html",  # 会读漫画的我是异世界最强
    "https://www.esjzone.cc/detail/1548327954.html",  # 在边境悠闲地度日
    "https://www.esjzone.cc/detail/1554475707.html",  # 闪亮的魔像
    "https://www.esjzone.cc/detail/1547022886.html",  # 肥宅勇者
    "https://www.esjzone.cc/detail/1554475896.html",  # 不变者闪亮的魔像 (第二部)
    "https://www.esjzone.cc/detail/1549534022.html",  # VRMMO学园的愉快魔改
    "https://www.esjzone.cc/detail/1543304565.html",  # 我的宠物是圣女大人
    "https://www.esjzone.cc/detail/1550591055.html",  # 弑神的英雄与七个誓约
    "https://www.esjzone.cc/detail/1550682586.html",  # 被舍弃的勇者的英雄坛
    "https://www.esjzone.cc/detail/1556528574.html",  # 随机召唤
    "https://www.esjzone.cc/detail/1543763168.html",  # 天启的异世界转生谭
    "https://www.esjzone.cc/detail/1545633667.html",  # 圣者无双
    "https://www.esjzone.cc/detail/1542934121.html",  # gm登入到异世界
    "https://www.esjzone.cc/detail/1548595935.html",  # 我和孤零零的她们
    "https://www.esjzone.cc/detail/1544279828.html",  # 破坏之御子
    "https://www.esjzone.cc/detail/1543764353.html",  # 异世界料理道
    "https://www.esjzone.cc/detail/1546368296.html",  # 普通抽奖也能拯救世界吗
    "https://www.esjzone.cc/detail/1555320317.html",  # 御宅女，转生为恶役千金
    "https://www.esjzone.cc/detail/1547094449.html",  # 魔王和女勇者的母亲再婚
    "https://www.esjzone.cc/detail/1550308150.html",  # 讨厌第四次的死属性魔术师
    "https://www.esjzone.cc/detail/1546094093.html",  # 转生从上位世界到下位世界
    "https://www.esjzone.cc/detail/1544282535.html",  # 想要成为影之实力者
    "https://www.esjzone.cc/detail/1553364118.html",  # 等级1的最强贤者
    "https://www.esjzone.cc/detail/1549257107.html",  # 雷帝的女仆
    "https://www.esjzone.cc/detail/1543647429.html",  # 大器晚成的冒险者
    "https://www.esjzone.cc/detail/1549169900.html",  # 转生魅魔的榨乳日常
    "https://www.esjzone.cc/detail/1543763751.html",  # Only Sense Online 绝对神境
    "https://www.esjzone.cc/detail/1548510239.html",  # 靠钱的力量驰骋于战国乱世
    "https://www.esjzone.cc/detail/1547096103.html",  # 异世界孤儿院
    "https://www.esjzone.cc/detail/1543764940.html",  # NO FATIGUE 战斗24小时的男人的转生谭
    "https://www.esjzone.cc/detail/1544079590.html",  # 无欲圣女
    "https://www.esjzone.cc/detail/1545676746.html",  # 在异世界购买土地建造农场
    "https://www.esjzone.cc/detail/1550913545.html",  # 为了供养精灵而潜入迷宫
    "https://www.esjzone.cc/detail/1550572270.html",  # 虫虫酱
    "https://www.esjzone.cc/detail/1546091491.html",  # 成为了勇者的母亲
    "https://www.esjzone.cc/detail/1550590267.html",  # 佣兵物语之纯粹的叛逆者
    "https://www.esjzone.cc/detail/1550107034.html",  # 十岁的最强魔导师
    "https://www.esjzone.cc/detail/1545674180.html",  # 重装大小姐玛娜特〜解除他人魔咒的方法〜
    "https://www.esjzone.cc/detail/1548246397.html",  # 月桂树之歌
    "https://www.esjzone.cc/detail/1544265729.html",  # 乙女游戏世界对路人角色太严厉
    "https://www.esjzone.cc/detail/1552055348.html",  # 看起来等级是0
    "https://www.esjzone.cc/detail/1543303989.html",  # 没落预订
    "https://www.esjzone.cc/detail/1546223076.html",  # 异世界转生骚动记
    "https://www.esjzone.cc/detail/1547024145.html",  # 为鲜血献上吻
    "https://www.esjzone.cc/detail/1547286247.html",  # 折断逆后宫旗标
    "https://www.esjzone.cc/detail/1547286560.html",  # 自称转生者的恶役令媛
    "https://www.esjzone.cc/detail/1552053324.html",  # Cheese
    "https://www.esjzone.cc/detail/1543764936.html",  # 圣女的魔力是万能的
    "https://www.esjzone.cc/detail/1546618252.html",  # 怕痛少女的防御特化
    "https://www.esjzone.cc/detail/1544271664.html",  # 暗黑骑士物语
    "https://www.esjzone.cc/detail/1548734437.html",  # 运用开挂魔术扭转命运
    "https://www.esjzone.cc/detail/1550914310.html",  # 原最强玩家在异世界成为最强
    "https://www.esjzone.cc/detail/1544272723.html",  # 异世界人的指南书
    "https://www.esjzone.cc/detail/1548946126.html",  # 驱除人-驱除者
    "https://www.esjzone.cc/detail/1549007916.html",  # 回复术士重来人生
    "https://www.esjzone.cc/detail/1543763301.html",  # 精灵幻想记
    "https://www.esjzone.cc/detail/1543764573.html",  # 现实主义勇者的王国再建记
    "https://www.esjzone.cc/detail/1548841674.html",  # 脚踏实地的努力就是开挂
    "https://www.esjzone.cc/detail/1546090764.html",  # 转生成为自己前世的妹妹
    "https://www.esjzone.cc/detail/1549259030.html",  # 会读漫画的我是异世界最强
    "https://www.esjzone.cc/detail/1548327954.html",  # 在边境悠闲地度日
    "https://www.esjzone.cc/detail/1554475707.html",  # 闪亮的魔像
    "https://www.esjzone.cc/detail/1547022886.html",  # 肥宅勇者
    "https://www.esjzone.cc/detail/1554475896.html",  # 不变者闪亮的魔像 (第二部)
    "https://www.esjzone.cc/detail/1549534022.html",  # VRMMO学园的愉快魔改
    "https://www.esjzone.cc/detail/1543304565.html",  # 我的宠物是圣女大人
    "https://www.esjzone.cc/detail/1550591055.html",  # 弑神的英雄与七个誓约
    "https://www.esjzone.cc/detail/1550682586.html",  # 被舍弃的勇者的英雄坛
    "https://www.esjzone.cc/detail/1556528574.html",  # 随机召唤
    "https://www.esjzone.cc/detail/1543763168.html",  # 天启的异世界转生谭
    "https://www.esjzone.cc/detail/1545633667.html",  # 圣者无双
    "https://www.esjzone.cc/detail/1542934121.html",  # gm登入到异世界
    "https://www.esjzone.cc/detail/1548595935.html",  # 我和孤零零的她们
    "https://www.esjzone.cc/detail/1544279828.html",  # 破坏之御子
    "https://www.esjzone.cc/detail/1543764353.html",  # 异世界料理道
    "https://www.esjzone.cc/detail/1546368296.html",  # 普通抽奖也能拯救世界吗
    "https://www.esjzone.cc/detail/1555320317.html",  # 御宅女，转生为恶役千金
    "https://www.esjzone.cc/detail/1547094449.html",  # 魔王和女勇者的母亲再婚
    "https://www.esjzone.cc/detail/1550308150.html",  # 讨厌第四次的死属性魔术师
    "https://www.esjzone.cc/detail/1546094093.html",  # 转生从上位世界到下位世界
    "https://www.esjzone.cc/detail/1544282535.html",  # 想要成为影之实力者
    "https://www.esjzone.cc/detail/1553364118.html",  # 等级1的最强贤者
    "https://www.esjzone.cc/detail/1549257107.html",  # 雷帝的女仆
    "https://www.esjzone.cc/detail/1543647429.html",  # 大器晚成的冒险者
    "https://www.esjzone.cc/detail/1549169900.html",  # 转生魅魔的榨乳日常
    "https://www.esjzone.cc/detail/1543763751.html",  # Only Sense Online 绝对神境
    "https://www.esjzone.cc/detail/1548510239.html",  # 靠钱的力量驰骋于战国乱世
    "https://www.esjzone.cc/detail/1547096103.html",  # 异世界孤儿院
    "https://www.esjzone.cc/detail/1543764940.html",  # NO FATIGUE 战斗24小时的男人的转生谭
    "https://www.esjzone.cc/detail/1544079590.html",  # 无欲圣女
    "https://www.esjzone.cc/detail/1545676746.html",  # 在异世界购买土地建造农场
    "https://www.esjzone.cc/detail/1550913545.html",  # 为了供养精灵而潜入迷宫
    "https://www.esjzone.cc/detail/1550572270.html",  # 虫虫酱
    "https://www.esjzone.cc/detail/1546091491.html",  # 成为了勇者的母亲
    "https://www.esjzone.cc/detail/1550590267.html",  # 佣兵物语之纯粹的叛逆者
    "https://www.esjzone.cc/detail/1550107034.html",  # 十岁的最强魔导师
}
