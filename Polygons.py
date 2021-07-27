# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 23:13:07 2021

@author: AKayal
"""
import Polygon
from Polygon import *

import itertools
from collections import namedtuple


class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        # self._m = m
        # self._R = R
        
        self.Polygons_n = m
        self.Polygons_R = R
        
        self._polygons = Polygons_area
        
        # self._polygons = [Polygon(i, R) for i in range(3, m+1)]
        self._index = 0
        
    @property
    def Polygons_area(self):
        self._polygons
        
    @property
    def Polygons_n(self):
        self.m

    @property
    def Polygons_R(self):
        self.R

    @Polygons_area.setter
    def Polygons_area(self):
        self._polygons = [Polygon(i, self.R) for i in range(3, self.m+1)]
        return self._polygons 
        
    @Polygons_n.setter
    def Polygons_n(self,m):
        return self.m

    @Polygons_R.setter
    def Polygons_R(self, R):
        return self.R
    
        
    def __len__(self):
        return self._m - 2
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __getitem__(self, s):
        return self._polygons[s]
    
    def __iter__(self):
        self
    
    def __next__(self):
        if self._index >= self._m:
            raise StopIteration
        else:
            item = self._polygons[self.__index]
            self._index += 1
            return item
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]