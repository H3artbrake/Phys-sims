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
    ax.plot([x2, 1000], [y2, y2 - (x2 - 1000) * (y2 - y1) / (x2 - x1)], color='black')

    # Line from arrow top to lens
    x2, y2 = 0, arrow_height
    ax.plot([x1, x2], [y1, y2], color='black')

    # Line from lens to focal point
    x1, y1 = 0, arrow_height
    x2, y2 = focal_length, 0
    ax.plot([x1, x2], [y1, y2], color='black')
    ax.plot([x2, 1000], [y2, y2 - (x2 - 1000) * (y2 - y1) / (x2 - x1)], color='black')

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
    try:
        intersection_x, intersection_y = line_intersection(line1, line2)
        # Plot intersection point
        ax.plot(intersection_x, intersection_y, 'ro', markersize=5)

        # Dotted line from intersection to x-axis
        ax.plot([intersection_x, intersection_x], [intersection_y, 0], 'r--', linewidth=1)

        # Extend lines to top of image if intersection is behind the lens
        if intersection_x < 0:
            # Extend line from arrow top through (0,0)
            ax.plot([x2, intersection_x], [y2, intersection_y], color='black')
    except:
        st.error("No image formed because object position is equal to focal length.")
        intersection_x, intersection_y = 0, 0


    ax.scatter(focal_length, 0, color='red', marker='x', s=100, linewidths=2)

    # x & y axis
    ax.axvline(x=0, color='black', linewidth=1)
    ax.axhline(y=0, color='black', linewidth=1)

    if intersection_x>0:
        # Graph limits
        ax.set_xlim(-11, intersection_x+4)
        ax.set_ylim(intersection_y-4, 11)
    elif intersection_x<0:
        ax.set_xlim(intersection_x-4, 11)
        ax.set_ylim(-11, intersection_y+4)
    else:
        ax.set_xlim(-11, 11)
        ax.set_ylim(-11, 11)


    fig.pyplot(plt)

    return fig, intersection_x, intersection_y

# Streamlit app
st.title("Convex Lens Simulation")

st.sidebar.header("Lens Parameters")
focal_length = st.sidebar.slider("Focal Length", 1.0, 10.0, 2.0)
arrow_height = st.sidebar.slider("Object Height", 1.0, 10.0, 5.0)
arrow_position = st.sidebar.slider("Object Position", -10.0, -1.0, -4.0)

fig, intersection_x, intersection_y = create_lens_plot(focal_length, arrow_height, arrow_position)

# Additional info
st.sidebar.divider()
st.sidebar.write(f"Focal Length: {focal_length:.1f}")
st.sidebar.write(f"Image Position: {intersection_x:.2f}, {intersection_y:.2f}")
magnification = intersection_y/arrow_height
st.sidebar.latex(r"M = \frac{I}{A}")
st.sidebar.latex(f"M = {magnification:.2f}")
                 
                 
