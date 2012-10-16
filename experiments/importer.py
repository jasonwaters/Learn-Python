
A = "importer A"
B = "importer B"

print A
print B


try:
    from imported import *
except:
    pass

print A
print B