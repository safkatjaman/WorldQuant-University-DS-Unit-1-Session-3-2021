%logstop
%logstart -rtq ~/.logs/vc.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:18:40
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def __repr__(self):
        return f"Point({self.x}, {self.y})"# Wed, 17 Nov 2021 05:18:44
point_O = Point(5,3)
print(point_O)# Wed, 17 Nov 2021 05:18:45
grader.score.vc__point_repr(lambda points: [str(Point(*point)) for point in points])# Wed, 17 Nov 2021 05:18:53
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, point):
        if isinstance(point, Point):
            return Point(self.x + point.x, self.y + point.y)
        else:
            print('Error, We cannot do this operand')
            
    def __sub__(self, point):
        if isinstance(point, Point):
            return Point(self.x - point.x, self.y - point.y)
        else:
            print('Error, We cannot do this operand')# Wed, 17 Nov 2021 05:19:00
point = Point(5, 3)
print(point + Point(1, 2))# Wed, 17 Nov 2021 05:19:03
from functools import reduce
def add_sub_results(points):
    points = [Point(*point) for point in points]
    return [str(reduce(lambda x, y: x + y, points)), 
            str(reduce(lambda x, y: x - y, points))]

grader.score.vc__add_subtract(add_sub_results)# Wed, 17 Nov 2021 05:19:10
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    """
    def __add__(self, point):
        if isinstance(point, Point):
            return Point(self.x + point.x, self.y + point.y)
        else:
            print('Error, We cannot do this operand')
    """
    
    def __mul__(self, sca_pt):
        if isinstance(sca_pt, int):
            return Point(self.x * sca_pt, self.y * sca_pt)
        elif isinstance(sca_pt, Point):
            return self.x * sca_pt.x + self.y * sca_pt.y
        else:
            print('Error, We cannot do this operand')# Wed, 17 Nov 2021 05:19:16
point = Point(22898, 793800)
print(point * 1 * Point(1, 1))# Wed, 17 Nov 2021 05:19:16
def mult_result(points):
    points = [Point(*point) for point in points]
    return [point*point*2 for point in points]

grader.score.vc__multiplication(mult_result)# Wed, 17 Nov 2021 05:19:30
from math import sqrt

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p_2):
        if isinstance(p_2, Point):
            return sqrt((self.x - p_2.x)**2 + (self.y - p_2.y)**2)
        else:
            print('Error, We cannot do this operand')      
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"# Wed, 17 Nov 2021 05:19:32
def dist_result(points):
    points = [Point(*point) for point in points]
    return [points[0].distance(point) for point in points]

grader.score.vc__distance(dist_result)# Wed, 17 Nov 2021 05:19:39
class Cluster(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.center = Point(self.x, self.y)
        self.points = [self.center]
    
    def update(self):
        xSum = 0
        ySum = 0
        for i in self.points:
            xSum += i.x
            ySum += i.y
        self.center = Point(xSum/(len(self.points)), ySum/(len(self.points)))
        self.points =[self.center]
    
    def add_point(self, point):
        self.points.append(point)# Wed, 17 Nov 2021 05:19:45
def compute_result(points):
    points = [Point(*point) for point in points]
    a = Cluster(1,0)
    b = Cluster(-1,0)
    a_old = []
    for _ in range(10000): # max iterations
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                a.add_point(point)
            else:
                b.add_point(point)
        if a_old == a.points:
            break
        a_old = a.points[:]
        a.update()
        b.update()
    
    if a.center.x > b.x:
        return [(a.center.x, a.center.y), (b.center.x, b.center.y)]
    else:
        return [(b.center.x, b.center.y), (a.center.x, a.center.y)]# Wed, 17 Nov 2021 05:19:47
grader.score.vc__k_means(compute_result)# Wed, 17 Nov 2021 05:20:36
grader.score.vc__k_means(compute_result)%logstop
%logstart -rtq ~/.logs/vc.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/vc.py append
import seaborn as sns
sns.set()
