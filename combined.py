# importing libraries
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt


def get_image_mask(ind):
    original = original_files[ind]
    original = cv2.imread(original_path + '/' + original)

    u2net = u2net_files[ind]
    u2net = cv2.imread(u2net_path + '/' + u2net)

    isnet = isnet_files[ind]
    isnet = cv2.imread(isnet_path + '/' + isnet)

    tracer = tracer_files[ind]
    tracer = cv2.imread(tracer_path + '/' + tracer)

    return original, u2net, isnet, tracer


original_path = "image_masking_SI/data/images"

u2net_path = "Image-Masking/data/u2net_results"
isnet_path = "image_masking_SI/data/is_net_results"
tracer_path = "TRACER/mask/custom_dataset"

original_files = sorted(os.listdir(original_path))
u2net_files = sorted(os.listdir(u2net_path))
isnet_files = sorted(os.listdir(isnet_path))
tracer_files = sorted(os.listdir(tracer_path))
l = len(original_files)

plt.ion()
fig, plts = plt.subplots(1, 4)
fig.set_size_inches(15, 7)

choices = []

for ind in range(75):
    o, u2, i, t = get_image_mask(ind)

    plts[0].imshow(o)
    plts[0].set_title("Original image")

    plts[1].imshow(u2)
    plts[1].set_title("U2-net mask")

    plts[2].imshow(i)
    plts[2].set_title("IS-net mask")

    plts[3].imshow(t)
    plts[3].set_title("TRACER mask")
    
    fig.canvas.draw()
    fig.canvas.flush_events()

    # print('combined/' + original_files[ind][:-3] + 'png', "saved")
    # plt.savefig('combined/' + original_files[ind][:-3] + 'png')
    # plt.show()
    choice = int(input("Chooce the mask : "))
    choices.append(choice)














# creating initial data values
# of x and y
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# # to run GUI event loop
# plt.ion()

# # here we are creating sub plots
# figure, ax = plt.subplots(figsize=(10, 8))
# line1, = ax.plot(x, y)

# # setting title
# plt.title("Geeks For Geeks", fontsize=20)

# # setting x-axis label and y-axis label
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# aas = []
# # Loop
# for _ in range(10):
# 	# creating new Y values
#     new_y = np.sin(x-0.5*_)

#     # updating data values
#     line1.set_xdata(x)
#     line1.set_ydata(new_y)

#     # drawing updated values
#     figure.canvas.draw()

#     # This will run the GUI event
#     # loop until all UI events
#     # currently waiting have been processed
#     figure.canvas.flush_events()
#     a = int(input("Enter : "))
#     aas.append(a)

# 	# time.sleep(0.1)
    
