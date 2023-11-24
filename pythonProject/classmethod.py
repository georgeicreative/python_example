class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return point(x,y)

p1 = point(2,3)
p2 = point(1,3)
p3 = p1+p2
print(p3)

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __lt__(self, other):
        return self.age < other.age

p1 = person('alice',20)
p2 = person('bob',22)

print(p1<p2)
print(p2>p2)
