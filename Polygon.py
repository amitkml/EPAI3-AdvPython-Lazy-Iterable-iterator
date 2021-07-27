# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 23:13:07 2021

@author: AKayal
"""
import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        
        #self.frodo_r =  R
        self.frodo_n =  n
        self.frodo_r = R
        
        #self._n = n
        #self._R = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def frodo_n(self):
        return self._n
    
    @property
    def frodo_r(self):
        return self._R
    
    @frodo_n.setter
    def frodo_n(self,n):
        self._n = n

    @frodo_r.setter
    def frodo_r(self,R):
        self._R = R
        
    # @frodo_r.setter 
    # def frodo_r(self,R):
    #     self._R = R
        
    @property
    def frodo_R(self):
        return self._R
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem
    
    @property
    def perimeter(self):
        return self._n * self.side_length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented
