import torch
import torch.nn as nn
import torch.optim as optim
from models.mobilenetv2 import MobileNetV2
from data.data_loader import get_cifar10_loaders

def train():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # Data
    train_loader, test_loader = get_cifar10_loaders(batch_size=128)
    
    # Model
    model = MobileNetV2(num_classes=10).to(device)
    
    # Training
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    for epoch in range(10):  # Short training for demo
        model.train()
        for inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
        
        print(f'Epoch {epoch} completed')
    
    print("Training complete!")

if __name__ == '__main__':
    train()
