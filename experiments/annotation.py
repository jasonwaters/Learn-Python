#Class Decorator
class callMeMaybe(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print "="*60
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__


@callMeMaybe
def func1():
    print "inside func1()"

@callMeMaybe
def func2():
    print "inside func2()"


func1()
func2()



#Function Decorator

def smarty(f):
    def new_f():
        print "="*60
        print "Entering", f.__name__
        f()
        print "Exited", f.__name__
    new_f.__name__ = f.__name__
    return new_f

@smarty
def func3():
    print 'inside func3()'

@smarty
def func4():
    print 'inside func4()'

func3()
func4()