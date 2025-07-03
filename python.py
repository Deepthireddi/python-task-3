x = 10
def show():
    x = 5
    print(x)
show()
print(x)
#for the above code the output is 5
                                  10
#because, it is a local variable.we have x=5 inside the function and show()runs that and print 5 first after that outside function will print as 10.


def outer():
    x = 10
    def inner():
        print(x)
    inner()
outer()
#for the above code the output is 10.
#Inside outer() function, we have x = 10.Then there’s another function inner() inside it.Inside inner() we print(x).Inner function uses the nearest available x then print x=10


x = "global"
def outer():
    x = "outer"
    def inner():
        x = "inner"
    inner()
    print("outer:", x)
outer()
print("global:", x)
#for the above code the output is :-
outer: outer  
global: global
#why beacuse, First outside x = "global"
#Inside outer()  again x = "outer"
#Inside inner()  again x = "inner"  In inner() you wrote x = "inner" but never printed, so nothing happens from there.
#Then print("outer:", x) runs, x is "outer" inside outer(), so prints that.
#Finally, outside print("global:", x) runs, x outside is still "global", so prints that.
 
