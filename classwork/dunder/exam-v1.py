import numpy as np

class Dataset():
    def __init__(self,images):
        self.images = images
    def __getitem__(self, index):
        return self.images[index]
    def __iter__(self):
        return iter(self.images)
    def __str__(self):
        return str(images)

class flip():
    def __init__(self):
        pass
    def __call__(self,my_data):
        return [flip_array(i) for i in my_data]

def flip_array(image):
    n_row, n_col = image.shape
    for i in range(n_row):
        for j in range(n_col//2):
            temp = image[i,j]
            image[i,j] = image[i,-j-1]
            image[i,-j-1] = temp
    return image

img1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
img2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
images = [img1, img2]
my_images = Dataset(images)
print(my_images)
my_flip = flip()
flipped_images = my_flip(my_images)
print(flipped_images)
