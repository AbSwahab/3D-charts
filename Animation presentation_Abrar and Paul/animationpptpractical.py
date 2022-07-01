# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:09:41 2021

@author: Abrar Sami
"""


#                                         #3D scatter plot 
# import matplotlib.pyplot as plt
# ax = plt.axes(projection='3d')
# #to know the x y z sides 
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()

                                        #3D Cube
# # Import libraries
# import matplotlib.pyplot as plt
# #to have y x and z axes
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
  
  
# # to create axis x y z
# axes = [5, 5, 5]
  
# # Create Data
# data = np.ones(axes, dtype=np.bool)
  
# # to controll the tranperency
# alpha = 0.9
  
# # controling the color
# colors = np.empty(axes + [4], dtype=np.float32)
# #choose the color
# colors[:] = [1, 0, 0,alpha]

  
# # Plot figure
# fig = plt.figure()
# ax = plt.axes(projection='3d') 

# # # to customizations of the sizes, positions and colors
# ax.voxels(data, facecolors=colors)
# plt.show()






#                                         #3D colored Cube
# # Import libraries
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np


# # to create axis x y z
# axes = [5, 6, 7]

# # Create Data
# data = np.ones(axes, dtype=np.bool)

# # to controll the tranperency
# alpha = 0.9

# # ontroling the color
# colors = np.empty(axes + [4], dtype=np.float32)

# #to have many colors
# colors[0] = [1, 0, 0, alpha] # red
# colors[1] = [0, 1, 0, alpha] # green
# colors[2] = [0, 0, 1, alpha] # blue
# colors[3] = [1, 1, 0, alpha] # yellow
# colors[4] = [1, 1, 1, alpha] # grey

# # Plot figure
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # to customizations of the sizes, positions and colors and the edge color.
# ax.voxels(data, facecolors=colors, edgecolors='red')


                            #animation ball


# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d
# from numpy import sin, cos, pi, outer, ones, size, linspace


# a = linspace(0, 2 * pi)
# b = linspace(0, pi)
# x = 10 * outer(cos(a), sin(b))
# y = 10 * outer(sin(a), sin(b))
# z = 10 * outer(ones(size(a)), cos(b))

# #assign frame to 26
# frames = 26

# #call it to read all 26 frames and save it
# for n in range(frames):
#     fig = plt.figure(figsize=(10, 10))
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot_surface(x, y, z, color=('b'))
#     ax.set_xticks([])
#     ax.set_yticks([])
#     ax.set_zticks([])
#     ax.set_xlim(-8,8)
#     ax.set_xlim(-8,8)
#     ax.set_xlim(-8,8)
#     plt.savefig(f"{n}.png")
#     plt.close()
#     x += 1


# from PIL import Image
# #nameing the images 
# images = [Image.open(f"{n}.png") for n in range(frames)]
# #make it gif
# images[0].save('ball.gif', save_all=True, append_images=images[1:], duration=100, loop=0)

















