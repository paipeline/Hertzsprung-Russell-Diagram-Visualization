import plotly.graph_objects as go
from parallax_luminosity_temperature import luminosity_ratio_log10
import numpy as np

def vis_effective_temperature_vs_log_luminosity_ratio(temperatures, rs, reference_temperature, reference_radius):
    """
    
    Create a plot of effective temperature vs. logarithmic luminosity ratio using Plotly.
    """
    luminosity_ratio_log10s = [
        luminosity_ratio_log10(temp, r, reference_temperature, reference_radius) 
        for temp, r in zip(temperatures, rs)
    ]
    
    fig = go.Figure(data=go.Scatter(
        x=temperatures,
        y=luminosity_ratio_log10s,
        mode='markers',
        marker=dict(
            size=10,
            color=temperatures,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title='Temperature (K)')
        )
    ))
    
    fig.update_layout(
        title='Effective Temperature vs. Logarithmic Luminosity Ratio',
        xaxis_title='Effective Temperature (K)',
        yaxis_title='Log Luminosity Ratio log(L/L_ref)',
        font=dict(size=14),
        plot_bgcolor='rgb(240, 240, 240)',
        hovermode='closest'
    )
    
    fig.update_xaxes(gridcolor='white', gridwidth=2)
    fig.update_yaxes(gridcolor='white', gridwidth=2)
    
    fig.show()

# log(L/L_ref) vs Effective Temperature data
fake_y = [100, 2004, 200, 300, 50]
fake_x = [10000, 8000, 6000, 4000, 3000]

L_sun = 3.828e26
R_sun = 6.96e8  # Sun's radius in meters
T_sun = 5778 

# Verify L_sun using the formula L = T^4
# Stefan-Boltzmann constant (units: W/m^2·K^4)
sigma = 5.67e-8

T_sun = 5770
R_sun = 6.96e8
# Calculate the surface area of the Sun
surface_area = 4 * np.pi * R_sun**2
# Calculate the total luminosity of the Sun
luminosity_by_calc = sigma * surface_area * T_sun**4
print(luminosity_by_calc, L_sun)
# Check if the calculated result matches the known solar luminosity

vis_effective_temperature_vs_log_luminosity_ratio(fake_x, fake_y, T_sun, R_sun)








