import os, sys
#                                                                           这里填-1就表示返回一级菜单↓
path = "\\".join(os.path.realpath(os.path.dirname(sys.argv[0])).split("\\")[:-1])
print(path)
sys.path.append(path)



from utility import*
from hero import*
from rune import*
from equipment import*
from skill import*

class 妲己(Hero):
    def __init__(self, name = "", kind="", level = 0 , pd=0,md=0, s=0, r=0, i=0, pp=0, mp=0, pa=0, ma =0, hp =0,skills=[] ):
        Hero.__init__(self, name , kind, level , pd,md, s, r, i, pp, mp, pa, ma , hp ,skills)
        



