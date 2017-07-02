from utility import*

#装备：

class Equipment:
    def __init__(self, name= "", kind= "", cost = 0, \
                 pd=0,md=0, s=0, r=0, i=0,\
                 pp=0, mp=0, pa=0, ma =0, \
                 hp =0, rcd=0, pvam=0, mvam =0, move=0):
        """
        name: 名字
        kind:  类型： 攻击，法术，防御，移动，打野
        cost: 价格
        pd:  物理攻击
        md: 法术攻击
        s: 攻击速度
        r: 暴击率
        i: 暴击效果
        pp: 物理穿透
        mp: 法术穿透
        pa: 物理防御
        ma: 法术防御
        hp: 血条
        pvam: 物理吸血
        mvam: 法术吸血
        rcd: 冷却减缩
        move: 移速加成

        
        """
        self.name = name
        self.kind = kind
        self.cost = cost
        self.pd = pd
        self.md =md
        self.s = s
        self.r =  r
        self.i = i
        self.pp = pp
        self.mp = mp
        self.pa =pa
        self.ma =ma
        self.pvam = pvam
        self.mvam = mvam
        self.move = move
        self.hp = hp
        self.rcd = rcd

    def __lt__(self,other):
        if self.cost == other.cost:
            return self.name<other.name
        else:
            return self.cost<other.cost

    def __gt__(self,other):
        if self.cost == other.cost:
            return self.name>other.name
        else:
            return self.cost>other.cost

    def __eq__(self,other):
        return self.cost == other.cost and self.name == other.name


#装备注入：
#攻击：
破魔刀 = Equipment( name= "破魔刀", kind = "攻击", cost=2000,               pd=100         )
名刀·司命 = Equipment( name= "名刀·司命", kind = "攻击", cost=1760,        pd=60       )
冰霜长矛 = Equipment( name= "冰霜长矛", kind = "攻击", cost=1980,         pd=80,hp=600         )
破甲弓 = Equipment( name= "破甲弓",  kind = "攻击",cost=2100,               pd=80            )
制裁之刃 = Equipment( name= "制裁之刃",  kind = "攻击",cost=1800,         pd=100     ,pvam =cent(10)  )
末世 = Equipment( name= "末世",  kind = "攻击",cost=2160,                 pd=60, s=cent(30)  ,pvam =cent(10) )
泣血之刃= Equipment( name= "泣血之刃", kind = "攻击",cost=1740,           pd=100  ,pvam =cent(25)   )
无尽战刃 = Equipment( name= "无尽战刃",kind = "攻击", cost=2140,              pd=100,  r=0.2, )
宗师之力 = Equipment( name= "宗师之力", kind = "攻击", cost=2100,         pd=60, r=0.2, hp =400 )
闪电匕首 = Equipment( name= "闪电匕首",kind = "攻击",  cost=1840,        s=0.3, r=0.2 )
影刃 = Equipment( name= "影刃",  kind = "攻击",cost=2070,                      s=0.4, r=0.1,)
暗影战斧= Equipment( name= "暗影战斧", kind = "攻击", cost=2090,              pd=85, hp =500)
破军 = Equipment( name= "破军", kind = "攻击", cost=2950,                             pd=200, )
逐日之弓 = Equipment( name= "逐日之弓",  kind = "攻击",cost=2100,                  pd=40, s=0.20, r=0.15, )
纯净苍穹 = Equipment( name= "纯净苍穹", kind = "攻击", cost=2230,                  s=0.30, r=0.2,)

