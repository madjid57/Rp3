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
