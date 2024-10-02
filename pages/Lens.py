import matplotlib.pyplot as plt
import streamlit as st

def create_lens_plot(focal_length, arrow_height, arrow_position):
    # Create a figure using Streamlit's plotting capabilities
    fig = st.pyplot(plt.figure(figsize=(10, 8)))
    
    # Get the current axes
    ax = plt.gca()

    # Arrow
    ax.arrow(arrow_position, 0, 0, (arrow_height-0.3), head_width=0.2, head_length=0.3, fc='red', ec='red')

    # Line from arrow top through (0,0)
    x1, y1 = arrow_position, arrow_height
    x2, y2 = 0, 0
    ax.plot([x1, x2], [y1, y2], color='black')
    ax.plot([x2, 20], [y2, y2 - (x2 - 20) * (y2 - y1) / (x2 - x1)], color='black')

    # Line from arrow top to lens
    x2, y2 = 0, arrow_height
    ax.plot([x1, x2], [y1, y2], color='black')

    # Line from lens to focal point
    x1, y1 = 0, arrow_height
    x2, y2 = focal_length, 0
    ax.plot([x1, x2], [y1, y2], color='black')
    ax.plot([x2, 20], [y2, y2 - (x2 - 20) * (y2 - y1) / (x2 - x1)], color='black')

    # Calculate intersection point
    def line_intersection(line1, line2):
        x1, y1, x2, y2 = line1
        x3, y3, x4, y4 = line2
        px = ((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4)) / \
             ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        py = ((x1*y2 - y1*x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4)) / \
             ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        return px, py

    line1 = (arrow_position, arrow_height, 0, 0)
    line2 = (0, arrow_height, focal_length, 0)
    intersection_x, intersection_y = line_intersection(line1, line2)

    # Plot intersection point
    ax.plot(intersection_x, intersection_y, 'ro', markersize=5)

    # Dotted line from intersection to x-axis
    ax.plot([intersection_x, intersection_x], [intersection_y, 0], 'r--', linewidth=1)

    # x & y axis
    ax.axvline(x=0, color='black', linewidth=1)
    ax.axhline(y=0, color='black', linewidth=1)

    # Graph limits
    ax.set_xlim(-11, 11)
    ax.set_ylim(-11, 11)

    # Update the Streamlit figure
    fig.pyplot(plt)

    return fig
# Streamlit app
st.title("Concave Lens Simulation")

# Sidebar for user inputs
st.sidebar.header("Lens Parameters")
focal_length = st.sidebar.slider("Focal Length", 1.0, 5.0, 2.0)
arrow_height = st.sidebar.slider("Arrow Height", 1.0, 10.0, 5.0)
arrow_position = st.sidebar.slider("Arrow Position", -10.0, -1.0, -4.0)

# Create and display the plot
fig = create_lens_plot(focal_length, arrow_height, arrow_position)

# Additional information
st.sidebar.divider()
st.sidebar.write(f"Focal Length: {focal_length:.1f}")
st.sidebar.write(f"Arrow Height: {arrow_height:.1f}")
st.sidebar.write(f"Arrow Position: {arrow_position:.1f}")