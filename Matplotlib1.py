"""from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.show()"""

"""from matplotlib import pyplot as plt
x = [1,2,3]
y = [4,5,1]
plt.plot(x,y)
plt.title('info')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()"""

from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
x = [5,8,6]
y = [12,6,7]
x2 = [8,9,9]
y2 = [11,3,2]
plt.plot(x,y,"g",label = "lineone", linewidth = 6)
plt.plot(x2,y2,"c", label = "linetwo", linewidth = 6)
plt.title("Epic Info")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.grid(True, color="k")
plt.show()