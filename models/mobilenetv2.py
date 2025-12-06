import torch
import torch.nn as nn

class MobileNetV2(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        # Simplified version for GitHub
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU6(),
        )
        self.classifier = nn.Linear(32, num_classes)
    
    def forward(self, x):
        x = self.features(x)
        x = x.mean([2, 3])
        x = self.classifier(x)
        return x
