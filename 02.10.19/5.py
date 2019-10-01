S = input ("Введите площадь:")
S = int(S)
from math import sqrt, pi
R = sqrt(S/pi)
D = 2*R
print ("Длина окружности равна:", pi*D)