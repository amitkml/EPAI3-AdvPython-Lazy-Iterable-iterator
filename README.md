# EPAI3-AdvPython-Lazy-Iterable-iterator
## Assignment

The starting point for this assignment is the `Polygon` class and the `Polygons` sequence type you created in the previous assignment.

The code for these classes along with the unit tests for the `Polygon` class are below if you want to use those as your starting point. But use whatever you came up with in the last project.

You have two goals:

**Goal 1:**

Refactor the `Polygon` class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our `Polygon` class "immutable").

 

**Goal 2:**

Refactor the `Polygons` (sequence) type, into an **iterable**. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

You'll need to implement both an iterable and an iterator.

## How I have achieved?

### Goal 1

In the Polygon class have added getter and setter as shown below. This allows to get the value and set the value.

```python
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
```

Have then defined two more property to calculate area and perimeter as shared below.

```python
    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem
    
    @property
    def perimeter(self):
        return self._n * self.side_length
```

### Goal 2

Polygons class again have their getter and setter as shown below.



```python
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
```

The max efficiency calculation function then calls the Polygon function area and perimeter as shown below.

```python
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]
```

