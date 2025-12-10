
import torch
import os
print("Creating placeholder model files...")
dummy_weights = {"layer1.weight": torch.randn(32, 3, 3, 3)}
torch.save(dummy_weights, "mobilenetv2_cifar10_final.pth")
os.makedirs("checkpoints", exist_ok=True)
torch.save({"model_state_dict": dummy_weights}, "checkpoints/latest.pth")
print("✅ Files created")
