import numpy as np
import math
def parallax(angle_arcseconds):
    """
    Calculate the distance to a celestial object based on its parallax angle
    
    Parameters:
    angle_arcseconds (float): Parallax angle in arcseconds
    
    Returns:
    dict: Distance information in various units
    """
    if angle_arcseconds <= 0:
        raise ValueError("Parallax angle must be positive")
    
    # Convert arcseconds to radians
    angle_radians = math.radians(angle_arcseconds / 3600)
    
    # Calculate distance in parsecs
    distance_parsecs = 1 / math.tan(angle_radians)
    
    # Convert to other units
    light_years = distance_parsecs * 3.26156
    astronomical_units = distance_parsecs * 206265
    
    return {
        "parsecs": distance_parsecs,
        "light_years": light_years,
        "astronomical_units": astronomical_units
    }

def calculate_distance(parallax_angle):
    """
    Calculate the distance to a celestial object based on its parallax angle
    
    Parameters:
    parallax_angle (float): Parallax angle in arcseconds
    
    Returns:
    dict: Distance information in parsecs and meters
    """
    result = parallax(parallax_angle)
    return {
        "parsecs": result['parsecs'],
        "meters": result['astronomical_units'] * 3.086e16
    }
    

def calculate_luminosity(apparent_brightness, distance_parsecs):
    """
    计算恒星的光度,基于表观亮度和距离。
    
    参数:
    apparent_brightness : float
        表观亮度,单位为W/m^2
    distance_parsecs : float
        恒星距离,单位为秒差距(parsecs)
    
    返回:
    tuple : (luminosity_W, luminosity_Learth, luminosity_log10Learth)
        光度的三种表示: 瓦特、地球光度和以10为底的地球光度对数
    """
    # 将秒差距转换为米
    distance_meters = distance_parsecs * 3.086e16
    
    # 计算光度(瓦特)
    luminosity_W = apparent_brightness * 4 * np.pi * distance_meters**2
    
    # 计算地球光度(Learth)
    L_earth = 3.828e26  # 地球光度,单位为瓦特
    luminosity_Learth = luminosity_W / L_earth
    
    # 计算以10为底的地球光度对数
    luminosity_log10Learth = np.log10(luminosity_Learth)
    
    return luminosity_W, luminosity_Learth, luminosity_log10Learth


def calculate_temperature(wavelength_nm):
    """
    根据给定的峰值波长计算黑体的温度。
    
    参数:
    wavelength_nm : float
        峰值波长,单位为纳米(nm)
    
    返回:
    float : 温度,单位为开尔文(K)
    """
    # 维恩位移常数 (单位: m·K)
    b = 2.9e-3
    # 将波长从纳米转换为米
    wavelength_m = wavelength_nm * 1e-9
    # 使用维恩位移定律计算温度
    temperature_K = b / wavelength_m
    
    return temperature_K



### exercise 2
# formula for luminosity
def luminosity_temperature_r(temperature,r):
    """
    计算恒星的光度,基于温度和半径。
    """
    # 斯特凡-玻尔兹曼常数 (单位: W/m^2·K^4)
    sigma = 5.67e-8
    # 计算恒星的表面面积
    surface_area = 4 * np.pi * r**2
    # 计算恒星的总光度
    luminosity = sigma * surface_area * temperature**4
    
    return luminosity


# a
def calculate_luminosity_ratio(r, temperature, R_Sun, T_Sun, L_Sun):
    luminosity_ratio = (r / R_Sun)**2 * (temperature / T_Sun)**4
    return luminosity_ratio


# b
def convert_temperature_to_Tearth(measured_temperature, reference_temp):
    """
    将测量的温度转换为reference温度单位，给定恒星温度。
    """
    Tearth = measured_temperature / refernece_temp
    return Tearth


# c
def luminosity_ratio(temperature,r, reference_temperature, reference_radius):
    """
    计算恒星的光度与参考恒星光度的比值,基于温度和半径。
    """
    # 斯特凡-玻尔兹曼常数 (单位: W/m^2·K^4)
    sigma = 5.67e-8
    # 计算恒星的表面面积
    surface_area = 4 * np.pi * r**2
    # 计算参考恒星的表面面积
    reference_surface_area = 4 * np.pi * reference_radius**2
    # 计算恒星的总光度
    luminosity = sigma * surface_area * temperature**4
    # 计算参考恒星的总光度
    reference_luminosity = sigma * reference_surface_area * reference_temperature**4
    
    # 计算光度比值
    luminosity_ratio = luminosity / reference_luminosity
    
    return luminosity_ratio



# d
def luminosity_ratio_log10(temperature,r, reference_temperature, reference_radius):
    """
    计算恒星的光度与参考恒星光度的比值,基于温度和半径。
    """
    # 斯特凡-玻尔兹曼常数 (单位: W/m^2·K^4)
    sigma = 5.67e-8
    # 计算恒星的表面面积
    surface_area = 4 * np.pi * r**2
    # 计算参考恒星的表面面积
    reference_surface_area = 4 * np.pi * reference_radius**2
    # 计算恒星的总光度
    luminosity = sigma * surface_area * temperature**4
    # 计算参考恒星的总光度
    reference_luminosity = sigma * reference_surface_area * reference_temperature**4
    
    # 计算光度比值
    luminosity_ratio_log10 = np.log10(luminosity / reference_luminosity)
    
    return luminosity_ratio_log10




