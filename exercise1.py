import matplotlib.pyplot as plt
from parallax_luminosity_temperature import luminosity_ratio_log10
import numpy as np
def vis_effective_temperature_vs_log_luminosity_ratio(temperatures, rs, reference_temperature, reference_radius):
    """
    绘制有效温度与光度比值的对数之间的图。
    """
    luminosity_ratio_log10s = [
        luminosity_ratio_log10(temp,r, reference_temperature, reference_radius) 
        for temp, r in zip(temperatures, rs)
    ]
    
    plt.plot(temperatures, luminosity_ratio_log10s)
    plt.xlabel('Effective Temperature (K)')
    plt.ylabel('Logarithmic Luminosity Ratio Lmeasured / Lref')
    plt.title('Effective Temperature vs. Logarithmic Luminosity Ratio')
    plt.show()
#log(L/L_ref) vs Effective Temperature data

fake_y = [100,2004,200,300,50]
fake_x = [10000,8000,6000,4000,3000]

L_sun = 3.828e26
R_sun = 6.96e8  # 太阳半径，单位为米
T_sun = 5778 
# 使用公式L = T^4来证明L_sun的正确性
# 斯特凡-玻尔兹曼常数 (单位: W/m^2·K^4)
sigma = 5.67e-8

T_sun = 5770
R_sun = 6.96e8
# 计算太阳的表面面积
surface_area = 4 * np.pi * R_sun**2
# 计算太阳的总光度
luminosity_by_calc = sigma * surface_area * T_sun**4
print(luminosity_by_calc, L_sun)
# 检查计算结果是否与已知的太阳光度相符


vis_effective_temperature_vs_log_luminosity_ratio(fake_x, fake_y, T_sun, R_sun)








