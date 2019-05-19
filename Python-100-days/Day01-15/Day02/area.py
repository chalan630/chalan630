"""
输入半径计算圆的周长和面积

Version: 0.1
"""
pi = 3.14
radius = float(input('请输入圆的半径：'))
perimeter = 2 * pi * radius
area = pi * pow(radius, 2)
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
