# importing libraries
from genericpath import isdir
from random import choices
from sys import stderr, stdout
import sys
import shutil
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import u2net_test
import is_net_test
import subprocess

original_path = "data/images"
u2net_path = "data/u2net_results"
isnet_path = "data/is_net_results"
tracer_path = "mask/images"

def get_image_mask(ind):
    original_files = sorted(os.listdir(original_path))
    u2net_files = sorted(os.listdir(u2net_path))
    isnet_files = sorted(os.listdir(isnet_path))
    tracer_files = sorted(os.listdir(tracer_path))
    l = len(original_files)

    original = original_files[ind]
    original = cv2.imread(original_path + '/' + original)

    u2net = u2net_files[ind]
    u2net = cv2.imread(u2net_path + '/' + u2net)

    isnet = isnet_files[ind]
    isnet = cv2.imread(isnet_path + '/' + isnet)

    tracer = tracer_files[ind]
    tracer = cv2.imread(tracer_path + '/' + tracer)

    return original, u2net, isnet, None


def choose_mask(source):   
    original_files = sorted(os.listdir(original_path))
    l = len(original_files)
        
    plt.ion()
    fig, plts = plt.subplots(1, 4)
    fig.set_size_inches(15, 7)

    choices = []

    for ind in range(l):
        o, u2, i, t = get_image_mask(ind)
        imgs = [o, u2, i, t]

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

        choice = int(input("Chooce the mask (1/2/3): "))
        choices.append(choice)
        
        print(choice, choices)
        
        if not os.path.isdir(source + 'results/'):
            os.mkdir(source + 'results/')
        file_name = source + 'results/' + original_files[ind]
        cv2.imwrite(file_name, imgs[choice])
        print(file_name, "saved")
        
    return choices


def main():    
    if not os.path.isdir(sys.argv[1]):
        print("Give a valid path!")
        return
    
    source = sys.argv[1]
    if source[-1] != '/':
        source = source + '/'
    destination = 'data/images'
    
    print("Copying files from " + source + " to " + destination)
    
    pre_data = ['data/images', 'data/is_net_results',
                'data/u2net_results', 'mask/images', 'object/images']
    for direc in pre_data:
        for f in os.listdir(direc):
            os.remove(os.path.join(direc, f))

    allfiles = os.listdir(source)
    
    for f in allfiles:
        src_path = os.path.join(source, f)
        
        if os.path.isdir(src_path):
            continue
        shutil.copy2(src_path, destination)
        
    process = subprocess.Popen(["bash", "tracer_run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    sys.stdout.buffer.write(stdout)
    # sys.stdout.buffer.write(stderr)
    sys.stdout.buffer.flush()
    process.stdout.close()
    process.wait()

    u2net_test.main()
    is_net_test.main()
    choices = choose_mask(source)
    print(choices)
    
if __name__ == '__main__':
    main()
