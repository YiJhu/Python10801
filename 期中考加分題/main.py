'''
B10802014_國企系
'''
import os
Type = str(input('選擇你要啟動的程式:\n\n1.加分題(1)[面積]\n2.加分題(2)[BMI]\n\n>>>>'))
try:
    if Type == '1':
        try:
            try:
                os.system("cls")
            except:
                os.system("clear")
            os.system("python ./libs/area.py")
        except:
            pass
    if Type == '2':
        try:
            try:
                os.system("cls")
            except:
                os.system("clear")
            os.system("python ./libs/BMI.py")
        except:
            pass
except:
    pass
exit()
