# Object Masking

Implemented [U2-net](https://github.com/neeraj361/Image-Masking), [IS-net](https://github.com/neeraj361/image_masking_SI) and [TRACER](https://github.com/neeraj361/TRAC) models.

U2-net, IS-net focus on
extracting distinct objects with edge information and aggregating multi-level features to improve object detection performance. 
TRACER detects objects with explicit
edges by incorporating attention guided tracing modules.

## Usage
<pre><code>
data
├── images
   ├── sample_image1.png
   ├── sample_image2.png
      .
      .
      .
</code></pre>
1. Clone this repo
```
git clone https://github.com/PoornaTheja/Object_Masking
```
2. Download the ```u2net.pth``` from [GoogleDrive](https://drive.google.com/file/d/1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ/view?usp=sharing)
3. Download the ```isnet-general-use.pth``` (for general use) from [GoogleDrive](https://drive.google.com/file/d/1nV57qKuy--d5u1yvkng9aXW1KS4sOpOi/view?usp=sharing)
2. You can add your images into 'data/images/'
3.  Run the combined model using  ``` python combined.py```. 
4. After generating masks for all the images, you can choose the best mask through STDIN.

## Requirements
* Python >= 3.7.x
* Pytorch >= 1.8.0
* albumentations >= 0.5.1
* tqdm >=4.54.0
* scikit-learn >= 0.23.2
* numpy 1.15.2  
* scikit-image 0.14.0  
* python-opencv
* PIL 5.2.0  
* torchvision 0.2.1  
* glob  

Install the requirements using
```
pip install -r requirements.txt
```

## References
* [U2-Net](https://github.com/xuebinqin/U-2-Net)
* [IS-Net](https://github.com/xuebinqin/DIS)
* [TRACER](https://github.com/Karel911/TRACER)