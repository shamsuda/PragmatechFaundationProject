# Daxil edilən ədədin rəqəmlerinin cemini tap
a=1
def Artir():
    a==3
    a+=1
    print(a)
    Artir()
    
# Daxil edilən ədədin rəqəmlerini ayrı ayrı çap edin
def Artir():
    global a
    print(a)
    if a<100:
        a+=1
        Artir()