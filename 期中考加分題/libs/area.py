# -*- coding: utf-8 -*-
'''
B10802014_國企系
'''
import math

Type = str(input('選擇你要計算的圖形類型(Select the type of graphics you want to calculate):\n\n1.圓形(Circle)\n2.矩形(Rectangle)\n3.三角形(Triangle)\n\n>>>>'))
quit = '\n按下\'Enter\'結束此程式'

try:
    if Type == '1':
        try:
            radius = eval(input('請輸入圓的半徑(Please enter the radius of the circle):\n\n>>>>'))
            area = (radius**2)*math.pi
            print('圓面積為(Circle area):%f' % (area))
            input(quit)
        except:
            pass
    if Type == '2':
        try:
            length1, length2 = eval(input('請輸入矩形的雙邊長以逗號分隔(Please enter the bilateral length of the rectangle):\n\n>>>>'))
            area = (length1*length2)
            print('矩形面積為(Rectangle area):%f' % (area))
            input(quit)
        except:
            pass
    if Type == '3':
        try:
            length, height = eval(input('請輸入三角形的邊長與高以逗號分隔(Please enter the length and height of the triangle):\n\n>>>>'))
            area = (length*height)/2
            print('三角形面積為(Truangle area):%f' % (area))
            input(quit)
        except:
            pass
except:
    pass
