import plotly.graph_objects as go
import numpy as np

def hr_diagram(temperatures, luminosities, names, wd_temp, wd_lum):
    """
    Create an HR diagram using Plotly.
    """
    fig = go.Figure()

    # Plot main sequence stars
    fig.add_trace(go.Scatter(
        x=temperatures,
        y=luminosities,
        mode='markers+text+lines',
        name='M67 Stars',
        text=names,
        textposition="top center",
        marker=dict(
            size=12,
            color=temperatures,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title='Temperature (K)')
        ),
        line=dict(color='rgba(50, 50, 50, 0.5)', width=1)
    ))

    # Plot white dwarf
    fig.add_trace(go.Scatter(
        x=[wd_temp],
        y=[wd_lum],
        mode='markers+text',
        name='White Dwarf',
        text=['WD'],
        textposition="top center",
        marker=dict(size=12, color='red', symbol='star')
    ))

    fig.update_layout(
        title='M67 Cluster HR Diagram',
        xaxis_title='Effective Temperature (K)',
        yaxis_title='Log Luminosity (L/L☉)',
        font=dict(size=14),
        plot_bgcolor='rgb(240, 240, 240)',
        hovermode='closest'
    )

    # Reverse x-axis
    fig.update_xaxes(autorange="reversed", gridcolor='white', gridwidth=2)
    fig.update_yaxes(gridcolor='white', gridwidth=2)

    fig.show()

# M67 cluster data (example values, replace with actual data if available)
temperatures = [6500, 6200, 5900, 5600, 5300, 5000, 4700, 4400]
luminosities = [np.log10(1.5), np.log10(1.3), np.log10(1.1), np.log10(0.9), 
                np.log10(0.7), np.log10(0.5), np.log10(0.3), np.log10(0.1)]
names = ['M67-1', 'M67-2', 'M67-3', 'M67-4', 'M67-5', 'M67-6', 'M67-7', 'M67-8']

# White dwarf data
wd_temp = 11000
wd_lum = np.log10(1/100)  # 100 times less luminous than the Sun

hr_diagram(temperatures, luminosities, names, wd_temp, wd_lum)








