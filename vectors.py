import math

#scalar multiple
#a is a scalar, b is a vector
def scalermult(a, b):
        v = []
        for x in b:
                v.append(x * a)
        return v
#add vectors
#a is vector, b is vector
def add(a, b):
        v = []
        for x in range(len(a)):
                v.append(a[x] + b[x])
        return v
#subtract vectors
#a is vector, b is vector
def subtract(a, b):
        v = []
        for x in range(len(a)):
                v.append(a[x] - b[x])
        return v

#change into a unit vector
#a is a vector
def unitv(a):
        v = []
        m = magnitude(a)
        if m == 0:
                return [0, 0, 0]
        else:
                for x in a:
                        v.append(x / m)
                return v

#Changes 2 points into vector form in 3d space
#given 2 points (x,y,z)
def vform(a, b):
        r0 = a
        u = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]
        r = [r0, u]
        return r

#dot product with 2 vectors
#a is vector, b is vector
def dotproduct1(a, b):
        t = 0
        for x in range(len(a)):
                t += a[x] * b[x]
        return t
#dot product with angle
#ma is scaler, mb is scalar, angle is scalar
def dotproduct2(ma, mb, angle):
        return ma * mb * math.cos(angle)
#magnitude
#a is vector
def magnitude(a):
        t = 0
        for x in a:
                t += math.pow(x, 2)
        return math.sqrt(t)
#proj_a b
#a is vector, b is vector
def projection(a, b):
        ma = magnitude(a)
        mb = magnitude(b)
        d = dotproduct1(a, b)
        return scalermult((d/math.pow(magnitude(a), 2)), a)
#distance of point to line
#a is a line in vector form, b is a point (x, y, z)
def ptToLine(a, b):
        r = a[1]
        P = b
        P0 = a[0]
        PP = [P[0] - P0[0], P[1] - P0[1], P[2] - P0[2]]
        return magnitude(subtract(PP, projection(r, PP)))

#distance of point to line
#a and b are 2 points that make up a line
#c is the other point not on the line
def ptToLine2(a, b, c):
        return ptToLine(vform(a, b), c)
