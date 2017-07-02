from utility import*
from rune import*
from equipment import*
from hero import*


attacker = Hero(pd = 411,level =15, s = 1.42, r =0, i =2, pp = 0, hp =5215)

victim = Hero(pa= 400, ma= 200, hp= 60000)

attacker.add_equips(["闪电匕首"])

value = attacker.real_attack_damage(victim, kind = "实际伤害", index = 0.885,ms =cent(4))

explain = {"r":"暴击率","i":"暴击效果","s":"攻击速度","pd":"物理攻击"}


def show(para):
    feature = attacker.getvalue(para)
    sentence = explain[para]+":" + str(feature)
    #print(sentence)

for key in explain:
    show(key)


def error(theory, real):
    s = "理论值：{}\n实际值：{}\n误差率：{}"
    s=s.format(theory,real, str(round((theory-real)/real*100,3))+"%")
    print(s)

#print(value)

error(value, 600)
