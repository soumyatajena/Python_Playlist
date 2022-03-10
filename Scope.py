def outer():
    x="local"
    def inner():
        nonlocal x
        x="nonlocal" # Parent Local
        print('inner:',x)
    inner()
    print("outer:",x)
outer()

# inner: nonlocal
# outer: nonlocal

def outer():
    x="local"
    def inner():
        x="nonlocal" # Local
        print('inner:',x)
    inner()
    print("outer:",x)
outer()

# inner: nonlocal
# outer: local

x="global"
def outer():
    x="local"
    def inner():
        x="nonlocal"
        print('inner:',x)
    inner()
    print("outer:",x)
outer()
print("global:",x)

# inner: nonlocal
# outer: local
# global: global