import h5py
import numpy as np
from PIL import Image
import py4DSTEM
import os
from py4DSTEM.visualize import show
import matplotlib.pyplot as plt
import yaml

py4DSTEM.check_config()
py4DSTEM.io.print_h5_tree("${reads}.h5")
# data from the image
filename = "${reads}.h5"
bname = os.path.basename(filename)
plt_bname = f"{bname.split('.')[0]}"
virtual_detector = py4DSTEM.io.read(filename, data_id="virtual_detector_depth0000")
inner_angle = 11
outer_angle = 20
virtual_detected = virtual_detector.data[:, :, inner_angle:outer_angle]
sum_slice = np.sum(virtual_detected, axis=-1)
cmap = "gray"
max_angle = virtual_detector.data.shape[-1]
inner_angles = [0, 11, 20, 61]
outer_angles = [20, 20, 40, max_angle]
labels = ["BF", "ABF", "ADF", "HAADF"]
data_list = []
for inner, outer in zip(inner_angles, outer_angles):
    im = virtual_detector.data[:, :, inner:outer]
    data_list.append(np.sum(im, axis=-1))

for i in range(4):
    fig = plt.imshow(data_list[i], cmap='gray', interpolation=None, resample=False)
    plt.axis("off")
    fpath = f"${start}/{plt_bname}_{labels[i]}.tiff"
    plt.savefig(fpath, bbox_inches="tight", pad_inches=0)

# angular analysis
angular_detect = py4DSTEM.io.read("${reads}.h5", data_id='annular_detector_depth0000')
print(angular_detect.data)