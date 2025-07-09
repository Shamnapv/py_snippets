import matplotlib.pyplot as plt;
fruits=["apple" , "orange" , "banana" , "papaya" ]
count=[20,30,10,40]
#line plot
plt.figure(figsize=(8, 4))
plt.subplot(1,3,1)
plt.plot(fruits,count,marker='o',linestyle='--',linewidth=2,color='red')
plt.grid(True,linestyle='-',alpha=0.2)
plt.title("count of fruits")
plt.xlabel("fruits")
plt.ylabel("count")
#pie plot
plt.subplot(1,3,2)
plt.pie(count,labels=fruits,autopct='%1.1f%%',startangle=90,colors=['red','orange','yellow','green'])
plt.axis('equal')
plt.title("count of fruits")
#bar plot
plt.subplot(1,3,3)
color=['red','orange','yellow','green']
plt.bar(fruits,count,color=color)
plt.title("count of fruits")
plt.xlabel("fruits")
plt.ylabel("counts")
plt.grid(True,linestyle='--',alpha=0.2)

plt.tight_layout()
plt.show()
