def arrsorting():
    arr=[]
    b=int(input("enter the size of array"))
    for i in range(0,b):
        c=int(input("enetr element of the array"))
        arr.append(c)
    print("array before sorting=",arr)
    arr.sort()
    print("array after sorting =",arr)
arrsorting()

