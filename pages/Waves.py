import numpy as np
import pandas as pd
import streamlit as st
import time

if 'title' not in st.session_state:
    st.session_state['title'] = "Wave sim" 

if 'side_title' not in st.session_state:
    st.session_state['side_title'] = "Adjust wave parameters"

def funs():
    st.balloons()
    time.sleep(2)
    st.session_state['title'] = ":rainbow[Wave sim] :face_with_rolling_eyes:✨"
    st.session_state['side_title'] = ":rainbow[Adjust wave parameters]"

st.title(st.session_state['title'])
st.write("")

# Set up the sidebar for wave parameters
st.sidebar.title(st.session_state['side_title'])
frequency = st.sidebar.slider("Select frequency (Hz):", min_value=1.0, max_value=10.0, value=5.0)
wavelength = st.sidebar.slider("Select wavelength (m):", min_value=1.0, max_value=20.0, value=15.0)
amplitude = st.sidebar.slider("Select amplitude:", min_value=1.0, max_value=5.0, value=2.0)

st.sidebar.divider()
velocity = frequency * wavelength
round_velocity = round(velocity, 2)
st.sidebar.latex(r"v = f \times \lambda")
st.sidebar.latex(f"v = {round_velocity} m/s")

distance = 20  # Distance in meters
sampling_rate = 1000  # Sampling rate

t = np.linspace(0, distance, int(sampling_rate * distance), endpoint=False)

#equation for sine wave
y = amplitude * np.sin(2 * np.pi * frequency * (t / wavelength))

data = pd.DataFrame({
    'Distance (m)': t,
    'Amplitude': y
})

st.line_chart(data, x='Distance (m)', y='Amplitude', color='#FF4B4B', use_container_width=True)

#hands down, the most important part of the entire project 
st.button("Click me", on_click=funs, help="hands down, the most important part of the entire project")


#lines if image on same side - virtual images for lens
#magnification scale