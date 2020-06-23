#binary search：
def binary_searche(l, r):
    while l < r:
        m = l + (r - l) // 2
        if f(m):    #optional
            return m
        if g(m):
            r = m   # new range [l, m)
        else:
            l = m + 1 # new range [m+1, r)
    return l    # or not found
