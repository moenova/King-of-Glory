from utility import*


#铭文：

class Rune:
    def __init__(self, name = "", kind="", level = 0 ,\
                 pd=0,md=0, s=0, r=0, i=0, pp=0,\
                 mp=0, pa=0, ma =0, hp =0, rhp =0,\
                 rcd =0, pvam=0, mvam=0, move= 0 ):
        """
        name: 名字
        kind:  类型： 红色，绿色，蓝色
        level: 等级
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
        self.level = level
        self.pd = pd
        self.md =md
        self.s = s
        self.r =  r
        self.i = i
        self.pp = pp
        self.mp = mp
        self.pa =pa
        self.ma =ma
        self.hp = hp
        self.pvam= pvam
        self.mvam = mvam
        self.move = move
        self.rcd =rcd
        self.rhp = rhp

    def __lt__(self,other):
        if self.level == other.level:
            return self.name<other.name
        else:
            return self.level<other.level

    def __gt__(self,other):
        if self.level == other.level:
            return self.name>other.name
        else:
            return self.level>other.level

    def __eq__(self,other):
        return self.level == other.level and self.name == other.name



#铭文注入：
#IV
#红色
衰败 = Rune(name= "衰败", kind = "红色",level =4, s = cent(1.2))
暴戾 = Rune(name= "暴戾", kind = "红色",level =4, pd = 1.5, hp = 13.5)
荆棘 = Rune(name= "荆棘", kind = "红色",level =4, pd = 1.5, s= cent(0.4))
风暴 = Rune(name= "风暴", kind = "红色",level =4, s = cent(0.6), r = cent(0.3),i = cent(1.1))
戒律 = Rune(name= "戒律", kind = "红色",level =4, md = 2.5, r = cent(0.3))
阳炎 = Rune(name= "阳炎", kind = "红色",level =4, md = 2.5, mp = 1.4)
惩戒= Rune(name= "惩戒", kind = "红色",level =4, i = cent(1))
狂热 = Rune(name= "狂热", kind = "红色",level =4,  r = cent(0.5), i = cent(2))

#绿色
铁躯 = Rune(name= "铁躯", kind = "绿色",level =4, pa =5.4)
无畏 = Rune(name= "无畏", kind = "绿色",level =4,  ma =5.4)
奇袭 = Rune(name= "奇袭", kind = "绿色",level =4, s = cent(0.4), rcd= cent(0.5))
庇护 = Rune(name= "庇护", kind = "绿色",level =4,  rhp = 4.5, pa = 3.2)
憎恶 = Rune(name= "憎恶", kind = "绿色",level =4, mvam = cent(0.5), ma = 3.2)
侵蚀 = Rune(name= "侵蚀", kind = "绿色",level =4,  md = 0.9, mp = 3.8)
潜能 = Rune(name= "潜能", kind = "绿色",level =4, hp = 15.7,rhp = 3.1, rcd = cent(0.3))
野性 = Rune(name= "野性", kind = "绿色",level =4,  hp = 13.5,  pp =3.8)
#蓝色
气数 = Rune(name= "气数", kind = "蓝色",level =4,  hp = 45)
刹那 = Rune(name= "刹那", kind = "蓝色",level =4,  hp =13.5, move = cent(0.7))
复苏 = Rune(name= "复苏", kind = "蓝色",level =4,  rhp = 9)
渴血 = Rune(name= "渴血", kind = "蓝色",level =4,  md = 1.4,mvam = cent(0.8), ma = 1.6)
吞噬 = Rune(name= "吞噬", kind = "蓝色",level =4,  s = cent(0.4), pvam = cent(0.8))
正义 = Rune(name= "正义", kind = "蓝色",level =4,  pd = 0.6, hp = 36)
滋生 = Rune(name= "滋生", kind = "蓝色",level =4,  hp = 36, pa = 1.6)
急救 = Rune(name= "急救", kind = "蓝色",level =4,  s = cent(0.4), r = cent(0.3), move = cent(0.5))
#V
#红色
圣人 = Rune(name= "圣人", kind = "红色",level =5, pd = 3.2)
传承 = Rune(name= "传承", kind = "红色",level =5, pd = 3.2)
异变 = Rune(name= "异变", kind = "红色" ,level =5,pd=2.00, pp = 3.6 )
纷争 = Rune(name= "纷争", kind = "红色",level =5, pd = 2.5, pvam = cent(0.5))
无双 = Rune(name= "无双", kind = "红色" ,level =5,r=cent(0.7),i=cent(3.6))

红月 = Rune(name= "红月", kind = "红色", level =5,s= cent(1.6),  r=cent(0.5))

祸源 = Rune(name= "祸源", kind = "红色" ,level =5,r=cent(1.6))
宿命 = Rune(name= "宿命", kind = "红色",level =5, s = cent(1), hp = 33.7, pa = 2.3)
梦魇 = Rune(name= "梦魇", kind = "红色",level =5, md = 4.2, mp = 2.4)
凶兆 = Rune(name= "凶兆", kind = "红色",level =5, md = 4.2, s = cent(0.6))


#绿色

鹰眼 = Rune(name= "鹰眼", kind = "绿色" ,level =5, pd=0.9, pp = 6.4 )
心眼 = Rune(name= "心眼", kind = "绿色" , level =5,s = cent(0.6) )
霸者 = Rune(name= "霸者", kind = "绿色" ,level =5, pa = 9 )
均衡 = Rune(name= "均衡", kind = "绿色" ,level =5, pa =5, ma = 5 )
虚空 = Rune(name= "虚空", kind = "绿色" ,level =5, hp = 37.5, rcd = cent(0.6) )
灵山 = Rune(name= "灵山", kind = "绿色" ,level =5, ma = 9 )
献祭 = Rune(name= "献祭", kind = "绿色" ,level =5, md=2.4, rcd = cent(0.7) )
怜悯 = Rune(name= "怜悯", kind = "绿色" ,level =5, rcd = cent(1) )
敬畏 = Rune(name= "敬畏", kind = "绿色" ,level =5, mvam = cent(0.7), pa = 5.9 )
回声 = Rune(name= "回声", kind = "绿色" ,level =5, pa=2.7, ma = 2.7, rcd = cent(0.6) )

#蓝色
隐匿 = Rune(name= "隐匿", kind = "蓝色" ,level =5,pd=1.6)
兽痕 = Rune(name= "兽痕", kind = "蓝色" , level =5,r=cent(0.5))
狩猎 = Rune(name= "狩猎", kind = "蓝色" ,level =5, s = cent(1))

长生 = Rune(name= "长生", kind = "蓝色" ,level =5, hp =75)
贪婪 = Rune(name= "贪婪", kind = "蓝色" ,level =5, mvam = cent(1.6))
夺萃 = Rune(name= "夺萃", kind = "蓝色" ,level =5, pvam = cent(1.6))
冥想 = Rune(name= "冥想", kind = "蓝色" ,level =5, hp = 60, rhp =4.5)
繁荣 = Rune(name= "繁荣", kind = "蓝色" ,level =5, pvam = cent(1), ma = 4.1)
轮回 = Rune(name= "轮回", kind = "蓝色" ,level =5, md = 2.4,  mvam =cent(1))
调和 = Rune(name= "调和", kind = "蓝色" ,level =5, hp =45, rhp =5.2, move = cent(0.4))

#铭文导入列表：

r4 = [衰败,暴戾,荆棘,风暴,戒律,阳炎,惩戒,狂热]
g4 = [铁躯,无畏,奇袭,庇护,憎恶,侵蚀,潜能,野性]
b4 = [气数,刹那,复苏,渴血,吞噬,正义,滋生,急救]

r5 = [圣人,传承,异变,纷争,无双,红月,祸源,宿命,梦魇,凶兆]
g5 =  [鹰眼,心眼,霸者,均衡,虚空,灵山,献祭,怜悯,敬畏,回声]
b5 = [隐匿,兽痕,狩猎,长生,贪婪,夺萃,冥想,繁荣,轮回,调和]

Runes = r5+g5+b5+r4+g4+b4


Runes_d = {}
for rune in Runes:
    Runes_d[rune.name] = rune


红色= [传承, 异变,无双,祸源,红月,纷争 ]
绿色 = [鹰眼]
蓝色 = [隐匿, 兽痕,狩猎,夺萃]
RLusing = 红色+绿色+蓝色



    

if __name__ == "__main__":
    #print(sumf(Runes, "level"))
    print(RDusing)


