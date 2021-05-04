'''
B10802014_國企系
'''
h = eval(input('請輸入你的身高 (Please enter your height(meter))\n\n>>>>'))
w = eval(input('\n請輸入你的體重 (Please enter your body weight(kilogram))\n\n>>>>'))

quit = '\n\n按下\'Enter\'結束此程式'

bmi = w/(h**2)
if bmi <= 18.5:
    print('\nBMI : %f\n\n體重過輕' %(bmi))
elif bmi <= 24:
    print('\nBMI : %f\n\n健康體重' %(bmi))
elif bmi <= 27:
    print('\nBMI : %f\n\n體重過重' %(bmi)) 
else:
    print('\nBMI : %f\n\n肥胖' %(bmi))
input(quit)
