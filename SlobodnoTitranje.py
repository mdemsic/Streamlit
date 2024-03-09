# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:52:26 2024

@author: mdems
"""

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Definicija funkcije koja izračunava pomak
def displacement(t, A, B, k, m):
    omega = np.sqrt(k / m)
    return A * np.cos(omega * t) + B * np.sin(omega * t)

# Glavna funkcija koja crta grafikon
def plot_vibration(A, B, m, k):
    period = 2 * np.pi * (np.sqrt(m / k))
    t = np.linspace(0, 5, 1000)
    x = displacement(t, A, B, k, m)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(t, x)
    ax.set_title(f'Slobodno neprigušeno titranje - Period: {period:.2f}')
    ax.set_xlabel('Vrijeme (s)')
    ax.set_ylabel('Pomak (m)')
    ax.grid(True)
    ax.set_ylim(-5, 5)

    return fig

# Streamlit aplikacija
def streamlit_app():
    st.title('Vizualizacija slobodnog neprigušenog titranja')

    # Definiranje korisničkih ulaza pomoću streamlit widgeta
    A = st.slider('Konstanta A = u(0)', min_value=-1.0, max_value=1.0, value=1.0, step=0.01)
    B = st.slider('Konstanta B - v(0)/omega', min_value=-4.0, max_value=4.0, value=0.0, step=0.1)
    m = st.slider('Masa (tone)', min_value=0.1, max_value=15.0, value=1.0, step=0.1)
    k = st.slider('Krutost (kN/m)', min_value=500.0, max_value=15000.0, value=1000.0, step=5.0)

    # Crtanje grafikona i prikazivanje na streamlit aplikaciji
    fig = plot_vibration(A, B, m, k)
    st.pyplot(fig)

# Pokretanje streamlit aplikacije
sreamlit_app(A, B, m, k)
