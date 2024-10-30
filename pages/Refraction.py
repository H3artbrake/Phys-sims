# Import the libraries
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

def plot_graph(medium, theta_i, n):
    #initialize graph
    fig, ax = plt.subplots()
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)

    #the lines i need at the start
    ax.axvline(x=5, color="black",  label=medium)
    ax.axhline(y=5, color="lightseagreen", label="Normal")

    #incident ray
    slope_i = np.tan(np.radians(theta_i))
    intercept = 5 - slope_i * 5
    x_vals = np.array([0, 5])
    y_vals = slope_i * x_vals + intercept
    ax.plot(x_vals, y_vals, label=f'Incident ray', color="crimson")

    # Draw Incident Angle Arc
    angle_radius = 1
    if theta_i >= 0:
        # Positive incident angle
        arc_incident = Arc((5, 5), angle_radius, angle_radius, angle=180,
                           theta1=0, theta2=theta_i, color="crimson")
        ax.text(3 + 0.6 * angle_radius, 4 + angle_radius * np.sin(np.radians(theta_i)) - 0.3,
                f"{theta_i}°", color="crimson", fontsize=9)
    else:
        # Negative incident angle
        arc_incident = Arc((5, 5), angle_radius, angle_radius, angle=180,
                           theta1=theta_i, theta2=0, color="crimson")
        ax.text(3 + 0.6 * angle_radius, 6.5 + angle_radius * np.sin(np.radians(theta_i)) - 0.3,
                f"{theta_i}°", color="crimson", fontsize=9)
    ax.add_patch(arc_incident)


    #finding r°
    i = np.radians(theta_i)
    r = np.arcsin(np.sin(i)/n)
    theta_r = np.degrees(r)

    #refracted ray
    slope_r = np.tan(np.radians(theta_r))
    intercept = 5 - slope_r*5
    x_vals = np.array([5, 10])
    y_vals = slope_r * x_vals + intercept
    ax.plot(x_vals, y_vals, label=f'Refracted ray', color="darkviolet")

    #write angle
    angle_radius=1
    if theta_i >= 0:
        #i is positive
        arc_refracted = Arc((5, 5), angle_radius, angle_radius, angle=0, theta1=0, theta2=theta_r, color="darkviolet")
        ax.text(6, 5 + 1 * slope_r - 0.5, f"{theta_r:.2f}°", color="darkviolet", fontsize=9)
    else:
        #i is negative
        arc_refracted = Arc((5, 5), angle_radius, angle_radius, angle=theta_r, theta1=0, theta2=-theta_r, color="darkviolet")
        ax.text(6, 5 + 0.1 * slope_r - 0.5, f"{theta_r:.2f}°", color="darkviolet", fontsize=9)
    ax.add_patch(arc_refracted)


    #just finishing up
    ax.legend()
    return fig

refractive_indexes = {
    "Glass": 1.52,
    "Water": 1.33,
    "Diamond": 2.42,
    "Acrylic": 1.49
}

st.title("Refraction")

#Sidebar stuff
#params
st.sidebar.title("Parameters")
medium = st.sidebar.selectbox(
    "Medium",
    ("Acrylic", "Diamond", "Glass", "Water"),
)
st.sidebar.write(f"Refractive index = {refractive_indexes[medium]}")
theta_i = st.sidebar.slider("Incident ray angle", -90, 90, 30)

st.sidebar.divider()

#math
st.sidebar.latex(r"n=\frac{\sin i}{\sin r}")
st.sidebar.latex(r"\sin r = \frac{\sin i}{n}")
st.sidebar.latex(r"r = \arcsin\left(\frac{\sin i}{n}\right)")
st.sidebar.latex(fr"r = \arcsin\left(\frac{{\sin({theta_i})}}{{{refractive_indexes[medium]}}}\right)")

# Display the plot in Streamlit
fig = plot_graph(medium, theta_i, refractive_indexes[medium])
st.pyplot(fig)
