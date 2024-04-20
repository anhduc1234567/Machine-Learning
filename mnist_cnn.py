import torch
import torch.nn as nn
from torchvision import transforms as T
from torchvision import datasets
import torch.optim as optim
from torch.utils.data import DataLoader
from tqdm import tqdm

class MLPModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28,100)
        self.fc2 = nn.Linear(100, 10)
    def forward(self,x):
        x = x.view(x.shape[0],-1)
        out1 = nn.functional.relu(self.fc1(x))
        out2 = self.fc2(out1)
        return out2

def train_model(model,train_data_loader, optimizer):
    total = 0
    total_correct = 0
    pbar = tqdm(train_data_loader)
    for bx,by in pbar:
        out = model(bx)
        loss = nn.functional.cross_entropy(out,by)
        pred = torch.argmax(out,dim=1)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(pred,by)
        total_correct += (pred == by).sum().item()
        total += len(by)
        pbar.set_description(f"acc {total_correct / total:.4f}")
        break

def test_model(model,test_data_loader):
    total = 0
    total_correct = 0
    pbar = tqdm(test_data_loader)
    for bx,by in pbar:
        out = model(bx)
        loss = nn.functional.cross_entropy(out,by)
        pred = torch.argmax(out,dim=1)

        total_correct += (pred == by).sum().item()
        total += len(by)
        pbar.set_description(f"test acc {total_correct / total:.4f}")
if __name__ == "__main__":
    transform = T.Compose(
        [T.PILToTensor(),
        T.ConvertImageDtype(torch.float)]
    )

    mnist_train = datasets.MNIST('.\MachineLearning',train=True,download=True,transform=transform)
    train_dataloader = DataLoader(mnist_train,batch_size=16,shuffle=True)
    
    mnist_test = datasets.MNIST('.\MachineLearning',train=False,download=True,transform=transform)
    test_dataloader = DataLoader(mnist_test,batch_size=16,shuffle=False)

    model = MLPModule()
    opti = optim.SGD(model.parameters(),lr = 1e-3)       


    print9
    for x, y in mnist_train:
        print(y)
        break
    for bx,by in tqdm(train_dataloader):
        print(by.shape)
        break

    # train_model(model,train_dataloader,opti)
    # test_model(model,test_dataloader)