#binary search：
'''
Points:
update start as mid + 1
return start at the end
f(mid): three sum questions, 'sum == target'
g(mid): usually 'nums[mid] > target'
'''
def binary_search(start, end):
    while start < end:
        mid = start + (end - start) // 2
        if f(mid):    #optional
            return mid
        if g(mid):
            end = mid   # new range, [start, mid)
        else:
            start = mid + 1 # new range [mid+1, end)
    return start    # or not found
