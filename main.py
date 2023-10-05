from __future__ import print_function
import torch
import torch.nn as nn
import matplotlib.pylab as plt
from torch.utils.data import DataLoader
from model.ConvolutionalNNModel import ConvolutionalNNModel
from data.ImageDataset import getTrainDataset, getValidationDataset
from utils.CNNModelUtil import showData
import argparse

parser = argparse.ArgumentParser(description="CNN Model using PyTorch")
parser.add_argument('--seed', type=int, default=1, metavar='S', help='random seed (default : 1')
parser.add_argument('--train', action='store_true', help='training a CNN model')
parser.add_argument('--evaluate', action='store_true', help='evaluating a trained CNN model by a tensor')
parser.add_argument('--learning_rate', type=float, default=0.01, metavar='LR',
                    help='learning rate for training (default : 0.01)')
parser.add_argument('--outf', default='/output', help='folder for output images and model checkpoints')
parser.add_argument('--ckpf', default='', help='path to model checkpoint file to continue training')

args = parser.parse_args()
lr = args.learning_rate

# Is CUDA available?
cuda = torch.cuda.is_available()
print("Is cuda available: ", cuda)
# Seed for replication
torch.manual_seed(args.seed)
if cuda:
    torch.cuda.manual_seed(args.seed)


def save_checkpoints(model):
    chkp = model.state_dict()
    path = "./output/model_checkpoint.pt"
    torch.save(chkp, path)
    print("Training model checkpoint saved ")


def train_model(model, train_loader, validation_loader, optimizer, n_epochs=5):
    # global variable
    N_test = len(getValidationDataset(16))
    print(" Number of test images: ", N_test)
    accuracy_list = []
    loss_list = []
    criterion = nn.CrossEntropyLoss()

    for epoch in range(n_epochs):
        for x, label in train_loader:
            # call train() on model which extents nn.module
            if cuda:
                x, label = x.cuda(), label.cuda()
                model = model.cuda()

            model.train()
            # reset the weights derivative values
            optimizer.zero_grad()
            # predict the output
            pred = model(x)
            # calculate Cross entropy loss
            loss = criterion(pred, label)
            # Calculate derivative of loss w.r.t weights
            loss.backward()
            # update the weights value
            optimizer.step()

            loss_list.append(loss.data)

        correct = 0

        # perform a prediction on the validation  data
        for x_test, y_test in validation_loader:
            if cuda:
                x_test, y_test = x_test.cuda(), y_test.cuda()

            model.eval()
            output = model(x_test)
            # get index of maximum value : argmax
            _, yhat = torch.max(output.data, 1)
            correct += (yhat == y_test).sum().item()

        accuracy = correct / N_test
        print(f' accuracy at epoch {epoch}: {accuracy}')
        accuracy_list.append(accuracy)

    save_checkpoints(model)
    return accuracy_list, loss_list


if args.train:
    model = ConvolutionalNNModel(input_channel=1, output_channel=10, need_BN=True)
    loss = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)
    train_dataset = DataLoader(dataset=getTrainDataset(16), batch_size=100)
    val_dataset = DataLoader(dataset=getValidationDataset(16), batch_size=5000)
    showData(getValidationDataset(16)[3], 16)

    print("Before Training starts: ")
    ACC, LOSS = train_model(model=model, train_loader=train_dataset, validation_loader=val_dataset, optimizer=optimizer)
    print("After Training ends: ")
    # Plot out the Loss and iteration diagram
    plt.plot(LOSS)
    plt.xlabel("batch iterations ")
    plt.ylabel("Cost/total loss ")
    plt.show()
