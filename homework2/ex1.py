import random
class Team:
    def init(self,name,nation,group,picked):
        self.name=name
        self.nation=nation
        self.group=group
        self.picked=picked

t1=Team("t1","Russia",1,0)
t2=Team("t2","Ukraine",2,0)
t3=Team("t3","France",1,0)
t4=Team("t4","England",2,0)
t5=Team("t5","Spain",1,0)
t6=Team("t6","Portugal",2,0)
t7=Team("t7","Bulgaria",1,0)
t8=Team("t8","Italy",2,0)
t9=Team("t9","Germany",1,0)
t10=Team("t10","Poland",2,0)
t11=Team("t11","Austria",1,0)
t12=Team("t12","Denmark",2,0)
t13=Team("t13","Sweden",1,0)
t14=Team("t14","Serbia",2,0)
t15=Team("t15","Hungary",1,0)
t16=Team("t16","Romania",2,0)
list=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16]
a=int()
b=int()
for i in range(8):
    while a==b or (list[a].nation=="Russia" and list[b].nation=="Ukraine") or list[a].nation==list[b].nation or list[a].group==list[b].group or list[a].picked==1 or list[b].picked==1:
        a=random.randrange(0,16)
        b=random.randrange(0,16)
    print(list[a].name,"VS",list[b].name)
    list[a].picked=1
    list[b].picked=1