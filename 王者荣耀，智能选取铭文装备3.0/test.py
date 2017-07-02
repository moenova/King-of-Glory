from utility import*
from rune import*
from equipment import*
from hero import*


attacker = Hero(pd = 400,level =10, s = 1.42, r =0, i =2, pp = 0, hp =5215)

victim = Hero(pa= 400, ma= 300, hp= 9000)

#attacker.add_equips(["暗影战斧","末世","影刃","破军"])
#print(attacker.real_damage(victim, True, True, True))
"""
d= []
for s in Runes_d:
        sub = [attacker.real_damage_with( Runes_d[s],victim, True), s]
        d.append(sub)
d.sort()
d.reverse()
for sub in d:
    print(sub[1],":" ,sub[0])

"""


#attacker.add_runes(["无双","鹰眼","兽痕"]*10)
attacker.choose_equips(victim, True)
for k in attacker.equipments:
    for e in attacker.equipments[k]:
        print(e.name)


#attacker.choose_runes(victim, True)



print(attacker.real_damage(victim, True, True, True))