#法术：
圣杯 = Equipment( name= "圣杯", kind = "法术", cost=2030,               md=140, ma=140, rcd=cent(20)         )
虚无法杖 =Equipment( name= "虚无法杖", kind = "法术", cost=2110,               md=180, hp = 500         )
博学者之怒 =Equipment( name= "博学者之怒", kind = "法术", cost=2300,               md=240        )
回响之仗 =Equipment( name= "回响之仗", kind = "法术", cost=2100,               md=240         )
冰霜法杖 =Equipment( name= "冰霜法杖", kind = "法术", cost=2100,               md=150, hp = 1050         )
痛苦面具 =Equipment( name= "痛苦面具", kind = "法术", cost=2040,               md=140, hp = 500, rcd = cent(5)         )
巫术法杖 =Equipment( name= "巫术法杖", kind = "法术", cost=2120,               md=120, hp = 400         )
时之预言 =Equipment( name= "时之预言", kind = "法术", cost=2090,               md=160, hp = 800         )
贤者之书 =Equipment( name= "贤者之书", kind = "法术", cost=2990,               md=400,        )
辉月=Equipment( name= "辉月", kind = "法术", cost=2990,               md=160, rcd = cent(10)         )
噬神之书 =Equipment( name= "噬神之书", kind = "法术", cost=2090,               md=180, hp = 800, rcd = cent(10)         )
梦魇之牙 =Equipment( name= "梦魇之牙", kind = "法术", cost=2050,               md=240         )
炽热支配者 =Equipment( name= "炽热支配者", kind = "法术", cost=1950,               md=160         )
#防御：
反伤刺甲 =Equipment( name= "反伤刺甲", kind = "防御", cost=1840,               pd=40, pa=420         )
红莲斗篷 =Equipment( name= "红莲斗篷", kind = "防御", cost=1830,               pa=240, hp = 1200         )
霸者重装 =Equipment( name= "霸者重装", kind = "防御", cost=2370,               hp=2000  )
不详征兆 =Equipment( name= "不详征兆", kind = "防御", cost=2180,               pa= 270, hp = 1200        )
不死鸟之眼 =Equipment( name= "不死鸟之眼", kind = "防御", cost=2100,        ma =240, hp = 1200         )
魔女斗篷 =Equipment( name= "魔女斗篷", kind = "防御", cost=2120,               ma =360, hp =1000         )
极寒风暴 =Equipment( name= "极寒风暴", kind = "防御", cost=2100, rcd = 0.2, pa= 360         )
贤者的庇护 =Equipment( name= "贤者的庇护", kind = "防御", cost=2080,pa=140, ma =140         )
冰痕之握 =Equipment( name= "冰痕之握", kind = "防御", cost=2020,      rcd =0.1, pa =200, hp = 800        )


#移动：
影忍之足 =Equipment( name= "影忍之足", kind = "移动", cost=690,      pa =110        )
抵抗之靴 =Equipment( name= "抵抗之靴", kind = "移动", cost=690,      rcd =110        )
冷静之靴 =Equipment( name= "冷静之靴", kind = "移动", cost=710,      rcd =0.1        )
秘法之靴 =Equipment( name= "秘法之靴", kind = "移动", cost=790,      )
急速战靴 =Equipment( name= "急速战靴", kind = "移动", cost=710,      s=0.15        )
#打野
符文大剑 = Equipment( name= "符文大剑",  kind = "打野",cost=1490,   md=240 )
巨人之握 = Equipment( name= "巨人之握",  kind = "打野",cost=1500,   hp = 1850 )
贪婪之噬 = Equipment( name= "贪婪之噬", kind = "打野", cost=1460,                 pd=45, s=0.42)


#装备导入列表：
攻击 = [破魔刀,名刀·司命,冰霜长矛, 破甲弓, 制裁之刃, 末世, 泣血之刃, 无尽战刃, 宗师之力, 闪电匕首, 影刃, 暗影战斧, 破军, 逐日之弓, 纯净苍穹]
法术 =[圣杯,虚无法杖,博学者之怒,回响之仗,冰霜法杖, 痛苦面具,巫术法杖,时之预言,贤者之书,辉月,噬神之书,梦魇之牙,炽热支配者]
防御 = [反伤刺甲,红莲斗篷,霸者重装,不详征兆, 不死鸟之眼,魔女斗篷,极寒风暴,贤者的庇护, 冰痕之握]
移动 =[影忍之足,抵抗之靴,冷静之靴,秘法之靴,急速战靴]
打野 =[符文大剑,  巨人之握, 贪婪之噬]

Equipments = 攻击+法术+防御+移动+打野

#Eusing = ["破甲弓", "末世","无尽战刃","宗师之力","闪电匕首","影刃","暗影战斧","破军","纯净苍穹","逐日之弓", "贪婪之噬"]
Eusing = ["破甲弓", "末世","无尽战刃","影刃","暗影战斧","破军","纯净苍穹","逐日之弓","贪婪之噬","宗师之力","闪电匕首"]

Equips_d ={}
for equipment in Equipments:
    Equips_d[equipment.name] = equipment

