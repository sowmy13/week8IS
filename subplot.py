import matplotlib.pyplot as plt

plt.figure(figsize =(10,5))
plt.subplot(1,2,1)
plt.plot([1,2,3,4],[1,4,9,16],'g-o')
plt.title("Square Data")

plt.subplot(1,2,2)
plt.plot([1,2,3,4],[1,8,29,66],'r-o')
plt.title("2nd cubic subplot")

plt.suptitle("All of my plots")
plt.show()
