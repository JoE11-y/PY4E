def chop(t):
    t.pop(0)
    t.pop(-1)

    #or
def chops(t):
    del t[0]
    del t[-1]


#b
def middle(t):
    t[1:-1]
