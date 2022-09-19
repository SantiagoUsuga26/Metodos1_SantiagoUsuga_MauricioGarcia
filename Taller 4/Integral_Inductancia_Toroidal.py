#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# In[29]:


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
    
    def Simpson(self):
        
        self.integral = 0.
        
        self.integral += self.y[0] + self.y[-1]
        
        for i in range( len(y[1:-1]) ):
            if i%2 == 0:
                self.integral += 4*y[i+1]
            else:
                self.integral += 2*y[i+1]
                
        return self.integral*self.h/3
    
    def GetSimpsonError(self,f):
        
        d = (f( self.x + 2*self.h ) -              4*f( self.x + self.h ) +              6*f(self.x) -              4*f( self.x - self.h ) +              f(self.x - 2*self.h))/self.h**4
        
        max_ = np.max( np.abs(d) )
        
        self.error = (self.x[-1] - self.x[0])*self.h**4 * max_ / 180.
        
        return self.error


# In[30]:


induc = lambda x: (np.sqrt(0.01**2-x**2))/(0.5+x)
N = 12
x = np.linspace(-0.01,0.01,N+1)
y = induc(x)


# In[31]:


int1 = Integrator(x,y)
int1


# In[32]:


int1.Trapezoid()


# In[33]:


int1.GetTrapezoidError(induc)


# In[34]:


int1.Simpson()


# In[ ]:


int1.GetSimpsonError(induc)


# In[ ]:




