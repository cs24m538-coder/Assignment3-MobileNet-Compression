import torch
from models.mobilenetv2 import MobileNetV2
from compression.quantizer import compress_model
from data.data_loader import get_cifar10_loaders
import argparse

def test_compression(bits=8):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # Load model
    model = MobileNetV2(num_classes=10)
    
    # Apply compression
    compressed_model = compress_model(model, bits=bits)
    compressed_model = compressed_model.to(device)
    
    # Test
    _, test_loader = get_cifar10_loaders(batch_size=100)
    
    correct = total = 0
    with torch.no_grad():
        for inputs, targets in test_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = compressed_model(inputs)
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()
    
    accuracy = 100. * correct / total
    print(f"{bits}-bit accuracy: {accuracy:.2f}%")
    
    return accuracy

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type=int, default=8)
    args = parser.parse_args()
    
    test_compression(args.bits)
