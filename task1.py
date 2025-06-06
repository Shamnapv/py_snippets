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

"""output:
(base) PS C:\Users\shaim\Desktop\pythonlab> python task1.py 
enter the size of array5
enetr element of the array1
enetr element of the array10
enetr element of the array8
enetr element of the array2
enetr element of the array9
array before sorting= [1, 10, 8, 2, 9]
array after sorting = [1, 2, 8, 9, 10]"""
