try:
    import psyco
    psyco.full()
except ImportError:
    pass

def count3(limit=5):
    l = []
    for i in range(limit):
        l.append(i)

def count1(limit=50000):
    x = 0
    for i in range(0, limit):
        count3()
        x += i

    return x

def count2(limit=150000):
    x = 0
    for i in range(0, limit):
        count3(10)
        x += i

    return x
