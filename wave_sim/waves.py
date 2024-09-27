import numpy as np
import pandas as pd
import streamlit as st

# Streamlit title and description
st.title(":rainbow[Wave sim]")

# Streamlit sliders for user input
frequency = st.slider("Select frequency (Hz):", min_value=1, max_value=10, value=5)
wavelength = st.slider("Select wavelength (m):", min_value=1, max_value=20, value=15)
#amplitude = st.slider("Select amplitude:", min_value=0.1, max_value=5.0, value=1.0)
amplitude = 2

st.divider()

st.write(f"Speed: {frequency * wavelength}")

st.divider()

# Duration and sampling rate
duration = 20  # Duration in seconds or spatial length
sampling_rate = 1000  # Sampling rate

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate sine wave
y = amplitude * np.sin(2 * np.pi * frequency * (t / wavelength))

# Create a DataFrame for the sine wave data
data = pd.DataFrame({
    'Distance': t,
    'Amplitude': y
})

# Plotting the sine wave using st.line_chart
st.line_chart(data.set_index('Distance'), use_container_width=True)

