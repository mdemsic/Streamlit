import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Definicija funkcije za izračunavanje pomaka
def displacement(t, A, B, omega):
    return A * np.cos(omega * t) + B * np.sin(omega * t)

# Definicija funkcije za crtanje grafikona
def plot_vibration(A, B, omega):
    t = np.linspace(0, 10, 400)  # Vrijeme od 0 do 10 sekundi, 400 točaka
    x = displacement(t, A, B, omega)

    plt.figure(figsize=(10, 6))
    plt.plot(t, x)
    plt.title('Slobodne neprigušene vibracije')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Pomak (m)')
    plt.grid(True)
    plt.ylim(-3, 3)  # Prilagodite ove vrijednosti prema potrebi za vašu specifičnu vizualizaciju
    st.pyplot(plt)  # Koristite Streamlitov st.pyplot() za prikaz Matplotlib grafikona

# Streamlit widgeti za unos
A = st.sidebar.slider('Početni pomak (A)', -2.0, 2.0, 1.0, 0.1)
B = st.sidebar.slider('Početna brzina (B)', -2.0, 2.0, 0.0, 0.1)
omega = st.sidebar.slider('Prirodna frekvencija (ω)', 0.0, 10.0, 2*np.pi, 0.1)

# Pozivanje funkcije za crtanje grafikona sa trenutnim vrijednostima widgeta
plot_vibration(A, B, omega)