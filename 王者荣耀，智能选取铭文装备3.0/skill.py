from utility import*

class Skill:
    def __init__(self, name="", base=0,additional=0, addType = "", damType= "" ,cd =0, last=0, accuracy =1, rate=0):
        """
      
        """
        self.name = name
        self.base = base
        self.additional = additional
        #at: addition type
        self.addType = addType
        #dt: damage type
        self.damType = damType
        #cd: cool down
        self.cd =cd
        self.last = last
        self.accuracy =  accuracy
        self.rate =rate




def skillrates(skills):
    cds = 0
    for skill in skills:
        cds+= skill.cd
    for skill in skills:
        skill.rate = skill.cd/cds
    


#不知火舞
龙炎 = Skill(name="飞翔龙炎阵", base=900,additional=0.73, addType = "法术", damType= "法术" ,cd =6, last=0)
花蝶扇 = Skill(name="花蝶扇", base=950,additional=1, addType = "法术", damType= "法术" ,cd =2, last=0)
必杀= Skill(name="必杀·忍峰", base=1200,additional=1.1, addType = "法术", damType= "法术" ,cd = 20, last=0)









