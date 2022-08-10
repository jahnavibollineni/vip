#skimage
#greyimage
import skimage
from matplotlib import pyplot as plt
from skimage import io
img3=io.imread('/home/matlab/Desktop/DIP3E_Original_Images_CH01/Fig0122(c)(skull).tif',0)
print(img3.shape)
plt.imshow(img3)
