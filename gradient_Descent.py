# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 09:11:08 2018

@author: sushi
"""
from numpy import *

def compute_error(b,m,points):
      totalError = 0
      for i in range(0,len(points)):
          x = points[i,0]
          y = points[i,1]
          totalError += (y-(m*x+b))**2
      return totalError/float(len(points))

def step_gredient(b_current,m_current,points,learning_rate):
    b_gredient = 0
    m_gredient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N)* (y-((m_current*x)+b_current))
        m_gradient += -(2/N)*x*(y-((m_current*x)+b_current))
    new_b = b_current - (learning_rate*b_gredient)
    new_m = m-current - (learning_rate * m_gredient)
    return(new_b,new_m)

def gredient_descent_runner(points,starting_b,starting_m,learning_rate,num_iteration):
    b = starting_b
    m = starting_m
    for i in range(num_iteration):
        b,m = step_gredient(b,m,array(points),learning_rate)
    return [b,m]

def run():
    points = genfromtext('data.csv',delimiter=',')
    learning_rate = 0.0001
    initial_b = 0
    initial_m =0
    num_iteration = 1000
    [b,m]=gredient_descent_runner(points,initial_b,initial_m,learning_rate,num_iteration)
    print(b)
    print(m)

if __name__ ==  '__main__':
    run()