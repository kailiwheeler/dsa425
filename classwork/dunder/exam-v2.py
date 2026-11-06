import numpy as np

class Dataset():
    def __init__(self,images,transform=None):
        self.images = images
        self.transform = transform
    def __getitem__(self, index):
        image = self.images[index]
        if self.transform:
            return self.transform(image)
        return image
    def __iter__(self):
        if self.transform:
            return iter([self.transform(i) for i in images])
        return iter(images)
    def __str__(self):
        return str(images)

class flip():
    def __init__(self):
        pass
    def __call__(self,image):
        return flip_array(image)

def flip_array(image):
    n_row, n_col = image.shape
    for i in range(n_row):
        for j in range(n_col//2):
            temp = image[i,j]
            image[i,j] = image[i,-j-1]
            image[i,-j-1] = temp
    return image

my_flip = flip()


img1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
img2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
images = [img1, img2]
my_images = Dataset(images,my_flip)
print(my_images)
# print(my_images[0])
# print(my_images[1])
for i in my_images:
    print(i)