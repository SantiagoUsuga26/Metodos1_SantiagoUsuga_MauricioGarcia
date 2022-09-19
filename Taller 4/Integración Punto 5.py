#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# In[36]:


class Integrator:
    
    def __init__(self, x,y):
        
        self.x = x
        self.y = y
        self.h = self.x[1] - self.x[0]
        
        self.integral = 0.
    
    def Trapezoid(self):
        
        self.integral = 0.
        self.integral += 0.5*(self.y[0] + self.y[-1])
        self.integral += np.sum( self.y[1:-1] )
        
        return self.integral*self.h
    
    def GetTrapezoidError(self,f):
        
        d = (f( self.x + self.h ) - 2*f(self.x) + f( self.x - self.h))/self.h**2 
        
        
        max_ = np.max(np.abs(d))
        
        self.error = (max_* (self.x[-1]-self.x[0])**3 )/(12*(len(self.x)-1)**2)
        
        return self.error


# In[37]:


exp = lambda x: np.exp(-x**2)
N = 12
x = np.linspace(0,1,N+1)
y = exp(x)


# In[38]:


int1 = Integrator(x,y)
int1


# In[39]:


int1.Trapezoid()


# In[40]:


int1.GetTrapezoidError(exp)


# In[ ]:





# In[ ]:




