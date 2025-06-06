f=open("output.txt","w")
print("hii everyone", file=f)
print("hello world...", file=f, flush=True)
x=10
print(f"processing {x}", flush=True)
f.close()

"""output:
    (base) PS C:\Users\shaim\Desktop\pythonlab> python task2a.py
    processing 10

    output.txt:
      hii everyone
      hello world..."""
