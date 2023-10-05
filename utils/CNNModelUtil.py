import torchvision.transforms as transforms
import matplotlib.pylab as plt


def getTransformFn(image_size):
    compose = transforms.Compose([transforms.RandomHorizontalFlip(),
                                  transforms.Resize((image_size, image_size)), transforms.ToTensor()])
    return compose


def showData(data_point, image_size):
    plt.imshow(data_point[0].numpy().reshape(image_size, image_size), cmap='gray')
    plt.title('y = ' + str(data_point[1]))
    plt.show()

