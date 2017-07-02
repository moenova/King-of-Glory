from utility import*
from rune import*
from equipment import*
from hero import*


attacker = Hero(pd = 411,level =15, s = 1.42, r =0, i =2, pp = 0, hp =5215)

victim = Hero(pa= 400, ma= 200, hp= 60000)

#attacker.add_equips(["暗影战斧","末世","影刃","破军"])
#print(attacker.real_damage(victim, True, True, True))

y = comb(Eusing, 4)


print(len(y))

rds = []
k=0
for elst in y:
    attacker.add_equips(elst)
    #attacker.choose_runes(victim, method = "attack", kind= "物理吸血")
    sub= [attacker.real_attack_damage(victim, kind = "实际伤害"), elst, attacker.runes.copy()]
    rds .append(sub)
    attacker.clear()
    k+=1
    if k % 10 == 0:
        print(k,"th" ,end = "     ")

print()
rds.sort()


for i in range(1,11):
    print(i, ":   ")
    print("real damage : ", rds[-i][0])
    print("equipments: ", rds[-i][1])
    for key in rds[-i][2]:
        for rune in rds[-i][2][key]:
            print(rune.name, end = " ")
        print()




##########
"""

d= []
for s in Runes_d:
        sub = [attacker.real_damage_with( Runes_d[s],victim, True), s]
        d.append(sub)
d.sort()
d.reverse()
for sub in d:
    print(sub[1],":" ,sub[0])

attacker.choose_runes(victim, True)

attacker.choose_equips(victim, True)
for k in attacker.equips:
    for e in attacker.equips[k]:
        print(e.name)





print(attacker.real_damage(victim, True, True, True))
"""

