import numpy as np
import scipy.integrate as integrate

'''
args
    (x0,y0) - Coordinates of the point on circle
    (x1,y1) - Coordinates of the point instide the disk
    theta - angle of intersection line with x-axis positive direction
    r - radius of the circle
return
    x1 - x coordinate of the first intersection
    y1 - y coordinate of the first intersection
    x2 - x coordinate of the second intersection
    y2 - y coordinate of the second intersection
'''
def  getIntersectionPoints(x,y,theta,r):
    #Getting coeffiecents for intersecting line's the linear equation where y = ax + b
    a = np.tan(theta)
    b = y - a*x

    #Solving quadric equation to find intesection's x coordinats
    D = (a**2)*(b**2) - (b**2-r**2)*(a**2+1)
    x1 = (-a*b-np.sqrt(D))/(a**2+1)
    x2 = (-a*b+np.sqrt(D))/(a**2+1)

    #Calculating y coordinats of intesection points
    y1 = a*x1+b
    y2 = a*x2+b

    return (x1,y1,x2,y2)

'''
args
    (x0,y0) - Coordinates of the first point on circle
    (x1,y1) - Coordinates of the second point instide the disk
return
    distance between points
'''
def distanceBetweenPoints(x1,y1,x2,y2):
    return np.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

def test_bdry_func(x,y):
    return y+x

'''
args
    P_x - x coordinates of point inside disk
    p_y - y coordinates of point inside disk
    r - radius of disk
    bdry_func - boundry function
return
    function that is integrable over theta
'''
def integrable(P_x,P_y,r,bdry_func):
    def bdry(theta):
        (x1,y1,x2,y2) = getIntersectionPoints(P_x,P_y,theta,r)
        r1 = distanceBetweenPoints(x1,y1,P_x,P_y)
        r2 = distanceBetweenPoints(x2,y2,P_x,P_y)
        f1 = bdry_func(x1,y1)
        f2 = bdry_func(x2,y2)
        return (r1*f2+r2*f1)/(r1+r2)
    return bdry

'''
args
    x - x coordinates of point inside disk
    y - y coordinates of point inside disk
    r - radius of disk
    bdry - boundry function
return
    value of harmonic function at that point with given boundry function
'''
def compute(x,y,r,bdry):
    return integrate.quad(integrable(x,y,r,bdry), 0, 2*np.pi)[0]/(2*np.pi)

#print( compute(1,3,10,test_bdry_func) )
