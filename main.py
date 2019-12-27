import func1
import func2

m = func1.math_class(10,4)
print("{} + {} = {}".format(m.mem1,m.mem2,m.sum()))
print("AVG({},{}) = {}".format(m.mem1,m.mem2,m.avg()))
print(func1.avg(m.mem1,m.mem2))
print("This line was added at the beginning of BR1")
del m
m = func2.func2_class
m.about()
del m
m = func2.func2_class
m.about()
del m
m = [[1,2],[2,3]]
print(m)
print(m[0])
print(m[1])
print(m[0:2])
del m
m = ((1,2),(3,4))
m1 = list(m)
print(m*2)
print("change on BR1")
print("BR3 added")