import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

'''Plot Number 1'''

ax = plt.axes(projection='3d')

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

ax.scatter(x,y,z)
ax.set_title('3D Plot')
ax.set_xlabel('Test')
plt.show()


'''Plot Number 2'''

ax = plt.axes(projection='3d')

x = np.arange(0,50,0.1)
y = np.sin(x)
z = np.cos(x)

ax.plot(x,y,z)
ax.set_title('3D Plot')
ax.set_xlabel('Test')
plt.show()


'''Plot Number 3'''

ax = plt.axes(projection='3d')

x = np.arange(0,50,0.1)
y = np.arange(0,50,0.1)
z = np.cos(x + y)

ax.plot(x,y,z)
ax.set_title('3D Plot')
ax.set_xlabel('Test')
plt.show()


'''Plot Number 4'''

ax = plt.axes(projection='3d')

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)

X,Y = np.meshgrid(x,y)

Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X,Y,Z,cmap='Spectral')
ax.set_title('3D Plot')
ax.set_xlabel('Test')
ax.view_init(azim=0, elev=90)     # This values of azim and elev will allow you to see the above 3D plot from above

plt.show()