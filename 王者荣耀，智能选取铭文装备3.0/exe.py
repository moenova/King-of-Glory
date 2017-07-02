#这是一个通用的装备选择工具
from equipment import*
from rune import*
from hero import*
from utility import*
from skill import*

#主要方向为，最大实际伤害（普攻，技能），抗打击时间，吸血，移速等
#填写技能
s1 = Skill(name="", base=0,additional=0, addType = "", damType= "" ,cd =0, last=0, accuracy =1, rate=0)
s2 = Skill(name="", base=0,additional=0, addType = "", damType= "" ,cd =0, last=0, accuracy =1, rate=0)
s3 = Skill(name="", base=0,additional=0, addType = "", damType= "" ,cd =0, last=0, accuracy =1, rate=0)
#注我方入英雄
self = Hero(name = "", kind="", level = 0 ,\
                 pd=0,md=0, s=0, r=0, i=0, \
                 pp=0, mp=0, pa=0, ma =0, \
                 hp =0, pvam=0, mvam=0,rcd =0,move=0 ,skills=[] )

#注入铭文和装备
蓝色铭文 = []
绿色铭文 = []
红色铭文 = []
装备 = []


#注入敌方英雄

#注入敌方英雄装备（主要填破甲）


#选取最大实际伤害/吸血

