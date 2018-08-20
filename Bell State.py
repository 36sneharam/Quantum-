
# coding: utf-8

# In[20]:


import qiskit as qk
from qiskit.tools.visualization import *


# In[90]:


# Creating a Bell 00 state 
qr = qk.QuantumRegister(2)
qc = qk.QuantumCircuit(qr,cr)
qc.h(qr[0])
qc.cx(qr[0],qr[1])
circuit_drawer(qc)


# In[95]:


# Creating a Bell 01 state 
qr = qk.QuantumRegister(2)
qc = qk.QuantumCircuit(qr,cr)
qc.h(qr[0])
qc.cx(qr[0],qr[1])
qc.x(qr[1])

circuit_drawer(qc)


# In[96]:


# Creating a Bell 10 state 
qr = qk.QuantumRegister(2)
qc = qk.QuantumCircuit(qr,cr)
qc.x(qr[0])
qc.h(qr[0])
qc.cx(qr[0],qr[1])

circuit_drawer(qc)


# In[97]:


# Creating a Bell 11 state 
qr = qk.QuantumRegister(2)
qc = qk.QuantumCircuit(qr,cr)
qc.h(qr[0])
qc.cx(qr[0],qr[1])
qc.z(qr[1])
qc.x(qr[1])

circuit_drawer(qc)

