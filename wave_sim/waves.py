import numpy as np
import pandas as pd
import streamlit as st

st.title(":rainbow[Wave sim]")

#st sliders for user input
frequency = st.slider("Select frequency (Hz):", min_value=1, max_value=10, value=5)
wavelength = st.slider("Select wavelength (m):", min_value=1, max_value=20, value=15)
#amplitude = st.slider("Select amplitude:", min_value=0.1, max_value=5.0, value=1.0)
amplitude = 2 #possible to add slider, but for now, just set it to 2

st.divider()

st.write(f"Speed: {frequency * wavelength} m/s")

st.divider()

distance = 20 
sampling_rate = 1000 

t = np.linspace(0, distance, int(sampling_rate * distance), endpoint=False)

#gen wave
y = amplitude * np.sin(2 * np.pi * frequency * (t / wavelength))

data = pd.DataFrame({
    'Distance': t,
    'Amplitude': y
})

st.line_chart(data, x='Distance', y='Amplitude', color='#FF4B4B')

