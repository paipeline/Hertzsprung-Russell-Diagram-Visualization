import plotly.graph_objects as go
from parallax_luminosity_temperature import luminosity_ratio_log10
import numpy as np

def vis_effective_temperature_vs_log_luminosity_ratio(temperatures, rs, names, reference_temperature, reference_radius):
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
        mode='markers+text',
        text=names,
        textposition="top right",
        marker=dict(
            size=15,
            color=temperatures,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title='Temperature (K)')
        )
    ))
    
    fig.update_layout(
        title='M67 Cluster: Effective Temperature vs. Logarithmic Luminosity Ratio',
        xaxis_title='Effective Temperature (K)',
        yaxis_title='Log Luminosity Ratio log(L/L_ref)',
        font=dict(size=14),
        plot_bgcolor='rgb(240, 240, 240)',
        hovermode='closest'
    )
    
    fig.update_xaxes(gridcolor='white', gridwidth=2)
    fig.update_yaxes(gridcolor='white', gridwidth=2)
    
    fig.show()

# M67 cluster data (example values, replace with actual data if available)
temperatures = [6500, 5900, 5400, 4800, 4200]
radii = [1.2, 1.0, 0.9, 1.5, 2.0]
names = ['M67-1', 'M67-2', 'M67-3', 'M67-4', 'M67-5']

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

vis_effective_temperature_vs_log_luminosity_ratio(temperatures, radii, names, T_sun, R_sun)








