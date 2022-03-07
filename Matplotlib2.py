"""from matplotlib import pyplot as plt    #bargraph
plt.bar([1,5,8,4,3],[9,8,6,4,2], label = "Example1")
plt.bar([1,5,9,7,3],[8,5,2,4,1], label = "Example2", color='k')
plt.legend()
plt.title("Info")
plt.xlabel("bar number")
plt.ylabel("bar height")
plt.show()"""

"""from matplotlib import pyplot as plt
population_ages = [25,50,56,62,74,88,92,101,108,126,136,147,159,168,177,189,199,200]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins, histtype="bar", rwidth= 0.5)
plt.title("Histogram")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.show()"""

"""from matplotlib import pyplot as plt
x = [1,5,6,8,3]
y = [8,6,4,3,1]
plt.scatter(x,y, label = "scat", color='g')
plt.title("Scatter Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.show()"""

"""from matplotlib import pyplot as plt
days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
walking = [7,8,7,2,2]
playing = [8,5,7,8,13]
plt.plot([],[], color='m', label="sleeping", linewidth=5)
plt.plot([],[], color='c', label="eating", linewidth=5)
plt.plot([],[], color='r', label="walking", linewidth=5)
plt.plot([],[], color='k', label="playing", linewidth=5)
plt.stackplot(days, sleeping, eating, walking, playing, color =['m','c','r','k'])
plt.title("StackPlot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.show()"""

from matplotlib  import pyplot as plt
slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'walking', 'playing']
cols = ['m', 'r', 'c', 'b']
plt.pie(slices,
        labels = activities,
        colors = cols,
        startangle = 90,
        shadow = True,
        explode = (0,0, 0.1,0),
        autopct = ('%1.1f%%'))
plt.title("Pie Chart")
plt.legend()
plt.show()







