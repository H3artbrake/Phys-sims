import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

st.title("Refraction")
n_medium = st.sidebar.slider("Number of mediums", 2,6,3)
st.sidebar.divider()

refractive_indexes = {
    "Glass": 1.52,
    "Water": 1.33,
    "Diamond": 2.42,
    "Acrylic": 1.49, 
    "Air":1.00,
    "Vacuum" :1.00,
}

mediums = {}

def plot_graph(mediums, theta_i):
    #initialize graph
    fig, ax = plt.subplots()
    ax.set_xlim(0,5*n_medium)
    ax.set_ylim(0,11)

    #medium changes
    ax.axvline(x=0, color="black", label="Medium change")
    for i in range (1, n_medium):
        posit_x = 5*i
        ax.axvline(x=posit_x, color="black")
    
    #writing refractive index for each medium
    medium_values = list(mediums.values())
    for i in range(1, n_medium+1):
        posit_x = 5*i-3.5
        ax.text(posit_x,10, f"n={medium_values[i-1]}", fontsize = 7)

    #incident ray
    slope_i = np.tan(np.radians(theta_i))
    intercept = 5 - slope_i * 5
    x_vals = np.array([0, 5])
    y_vals = slope_i * x_vals + intercept
    ax.plot(x_vals, y_vals, label=f'Incident ray', color="crimson")
    ax.plot([3, 7], [5, 5], color="lightseagreen", label="Normal", linestyle="--")

    next_y = 5
    ax.plot([0,0], [0,0], label=f'Refracted ray', color="darkviolet")

    for j in range(1, n_medium):
        #finding r°
        i = np.radians(theta_i)
        n = (medium_values[j])/(medium_values[j-1])
        posit_x=5*j+1.5
        ax.text(posit_x,9.5, f"n'={n:.2f}", fontsize = 7)
        r = np.arcsin(np.sin(i)/n)
        theta_r = np.degrees(r)

        #refracted ray
        slope_r = np.tan(np.radians(theta_r))
        intercept = next_y - slope_r* (5*j)
        x_vals = np.array([5*j, 5*(j+1)])
        y_vals = slope_r * x_vals + intercept
        ax.plot(x_vals, y_vals, color="darkviolet")
        ax.text(5*j+1, next_y + 1 * slope_r - 0.5, f"{theta_r:.2f}°", color="darkviolet", fontsize=7)

        
        x_target = 5*(j+1)
        next_y = slope_r * x_target + intercept
        ax.plot([5*(j+1)-2, 5*(j+1)+2], [next_y, next_y], color="lightseagreen", linestyle="--")
        ax.set_ylim(0,next_y+1)
        theta_i=theta_r


    ax.legend()
    return fig

def sidebar_medium_selection(i):
    medium = st.sidebar.selectbox(
        f"Medium {i}",
        ("Vacuum", "Air", "Water", "Acrylic", "Glass", "Diamond"),
        i-1
    )
    n = refractive_indexes[medium]
    st.sidebar.write(f"Refractive index = {n}")
    return medium, n

#sidebar
theta_i = st.sidebar.slider("Incident ray angle", -90, 90, 30)

for i in range(1, n_medium+1):
    medium, n = sidebar_medium_selection(i)
    mediums[f"medium{i}"] = n

fig = plot_graph(mediums, theta_i)
st.pyplot(fig)
