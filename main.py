import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


def equation(z,t,k,m):
          #on pose z0 = x et z1 = dx on aura dz0 = dx = z1
          #w_carré = k/m
          
          return [z[1], -np.dot(z[0],k/m)]

t = np.linspace(0,10,400)


st.sidebar.title("Système ressort")
k=st.sidebar.slider("Raideur du ressort",min_value=100,max_value=300)
m=st.sidebar.slider("Masse",min_value=45,max_value=70)
if st.sidebar.button("Courbes"):
          
          ci = [2, 0]
          solution = odeint(equation,ci,t, args=(int(k),int(m)))
          st.title("Courbe x(t)")
          fig = px.scatter(
                              x=t,
                              y=solution[:,0],
                              
                              )

          st.plotly_chart(fig)
          st.title("Courbe v(t)")
          fig = px.scatter(
                              x=t,
                              y=solution[:,1],
                              
                              )

          st.plotly_chart(fig)
#fig, axs = plt.subplots(2)
#axs[0].plot(t,solution[:,0])
#axs[0].set_ylabel('$x(t)$')
#axs[1].set_xlabel('t')
#axs[1].plot(t,solution[:,1])
#axs[1].set_ylabel('$v(t)$')
#plt.show()