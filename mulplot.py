import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [elem * elem * elem for elem in x]


print(y)
plt.plot([1,2,3,4], [1,4,9,16], 'go', x, y, "r^")
#plt.show()

# Telling them apart


labels = ["Squares","Cubes"]

#plt.plot([1,2,3,4], [1,4,9,16], ’go’, label=labels[0])

plt.plot(x,[1,4,9,16], label=labels[0])
plt.plot(x,y,label = "cubes")
plt.legend()
plt.show()