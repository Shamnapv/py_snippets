s1={1,2,3,4,5}
s2={6,7,8,9}
print("original set:",s1)
print("After adding",s1.add(6))
s1.remove(2)
print("After removing usind remove():",s1)
s1.discard(3)
print("After removing using discard():",s1)
s1.pop()
print("After removing using pop():",s1)
s3=s1.intersection(s2)
print("After intersection:",s3)
s4=s1.union(s2)
print("After union:",s4)
s5=s1.copy()
print("After copy():",s5)
s4.difference_update(s2)
print("After difference_update:",s4)
print("before intersection_update():",s1)
s1.intersection_update(s4)
print("After intersection_update():",s1)
print("After isdisjoint():",s4.isdisjoint(s2))
s1.update(s2)
print("After update:",s1)
print("After issubset():",s1.issubset(s2))
print("After issuperset():",s1.issuperset(s2))
print("After clear():",s1.clear())

"""output:(base) PS C:\Users\shaim\Desktop\pythonlab> python task6d.py
original set: {1, 2, 3, 4, 5}
After adding None
After removing usind remove(): {1, 3, 4, 5, 6}
After removing using discard(): {1, 4, 5, 6}
After removing using pop(): {4, 5, 6}
After intersection: {6}
After union: {4, 5, 6, 7, 8, 9}
After copy(): {4, 5, 6}
After difference_update: {4, 5}
before intersection_update(): {4, 5, 6}
After intersection_update(): {4, 5}
After isdisjoint(): True
After update: {4, 5, 6, 7, 8, 9}
After issubset(): False
After issuperset(): True
After clear(): None"""
