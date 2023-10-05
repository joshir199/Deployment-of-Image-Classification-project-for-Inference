# Model graph flow
"""
Input (1 channel)
   |
   v
Conv2d (16 filters, kernel=5x5)
   |
   v
BatchNorm2d
   |
   v
MaxPool2d (kernel=2x2)
   |
   v
Conv2d (32 filters, kernel=5x5)
   |
   v
BatchNorm2d
   |
   v
MaxPool2d (kernel=2x2)
   |
   v
Flatten
   |
   v
Linear (output=10)
   |
   v
BatchNorm1d
   |
   v
Output (10 classes)
"""



# model summary
"""
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 16, 16, 16]             416
       BatchNorm2d-2           [-1, 16, 16, 16]              32
         MaxPool2d-3             [-1, 16, 8, 8]               0
            Conv2d-4             [-1, 32, 8, 8]          12,832
       BatchNorm2d-5             [-1, 32, 8, 8]              64
         MaxPool2d-6             [-1, 32, 4, 4]               0
            Linear-7                   [-1, 10]           5,130
       BatchNorm1d-8                   [-1, 10]              20
================================================================
Total params: 18,494
Trainable params: 18,494
Non-trainable params: 0

Note : It also contains trainable parameters for Batch Normalisation:
 1. Scaling parameters: (number of output channels) (std. deviation)
 2. Shifting parameters: (number of output channels) (std. mean)
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.25
Params size (MB): 0.05
Estimated Total Size (MB): 0.30
----------------------------------------------------------------

"""
