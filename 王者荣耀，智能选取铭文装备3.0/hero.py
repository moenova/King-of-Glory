from utility import*
from rune import*
from equipment import*
from skill import*

class Hero:
    def __init__(self, name = "", kind="", level = 0 ,\
                 pd=0,md=0, s=0, r=0, i=0, pp=0, mp=0,pa=0, ma =0,\
                 hp =0, pvam=0, mvam=0,rcd =0,move=0 ,skills=[] ):
        """
        name: 名字
        kind:  类型： 坦克，战士，刺客，法师，射手
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
        move: 移动速度
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
        self.pa = pa
        self.ma = ma
        self.pvam = pvam
        self.mvam =mvam
        self.rcd = rcd
        self.move = move
        self.hp = hp
        self.runes = {"红色":[],"绿色":[],"蓝色":[]}
        self.equips = {"攻击":[], "法术":[],  "防御":[]  ,"移动":[], "打野" :[]}
        # skills: [skill0,skill1,skill2,skill3] calculation will be done in the orders
        # 如果爆发计算可以在 skill3 后加 skill1
        #skill0,是被动，需要建造skill类，但可以不定义内容
        self.skills = skills
        skillrates(self.skills)

    def getvalue(self, s):
        return eval("self."+s)+sum_runes_f(self.runes, s) +sum_equips_f(self.equips, s)

    def __lt__(self, other):
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


# 铭文满格判断
    def red(self):
        return len(self.runes["红色"])<10
        
    def green(self):
        return len(self.runes["绿色"])<10

    def blue(self):
        return len(self.runes["蓝色"])<10

#装备个数判断
    def enum(self):
        return sum(   [    len(self.equips[key])     for key in self.equips    ]  )

#加铭文
    def add_a_rune(self, rune):
        #if rune.kind == ("红色" or "绿色" or "蓝色"):
        self.runes[rune.kind].append(rune)

#加一串铭文
    def add_runes(self, slist):
        for s in slist:
            if ((Runes_d[s].kind == "红色" and self.red()) or
                (Runes_d[s].kind == "绿色" and self.green()) or
                (Runes_d[s].kind == "蓝色" and self.blue())):
                if s in Runes_d:
                    self.runes[       Runes_d[s].kind         ].append(       Runes_d[s]      )
                else:
                    raise Exception("铭文名字有误！或还没有添加该铭文，请在rune.py 中添加")

#加装备
    def add_a_equip(self, equip):
        if equip.kind in self.equips:
            self.equips[equip.kind].append(equip)

#加一串装备
    def add_equips(self, slist):
        for s in slist:
            if self.enum()<6:
                if s in Equips_d:
                    self.equips[            Equips_d[s].kind           ].append(        Equips_d[s]       )
                else:
                    raise Exception("装备名字有误！或还没有添加该装备，请在equipment.py 中添加")

#有唯一被动装备：
    def have_the_equip(self, s):
        #注意武器名称中间不能有空格！
        #首末空格已自动去除
        for k in self.equips:
            for e in self.equips[k]:
                if e.name == s.strip():
                    return True
        return False
                    
#计算实际伤害
    def real_attack_damage(self,target, with_equips= True, with_runes =True, after_skill=False, kind = "实际伤害",index = 0.885,ms=cent(4) ):
        """
    
        """
        pd = self.pd
        s = self.s
        r =  self.r
        i = self.i
        pp = self.pp
        mp = self.mp
        pa =target.pa
        ma =target.ma
        hp = target.hp
        pvam = self.pvam
        #print(pvam)
        mvam = self.mvam
        rcd = self.rcd
        if not with_runes:
            #原始数值
            rpd = pd*s*index*(r*i-r+1)*arm2dam(pa-pp)
            rblood = (rpd)*pvam
            if kind == "物理吸血":
                return rblood
            elif kind == "实际伤害":
                return rpd
        else:
            pd += sum_runes_f(self.runes, "pd")
            s += sum_runes_f(self.runes, "s")
            r += sum_runes_f(self.runes, "r")
            i += sum_runes_f(self.runes, "i")
            pp += sum_runes_f(self.runes, "pp")
            pvam += sum_runes_f(self.runes, "pvam")
            mvam += sum_runes_f(self.runes, "mvam")
            rcd += sum_runes_f(self.runes, "rcd")
        if not with_equips:
            #原始数值+铭文
            rpd = pd*s*index*(r*i-r+1)*arm2dam(pa-pp)
            rblood = (rpd)*pvam
            if kind == "物理吸血":
                return rblood
            elif kind == "实际伤害":
                return rpd
        else:
            pd += sum_equips_f(self.equips, "pd")
            s += sum_equips_f(self.equips, "s")
            r += sum_equips_f(self.equips, "r")
            i += sum_equips_f(self.equips, "i")
            pp += sum_equips_f(self.equips, "pp")
            mp += sum_equips_f(self.equips, "mp")
            pvam += sum_equips_f(self.equips, "pvam")
            mvam += sum_equips_f(self.equips, "mvam")
            rcd += sum_equips_f(self.equips, "rcd")
            #最值调控：
            if s>3: s =3
            if r>1: r =1
            if rcd>0.4: rcd = 0.4
            if pvam>1: pvam =1
            if mvam>1: mvam =1
            #开始唯一被动计算
            if self.have_the_equip("暗影战斧"):
                pp =pp+ 50 + 10*self.level
            #rpa: real physics armor
            rpa = pa - pp
            if self.have_the_equip("破甲弓"):
                rpa = (1- 0.45)*rpa
            if self.have_the_equip("秘法之靴"):
                mp+= 75
            if self.have_the_equip("痛苦面具"):
                mp+= 75
            # rma: real magic armor
            rma = ma - mp
            if self.have_the_equip("虚无法杖"):
                rma  = rma*(1-0.45)
            if self.have_the_equip("无尽战刃"):
                i +=0.5
            #print("暴击效果：", i)
            #bpd: buff physics damage
            bpd = 0
            if self.have_the_equip("巫术法杖"):
                bpd +=pd*cent(30) 
            if after_skill and self.have_the_equip("宗师之力"):
                bpd += pd
            if self.have_the_equip( "纯净苍穹"):
                bpd += 72
            if self.have_the_equip("末世"):
                bpd += ms*hp

            if self.have_the_equip("影刃"):
                if after_skill:
                    s= s*r +(s+0.5)*(1-r)
                else:
                    drop = (1-r)**(2*s+1)
                    s = s*drop+ (1-drop)*(s+0.5)
            if s>3: s =3
            #rpd: real physics damage
            #rmd: real magic damage
            rpd = pd*(   1-r + r*i   )*arm2dam(rpa)+bpd*arm2dam(rpa)
            #sentence="物理攻击：{}\n暴击效益：{}\n减伤系数：{}\n物理伤害加成：{}\n".format(pd, (   1-r + r*i   ), arm2dam(rpa),bpd)
            #print(sentence)
            rmd =0
            if self.have_the_equip("红莲斗篷"):
                rmd += 100*arm2dam(ma)
            #重要： after skill 计算一次伤害不算攻速
            if not after_skill:
                #print("攻击速度：{}\n速度系数：{}\n".format(s,index))
                #(   1-r + r*i   )*arm2dam(rpa)*
                #print("计算：{}".format(pd*s*index))
                rpd=rpd*s*index
            #brmd: buff real magic damage
            #brpd: buff real physics damage
            brmd = 0
            brpd = 0
            if self.have_the_equip("博学者之怒"):
                brmd += rmd*cent(35)
            if self.have_the_equip("破军"):
                brpd += rpd * cent(15)
                brmd += rmd*cent(15)
            rpd += brpd
            rmd+= brmd
            """
            if self.have_the_equip( "闪电匕首"):
                #这里就不考虑法术穿透了，物理英雄不会有的
                if s*index<2:
                    #rmd: real magic damage
                    rmd += 20*s*index(   r*i     +  (1-r)   )*arm2dam(ma)
                else:
                    rmd += 40*s*(   r*i     +  (1-r)   )*arm2dam(ma)
            """

                    
            rblood = (rpd)*pvam
            rd = rpd+rmd
            if kind == "物理吸血":
                return rblood
            elif kind == "实际伤害":
                return rd

    def real_skill_damage(self, target, skill, with_equips= True, with_runes =True, after_a_while =True, kind="实际伤害"):
        pd = self.pd
        md =self.ma
        s = self.s
        r =  self.r
        i = self.i
        pp = self.pp
        mp = self.mp
        pa =target.pa
        ma =target.ma
        hp = target.hp
        pvam = self.pvam
        mvam = self.mvam
        rcd = self.rcd
        
        #定义技能伤害函数
        # skilldamage(skill.base,skill.additional, pd, md, rpa, rma, skill.damType, skill.addType, pvam, mvam, kind)
        def skilldamage(basic, add, pd, md, rpa_, rma_, dType, aType, pvam_, mvam_, kind):
            rpd = 0
            rmd = 0
            if dtype == "物理" and aType == "物理":
                    rpd = (basic+add*pd)*arm2dam(rpa_)
            elif dType == "法术":
                if aType == "物理":
                    rmd= (basic+add*pd)*arm2dam(rma_)
                elif aType == "法术":
                    rmd = (basic+add*md)*arm2dam(rma_)
            else:
                raise Exception("unknown damType, addType combination")
            if kind == "物理吸血":
                return rpd*pvam_
            elif kind == "法术吸血":
                return rmd*mvam_
            elif kind =="实际伤害":
                return rpd+rmd
        #完成定义
        if not with_runes:
            #原始数值
            result = skilldamage(skill.base,skill.additional, pd, md, rpa, rma, skill.damType, skill.addType, pvam, mvam, kind)
            return result
        else:
            pd += sum_runes_f(self.runes, "pd")
            md += sum_runes_f(self.runes, "md")
            s += sum_runes_f(self.runes, "s")
            r += sum_runes_f(self.runes, "r")
            i += sum_runes_f(self.runes, "i")
            pp += sum_runes_f(self.runes, "pp")
            mp += sum_runes_f(self.runes, "mp")
            pvam += sum_runes_f(self.runes, "pvam")
            mvam += sum_runes_f(self.runes, "mvam")
            rcd += sum_runes_f(self.runes, "rcd")
        if not with_equips:
            #原始数值+铭文
            result =  skilldamage(skill.base,skill.additional, pd, md, rpa, rma, skill.damType, skill.addType, pvam, mvam, kind)
            return result
        else:
            pd += sum_equips_f(self.equips, "pd")
            md += sum_equips_f(self.equips, "md")
            s += sum_equips_f(self.equips, "s")
            r += sum_equips_f(self.equips, "r")
            i += sum_equips_f(self.equips, "i")
            pp += sum_equips_f(self.equips, "pp")
            mp += sum_equips_f(self.equips, "mp")
            pvam += sum_equips_f(self.equips, "pvam")
            mvam += sum_equipss_f(self.equips, "mvam")
            rcd += sum_equips_f(self.equips, "rcd")
            #开始唯一被动计算
            #rpd : real physics damge
            #rmd: real magic damage
            #rtd: real truely damage
            if self.have_the_equip("暗影战斧"):
                pp =pp+ 50 + 10*self.level
            #rpa : real physics armor
            rpa = pa - pp
            if self.have_the_equip("破甲弓"):
                rpa = (1- 0.45)*rpa
            if self.have_the_equip("无尽战刃"):
                i+= 0.5
            if self.have_the_equip("秘法之靴"):
                mp+= 75
            if self.have_the_equip("痛苦面具"):
                mp+= 75
            # rma: real magic armor
            rma = ma - mp
            if self.have_the_equip("虚无法杖"):
                rma  = rma*(1-0.45)

###########################################################以下内容有待修改
#addtype     damagetype
# 物理           物理
# 法术          法术
#物理       法术
#物理     真实         暂不考虑
            rpd =0
            rmd = 0
            if skill.damType =="物理" and skill.addType == "物理":
                    rpd += (skill.base+skill.additional*pd)*arm2dam(rpa)
            if skill.damType == "法术":
                if skill.addType == "物理":
                    rmd += (skill.base+skill.additional*pd)*arm2dam(rma)
                elif skill.addType == "法术":
                    rmd += (skill.base+skill.additional*md)*arm2dam(rma)
            if after_a_while and self.have_the_equip("回响之仗"):
                    rmd += (50+0.5*md)*arm2dam(rma)
            if after_a_while and self.have_the_equip("痛苦面具"):
                rmd += target.hp*cent(4)*arm2dam(rma)
            if self.have_the_equip("博学者之怒"):
                    rmd +=cent(35)
            if self.have_the_equip("破军"):
                    rpd +=rpd*cent(15)
                    rmd+= rmd*cent(15)
            if kind == "物理吸血":
                return rpd*pvam
            elif kind == "法术吸血":
                return rmd*mvam
            elif kind =="实际伤害":
                return rpd+rmd
                    
    def real_damage_resistance(self, target,px=0, mx=0):
        #直接一起算了
        #px和mx是简化后的实际伤害包括概率，因为无论对方的px和mx多大，装备防御的抗性都是成比例提升
        #例如，对方px = 1000， 防御降低为原来的0.8，就是800，那么如果对方px = 1， 就是0.8，
        #那么对于同样的hp来说，抗打击时间的增加的比例也是一定的，和px无关。
        ph = self.ph+sum_runes_f(self.runes, "hp")+sum_equips_f(self.equips, "hp")
        pa = self.ph+sum_runes_f(self.runes, "pa")+sum_equips_f(self.equips, "pa")
        ma = self.ph+sum_runes_f(self.runes, "ma")+sum_equips_f(self.equips, "ma")
        pp = target.pp+sum_runes_f(target.runes, "pp")+sum_equips_f(target.equips, "pp")
        mp = target.pp+sum_runes_f(target.runes, "mp")+sum_equips_f(target.equips, "mp")
        if target.have_the_equip("暗影战斧"):
            pp =pp+ 50 + 10*target.level
            #rpa : real physics armor
            rpa = pa - pp
        if target.have_the_equip("破甲弓"):
            rpa = (1- 0.45)*rpa
        if target.have_the_equip("秘法之靴"):
            mp+= 75
        if target.have_the_equip("痛苦面具"):
            mp+= 75
            # rma: real magic armor
            rma = ma - mp
        if target.have_the_equip("虚无法杖"):
            rma  = rma*(1-0.45)
        if self.have_the_equip("影忍之足"):
            px = px*cent(85)
        time = hp/(px*arm2dam(rpa)+mx*arm2dam(rma))
        if self.have_the_equip("魔女斗篷"):
            time += (200+120*self.level)/(mx*arm2dam(rma))
        return time
    
#################################一下内容需要更改
# 计算如果加上铭文或者武器后的效果
    def real_attack_damage_with(self, what, target, after_skill, kind = ""):
        if what.name in Runes_d:
            k = what.kind
            #print(what.kind)
            self.add_a_rune(what)
            rd = self.real_attack_damage(target,  True, True, after_skill , kind )
            self.runes[k].pop()
            return rd
        elif what.name in Equips_d:
            k = what.kind
            self.add_a_equip(what)
            rd = self.real_attack_damage(target,  True, True, after_skill , kind )
            self.equips[k].pop()
            return rd
        else:
            raise Exception("不知道你放了什么进♂来")

    def real_skill_damage_with(self,what, target, skill, after_a_while , kind ="" ):
        if what.name in Runes.d:
            rd = 0
            k= what.kind
            self.add_a_rune(what)
            for skill in self.skills:
                rd += self.real_skill_damage(target, skill, True, True, after_a_while , kind)
            self.runes[k].pop()
            return rd
        elif what.name in Equips_d:
            rd = 0
            k = what.kind
            self.add_a_equip(what)
            for skill in self.skills:
                rd+= self.real_skill_damage( target, skill, True, True, after_a_while , kind)
            self.equips[k].pop()
            return rd
        else:
            raise Exception("不知道你放了什么进♂来")

    def real_damage_resistance_with(self,what, px, py):
        if what.name in Runes.d:
            k= what.kind
            self.add_a_rune(what)
            time = self.real_damage_resistance(target,px, mx)
            self.runes[k].pop()
            return time
        elif what.name in Equips_d:
            k = what.kind
            self.add_a_equip(what)
            time = self.real_damage_resistance( target,px, mx)
            self.equips[k].pop()
            return time
        else:
            raise Exception("不知道你放了什么进♂来")
                                                
#检查铭文和装备是否满格
    def rune_is_full(self):
        for k in self.runes:
            if len(self.runes[k]) <10:
                return False
        return True

    def equip_is_full(self):
        return self.enum() >= 6

#挑选铭文和装备
    def choose_runes(self, target, method ="attack" ,after_skill = False , after_a_while =False, kind= "实际伤害", px =0, mx =0, using_list = RLusing):
        #method: real_attack_damage:     kind: 物理吸血   /  实际伤害
        #method:real_skill_damage:  kind: 物理吸血/ 法术吸血/ 实际伤害
        if method == "attack":
            Origin = self.real_attack_damage(target, True, True, after_skill, kind )
        elif method == "skill":
            Origin = self.real_skill_damage(target, skill,True, True, after_a_while, kind)
        elif method == "resistance":
            Origin = self.real_damage_resistance(target,px, mx)
        else:
            raise Exception("unrecognize method")
        k= 0
        while not self.rune_is_full():
            add = True
            if method == "attack":
                rd_rune = [     [self.real_attack_damage_with(r, target, after_skill, kind), r]  for r in using_list ]
            elif method == "skill":
                rd_rune = [     [self.real_skill_damage_with(r, target, skill, after_a_while , kind ), r]  for r in using_list ]
            elif method == "resistance":
                rd_rune = [     [self.real_damage_resistance_with(r, px, py), r]  for r in using_list ]
            else:
                raise Exception("unrecognize method")

            #
            rd_rune.sort()
            i  = -1
            while i >= - len(rd_rune) and add:
                if ((rd_rune[i][1].kind == "红色" and self.red()) or
                (rd_rune[i][1].kind == "绿色" and self.green()) or
                 (rd_rune[i][1].kind == "蓝色" and self.blue())):
                    k+=1
                    self.add_a_rune(rd_rune[i][1])
                    #print(rd_rune[i][1].name, end= "  " )
                    if k % 10== 0:
                        #print()
                        pass
                    add = False
                else:
                    i -= 1
        if method == "attack":
            Buff = self.real_attack_damage(target, True, True, after_skill, kind )
        elif method == "skill":
            Buff = self.real_skill_damage(target, skill,True, True, after_a_while, kind)
        elif method == "resistance":
            Buff = self.real_damage_resistance(target,px, mx)
        else:
            raise Exception("unrecognize method")
        #print("{}:      {}----> {}  增加了：{}%".format(kind,Origin, Buff, (Buff-Origin)/Origin*100))

    def choose_equips(self, target, method = "attack", after_skill =False, after_a_while= False , kind = "实际伤害"):
        while not self.equip_is_full():
            if method == "attack":
                Origin = self.real_attack_damage(target, True, True, after_skill, kind )
            elif method == "skill":
                Origin = self.real_skill_damage(target, skill,True, True, after_a_while, kind)
            elif method == "resistance":
                Origin = self.real_damage_resistance(target,px, mx)
            else:
                raise Exception("unrecognize method")
            #Origin 
            if method == "attack":
                rd_equip = [     [self.real_attack_damage_with(e, target, after_skill, kind), e]   for e in Equipments  ]
            elif method == "skill":
                rd_equip = [     [self.real_skill_damage_with(e, target, skill, after_a_while , kind ), e]  for e in Equipments ]
            elif method == "resistance":
                rd_equip = [     [self.rreal_damage_resistance_with(e, px, py), e]   for e in Equipments  ]
            else:
                raise Exception("unrecognize method")
            #rd_equip = [         [self.real_damage_with(e, target, conti), e]  for e in Equipments                   ]
            rd_equip.sort()
            self.add_a_equip(rd_equip[-1][1])
            if method == "attack":
                Buff = self.real_attack_damage(target, True, True, after_skill, kind )
            elif method == "skill":
                Buff = self.real_skill_damage(target, skill,True, True, after_a_while, kind)
            elif method == "resistance":
                Buff = self.real_damage_resistance(target,px, mx)
            else:
                raise Exception("unrecognize method")
            #print("{}:    {}----> {}  增加了：{}%".format(kind,  Origin, Buff, (Buff-Origin)/Origin*100))

    def clear(self, t="all"):
        if t == "all":
            self.runes = {"红色":[],"绿色":[],"蓝色":[]}
            self.equips = {"攻击":[], "法术":[],  "防御":[]  ,"移动":[], "打野" :[]}
        elif t == "runes":
            self.runes = {"红色":[],"绿色":[],"蓝色":[]}
        elif t== "equips":
            self.equips = {"攻击":[], "法术":[],  "防御":[]  ,"移动":[], "打野" :[]}
        else:
            raise Exception("sorry")
            
                    
if __name__ == "__main__":
    attacker = Hero(pd = 319,level =10, s = 1.42, r =0, i =2, pp = 0, hp =5215)
    victim = Hero(pa= 400, ma= 250, hp= 8000)
    attacker.add_equips(["末世"])
    attacker.choose_runes(victim, method = "attack", kind= "物理吸血")
    print(attacker.real_attack_damage(victim, kind = "物理吸血" ))
            
    
       
